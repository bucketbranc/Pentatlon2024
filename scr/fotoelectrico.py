from rcu import *

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
while True:
     left = GetColorSensor(1,4)
     right = GetColorSensor(2,4)
     if left == 6 and right == 6 :
               argon.setMotors(40, 40)
     elif left == 5 and right == 6:
               argon.setMotors(-100, 100)
     elif left == 6 and right == 5:
               argon.setMotors(100, -100)