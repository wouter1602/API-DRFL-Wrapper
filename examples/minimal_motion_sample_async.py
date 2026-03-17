#!/usr/bin/env python3

import asyncio
import time
import numpy as np
import doosan_drfl as drfl
import sys

IP_ADDRESS = "127.0.0.1"
PORT = 12345

SPEED = 5.0  # deg/s
ACCELERATION = 5.0  # deg/s2
MOVE_TIMEOUT = 10.0  # seconds
POLL_INTERVAL = 0.05  # seconds (50ms polling rate)

VIRTUAL = False  # Will set the movement to be virtual (simulated)

robot = drfl.CDRFLEx()

# Global flags for connection state
get_control_access = False
is_standby = False

def on_monitoring_access_control(access: drfl.MONITORING_ACCESS_CONTROL) -> None:
    global get_control_access
    access_in_string = drfl.MONITORING_ACCESS_CONTROL(access).name
    print(f"[on_monitoring_access_control] Control Access: {access_in_string} [{access}]")
    if access == drfl.MONITORING_ACCESS_CONTROL.Grant:
        get_control_access = True
        print("Got Control Access!!")
    elif access == drfl.MONITORING_ACCESS_CONTROL.Loss:
        get_control_access = False

def on_monitoring_state(state: drfl.ROBOT_STATE) -> None:
    global is_standby
    state_in_string = drfl.ROBOT_STATE(state).name
    print(f"[on_monitoring_state] Robot State: {state_in_string} [{state}]")
    if state == drfl.ROBOT_STATE.Standby:
        is_standby = True
    else:
        is_standby = False

async def wait_for_standby(timeout: float) -> bool:
    """
    Asynchronously waits for the robot to reach Standby state.
    Returns True if successful, False if timeout occurs.
    """
    start_time = time.time()
    while not is_standby:
        await asyncio.sleep(POLL_INTERVAL)
        if time.time() - start_time > timeout:
            return False
    return True

async def main():
    global get_control_access, is_standby

    # 1. Setup Callbacks
    robot.set_on_monitoring_access_control(on_monitoring_access_control)
    robot.set_on_monitoring_state(on_monitoring_state)

    # 2. Connect
    print(f"Connecting to robot @ {IP_ADDRESS}:{PORT}...")
    ret = robot.open_connection(IP_ADDRESS, port=PORT)
    print(f"open_connection return value: {ret}")

    if not ret:
        print(f"Cannot open connection to robot @ {IP_ADDRESS}:{PORT}")
        raise SystemExit(1)

    robot.setup_monitoring_version(1)

    # 3. Version Check
    version = drfl.SYSTEM_VERSION()
    robot.get_system_version(version)
    print(f"Controller (DRCF) version: {version._szController}")
    print(f"Library version: {robot.get_library_version()}")

    # 4. Handshake: Get Access and Servo On
    # We use a loop with small sleeps to allow callbacks to fire
    for _ in range(10):
        if not get_control_access:
            robot.manage_access_control(drfl.MANAGE_ACCESS_CONTROL.Force_request)
            await asyncio.sleep(0.5)
            continue
        if not is_standby:
            robot.set_robot_control(drfl.ROBOT_CONTROL.Servo_on)
            await asyncio.sleep(1.0)
            continue
        break

    if not (get_control_access and is_standby):
        print("Failed setting intended states (Access or Servo)")
        robot.close_connection()
        raise SystemExit(1)

    # 5. Configure Robot
    if VIRTUAL:
        if not robot.set_robot_system(drfl.ROBOT_SYSTEM.Virtual):
            raise SystemExit(1)
    else:
        if not robot.set_robot_system(drfl.ROBOT_SYSTEM.Real):
            raise SystemExit(1)

    if not robot.set_robot_mode(drfl.ROBOT_MODE.Autonomous):
        raise SystemExit(1)

    print("\n--- Ready to Move ---")
    # Note: In a real async app, you might await user input differently,
    # but input() blocks the thread. We'll keep it simple here.
    input("Press Enter to continue...")

    # 6. First Movement (amovej)
    target_pos = np.array([0., 0., 30., 0., 0., 0.], dtype=np.float32)
    print(f"Sending amovej to target: {target_pos}...")

    if not robot.amovej(
        pos=target_pos,
        vel=SPEED,
        acc=ACCELERATION,
        time=0.0,
        move_mode=drfl.MOVE_MODE.Absolute,
        blending_type=drfl.BLENDING_SPEED_TYPE.Duplicate):
        print("Failed to execute amovej command")
        robot.close_connection()
        raise SystemExit(1)

    # Wait asynchronously for completion
    if not await wait_for_standby(MOVE_TIMEOUT):
        print("Move timed out waiting for Standby state")
        robot.close_connection()
        raise SystemExit(1)

    print("First target reached!")

    # 7. Second Movement
    target_pos[2] = 0.0
    print(f"Sending amovej to target: {target_pos}...")

    if not robot.amovej(
        pos=target_pos,
        vel=SPEED,
        acc=ACCELERATION,
        time=0.0,
        move_mode=drfl.MOVE_MODE.Absolute,
        blending_type=drfl.BLENDING_SPEED_TYPE.Duplicate):
        print("Failed to execute second amovej command")
        robot.close_connection()
        raise SystemExit(1)

    if not await wait_for_standby(MOVE_TIMEOUT):
        print("Second move timed out waiting for Standby state")
        robot.close_connection()
        raise SystemExit(1)

    print("Second target reached!")

    robot.close_connection()
    print("Connection closed.")
    sys.exit(0)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nInterrupted by user. Closing connection...")
        robot.close_connection()
        sys.exit(1)
