#!/usr/bin/env python3

import time
import numpy as np
import doosan_drfl as drfl
import sys

IP_ADDRESS = "127.0.0.1"
PORT = 12345

SPEED = 5.0 # deg/s
ACCELERATION = 5.0 # deg/s2
MOVE_TIMEOUT = 10.0 # seconds

VIRTUAL = False # Will set the movement to be virtual (simulated)

robot = drfl.CDRFLEx()

get_control_access: bool = False
is_standby: bool = False


"""
Callback function for monitoring access control.
"""
def on_monitoring_access_control(access: drfl.MONITORING_ACCESS_CONTROL) -> None:
    global get_control_access
    access_in_string = drfl.MONITORING_ACCESS_CONTROL(access).name
    print(f"[on_monitoring_access_control] Control Access: {access_in_string} [{access}]")
    if access == drfl.MONITORING_ACCESS_CONTROL.Grant:
        get_control_access = True
        print("Got Control Access!!")
    elif access == drfl.MONITORING_ACCESS_CONTROL.Loss:
        get_control_access = False


"""
Callback function for monitoring robot state.
"""
def on_monitoring_state(state: drfl.ROBOT_STATE) -> None:
    global is_standby
    state_in_string = drfl.ROBOT_STATE(state).name
    print(f"[on_monitoring_state] Robot State: {state_in_string} [{state}]")
    if state == drfl.ROBOT_STATE.Standby:
        is_standby = True
        print("Successfully Servo on!!")
    else:
        is_standby = False

def is_move_done(timeout: float) -> bool:
    start_time = time.time()
    while not is_standby:
        time.sleep(0.1)
        if time.time() - start_time > timeout:
            return False
    return True


def main():
    global get_control_access
    """
    Set up monitoring callbacks and connect to the robot.
    """
    robot.set_on_monitoring_access_control(on_monitoring_access_control)
    robot.set_on_monitoring_state(on_monitoring_state)

    ret = robot.open_connection(IP_ADDRESS, port=PORT) # Connect to the Robot

    print(f"open_connection return value: {ret}")
    if not ret:
        print(f"Cannot open connection to robot @ {IP_ADDRESS}:{PORT}")
        raise SystemExit(1)

    robot.setup_monitoring_version(1)

    version = drfl.SYSTEM_VERSION()
    robot.get_system_version(version)
    print(f"Controller (DRCF) version: {version._szController}")
    print(f"Library version: {robot.get_library_version()}")

    # Try to get control access (Fails after 10 attempts)
    for _ in range(10):
        if not get_control_access:
            robot.manage_access_control(drfl.MANAGE_ACCESS_CONTROL.Force_request)
            time.sleep(1.0)
            continue
        if not is_standby:
            robot.set_robot_control(drfl.ROBOT_CONTROL.Servo_on)
            time.sleep(2.0)
            continue
        break

    if not (get_control_access and is_standby):
        print("Failed setting intended states")
        raise SystemExit(1)

    # Set robot system (Virtual or Real)
    if VIRTUAL:
        if not robot.set_robot_system(drfl.ROBOT_SYSTEM.Virtual):
            raise SystemExit(1)
    else:
        if not robot.set_robot_system(drfl.ROBOT_SYSTEM.Real):
            raise SystemExit(1)

    # Set robot mode (Autonomous) This enables the robot to execute autonomous motion.
    if not robot.set_robot_mode(drfl.ROBOT_MODE.Autonomous):
        raise SystemExit(1)

    input("Press Enter to continue...")

    target_pos = np.array([0., 0., 30., 0., 0., 0.], dtype=np.float32)
    print(f"Moving to target position... [{target_pos}]")
    if not robot.movej(
        pos=target_pos,
        vel=SPEED,
        acc=ACCELERATION,
        time=0.0,
        move_mode=drfl.MOVE_MODE.Absolute,
        blending_radius=0.0,
        blending_type=drfl.BLENDING_SPEED_TYPE.Duplicate):
        print("Failed to execute movej command")
        raise SystemExit(1)

    if not is_move_done(MOVE_TIMEOUT): # Waits for the movement to be done
        print("Move timed out")
        raise SystemExit(1)

    print("Target position reached!")
    target_pos[2] = 0.

    print(f"Moving to target position... [{target_pos}]")
    if not robot.movej(
        pos=target_pos,
        vel=SPEED,
        acc=ACCELERATION,
        time=0.0,
        move_mode=drfl.MOVE_MODE.Absolute,
        blending_radius=0.0,
        blending_type=drfl.BLENDING_SPEED_TYPE.Duplicate):
        print("Failed to execute movej command")
        raise SystemExit(1)

    if not is_move_done(MOVE_TIMEOUT): #Waits for the movement to be done.
        print("Move timed out")
        raise SystemExit(1)

    print("Target position reached!")
    robot.close_connection()
    time.sleep(1.0) #Gives time to close the connection before exiting
    sys.exit(0)

if __name__ == "__main__":
    main()
