from rcu import *

# Constants
THRESHOLD = 2000
OBSTACLE_DISTANCE = 15

class argon:
     def setMotors(left_speed: int, right_speed: int) -> None:
          SetMotor(1, left_speed)
          SetMotor(2, right_speed)

     def getLigthSensors():
          """
          Returns the values of the two light sensors.

          :return: A tuple containing the values of the two light sensors.
          """
          return GetLightSensor(1), GetLightSensor(2)

     def detectObstacle(distance):
          return GetUltrasound(3) < distance

class argonPerformer:
     
     def followLine(is_light: bool) -> None:
          left, right = argon.getLigthSensors()
          if is_light:
               argonPerformer.light(left, right)
          else:
               argonPerformer.dark(left, right)

     def light(left: int, right: int) -> None:
          if left > THRESHOLD and right > THRESHOLD:
               argon.setMotors(35, 35)
          elif left < THRESHOLD < right:
               argon.setMotors(-100, 100)
          elif left > THRESHOLD > right:
               argon.setMotors(100, -100)

     def dark(left: int, right: int) -> None:
          if left < THRESHOLD and right < THRESHOLD:
               argon.setMotors(35, 35)
          elif left > THRESHOLD > right:
               argon.setMotors(-100, 100)
          elif left < THRESHOLD < right:
               argon.setMotors(100, -100)

     def reintegrate() -> None:
          SetDisplayString(2, "1: Reintegrating", 0xFFE0, 0x0000)
          on_line = False
          while not on_line:
               left, right = argon.getLigthSensors()
               if left < THRESHOLD and right < THRESHOLD:
                    argon.setMotors(35, 35)
                    if on_line:
                        break
               elif left > THRESHOLD > right:
                    argon.setMotors(-50, 50)
                    SetWaitForTime(0.5)
                    on_line = True
               elif left < THRESHOLD < right:
                    argon.setMotors(-50, -50)
                    SetWaitForTime(0.5)
                    on_line = True
          SetDisplayString(2, "1: Changing to Dark", 0xFFE0, 0x0000)

     def dodge() -> None:
          SetDisplayString(2, "1: Dodging", 0xFFE0, 0x0000)
          argon.setMotors(-50, 50)
          SetWaitForTime(0.7)
          argon.setMotors(50, 50)
          SetWaitForTime(1.5)
          argon.setMotors(50, 0)
          SetWaitForTime(0.75)
          argon.setMotors(50, 50)
          SetWaitForTime(3)
          argon.setMotors(50, 0)
          SetWaitForTime(0.85)
          argon.setMotors(50, 50)
          SetWaitForTime(0.7)
          SetDisplayString(2, "1: ", 0xFFE0, 0x0000)
          SetDisplayString(4, "2: ", 0xFFE0, 0x0000)

def main() -> None:
    SetDisplayStringXY(10, 10, "PoodleBot", 0xFFFF, 0x0000, 1)
    SetDisplayStringXY(20, 10, "GPL Licence V3", 0x0000, 0xFFFF, 1)

    is_light_line = True
    setback = False
    while True:
          if argon.detectObstacle(20) and setback:
               SetDisplayString(4, "2: Obstacle Detected", 0xFFE0, 0x0000)
               argon.setMotors(0, 0)
               SetWaitForTime(1)
               argonPerformer.dodge()
               argonPerformer.reintegrate()
               argonPerformer.followLine(is_light_line)
               setback=False
          elif argon.detectObstacle(15) and not setback:
               SetDisplayString(4, "2: Satelite Detected", 0xFFE0, 0x0000)
               argon.setMotors(0, 0)
               SetWaitForTime(1)
               argon.setMotors(-50, 50)
               SetWaitForTime(0.7)
               argon.setMotors(50, 50)
               SetWaitForTime(1)
               argon.setMotors(50, -50)
               SetWaitForTime(0.7)
               SetMotor(3, 100)
          else:
                argonPerformer.followLine(is_light_line)

          if (argon.getLigthSensors()[0] < THRESHOLD and argon.getLigthSensors()[1] < THRESHOLD):
               SetDisplayString(1, "0: Changing to Dark", 0xFFE0, 0x0000)
               is_light_line = False
          elif (argon.getLigthSensors()[0] > THRESHOLD and argon.getLigthSensors()[1] > THRESHOLD):
               SetDisplayString(3, "2: Changing to Bright", 0xFFE0, 0x0000)
               is_light_line = True

main()