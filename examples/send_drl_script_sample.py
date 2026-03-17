#!/usr/bin/env python3

import sys
import time

import doosan_drfl as drfl
import numpy as np

IP_ADDRESS = "127.0.0.1"
PORT = 12345

SPEED = 5.0 # deg/s
ACCELERATION = 5.0 # deg/s^2

VIRTUAL = False # Will set the movement to be virutal (simulated)

robot = drfl.CDRFLEx()

get_control_access = False
is_standby = False

STRINGDRL: str = str("\r\nloop = 0\r\nwhile loop < 5:\r\n movej(posj(0,0,90,0,90,0), vel=60, acc=60)\r\n movej(posj(0,0,80,0,90,0), vel=60, acc=60)\r\n loop+=1\r\n")

def on_monitoring_access_control(access: drfl.MONITORING_ACCESS_CONTROL) -> None:
    global get_control_access
    access_in_stirng = drfl.MONITORING_ACCESS_CONTROL(access).name
    print(f"[on_monitor_access_control] access: {access_in_stirng} [{access}]")
    if access == drfl.MONITORING_ACCESS_CONTROL.Grant:
        get_control_access = True
    elif access == drfl.MONITORING_ACCESS_CONTROL.Loss:
        get_control_access = False

def on_monitoring_state(state: drfl.ROBOT_STATE) -> None:
    global is_standby
    state_in_string = drfl.ROBOT_STATE(state).name
    print(f"[on_monitoring_state] state: {state_in_string} [{state}]")
    if state == drfl.ROBOT_STATE.Standby:
        is_standby = True
        print("Succesfully Servo on!!")
    else:
        is_standby = False


def main():
    robot.set_on_monitoring_access_control(on_monitoring_access_control)
    robot.set_on_monitoring_state(on_monitoring_state)


    ret = robot.open_connection(IP_ADDRESS, port=PORT)

    print(f"Open_connection return value: {ret}")
    if not ret:
        print(f"Cannot open connection to robot @ {IP_ADDRESS}:{PORT}")
        raise SystemError(1)

    robot.setup_monitoring_version(1)

    version = drfl.SYSTEM_VERSION()
    robot.get_system_version(version)
    print(f"Controller (DRCF) version: {version._szController}")
    print(f"Library version: {robot.get_library_version()}")

    # Try to get control acces (Fails after 10 attempts)
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
        print("Failed to get control access and/or robot is not in standby state")
        raise SystemError(1)

    # Set robot system (Virtual or Real)
    if VIRTUAL:
        if not robot.set_robot_system(drfl.ROBOT_SYSTEM.Virtual):
            print("Failed to set robot system to virtual")
            raise SystemError(1)
    else:
        if not robot.set_robot_system(drfl.ROBOT_SYSTEM.Real):
            print("Failed to set robot system to real")
            raise SystemError(1)

    # Set robot mode (Autonomous) This enables the robot to execute autonomous motion.
    if not robot.set_robot_mode(drfl.ROBOT_MODE.Autonomous):
        print("Failed to set robot mode to autonomous")
        raise SystemError(1)

    input("Press Enter to continue...")

    robot.drl_start(drfl.ROBOT_SYSTEM.Real, STRINGDRL)

    input("Press Enter to pause ...")

    robot.drl_pause()

    input("Press Enter to resume ...")

    robot.drl_resume()

    input("Press Enter to stop ...")

    robot.drl_stop()

    time.sleep(4.0)

    robot.close_connection()

    sys.exit(0)





if __name__ == "__main__":
    main()
