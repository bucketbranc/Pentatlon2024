import rcu
from typing import Tuple

# Constants
THRESHOLD = 2000
OBSTACLE_DISTANCE = 15

# Helper functions
def set_motors(left_speed: int, right_speed: int) -> None:
    SetMotor(1, left_speed)
    SetMotor(2, right_speed)

def get_light_sensors() -> Tuple[int, int]:
    return GetLightSensor(1), GetLightSensor(2)

def is_obstacle_ahead() -> bool:
    return GetUltrasound(3) < OBSTACLE_DISTANCE

# Line following functions
def follow_line(is_light: bool) -> None:
    left, right = get_light_sensors()
    if is_light:
        follow_light_line(left, right)
    else:
        follow_dark_line(left, right)

def follow_light_line(left: int, right: int) -> None:
    if left > THRESHOLD and right > THRESHOLD:
        set_motors(35, 35)
    elif left < THRESHOLD <= right:
        set_motors(-100, 100)
    elif left >= THRESHOLD > right:
        set_motors(100, -100)

def follow_dark_line(left: int, right: int) -> None:
    if left < THRESHOLD and right < THRESHOLD:
        set_motors(35, 35)
    elif left >= THRESHOLD > right:
        set_motors(-100, 100)
    elif left < THRESHOLD <= right:
        set_motors(100, -100)

def reintegrate_line() -> None:
    SetDisplayString(2, "1: Reintegrating", 0xFFE0, 0x0000)
    on_line = False
    while not on_line:
        left, right = get_light_sensors()
        if left < THRESHOLD and right < THRESHOLD:
            set_motors(35, 35)
        elif left >= THRESHOLD > right:
            set_motors(100, -100)
            on_line = True
        elif left < THRESHOLD <= right:
            set_motors(-100, 100)
            on_line = True
    SetDisplayString(2, "1: Changing to Dark", 0xFFE0, 0x0000)

def dodge_obstacle() -> None:
    SetDisplayString(2, "1: Dodging", 0xFFE0, 0x0000)
    set_motors(-100, 50)
    SetWaitForTime(0.6)
    set_motors(50, 50)
    SetWaitForTime(1.5)
    set_motors(50, -90)
    SetWaitForTime(0.6)
    set_motors(50, 50)
    SetWaitForTime(2)
    set_motors(50, -50)
    SetWaitForTime(0.7)
    set_motors(50, 50)
    SetWaitForTime(0.5)
    SetDisplayString(2, "1: ", 0xFFE0, 0x0000)

def main() -> None:
    SetDisplayStringXY(4, 10, "PoodleBot", 0xFFFF, 0x0000, 1)
    SetDisplayStringXY(4, 10, "GPL Licence V3", 0x0000, 0xFFFF, 1)
    rcu.SetDisplayPicture(20, 10, "a.jpg", 2)

    is_light_line = True
    while True:
        if is_obstacle_ahead():
            SetDisplayString(4, "2: Stoping", 0xFFE0, 0x0000)
            set_motors(0, 0)
            dodge_obstacle()
            reintegrate_line()
        else:ñ
            follow_line(is_light_line)

        if (get_light_sensors()[0] < THRESHOLD and get_light_sensors()[1] < THRESHOLD):
            SetDisplayString(1, "0: Changing to Dark", 0xFFE0, 0x0000)
            is_light_line = False
        elif (get_light_sensors()[0] > THRESHOLD and get_light_sensors()[1] > THRESHOLD):
            SetDisplayString(3, "2:Changing to Bright", 0xFFE0, 0x0000)
            is_light_line = True

if __name__ == "__main__":
    main()