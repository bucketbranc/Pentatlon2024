from rcu import *
#Poodle-anotaciones :
'''

mejora el descaergador
Arregla el esquivar
Mover objeto
'''
# Constants
THRESHOLD = 2000
OBSTACLE_DISTANCE = 15

class argon:
     def setMotors(left_speed: int, right_speed: int, time: int = 0) -> None:
          SetMotor(1, left_speed)
          SetMotor(2, right_speed)
          SetWaitForTime(time)

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
          speed = 40
          '''
          
          if not GetColorSensor(5,4) == 5:
               speed = 30
          elif GetColorSensor(5,4) == 5:
               speed = 40
          '''
          if left > THRESHOLD and right > THRESHOLD:
               argon.setMotors(speed, speed)
          elif left < THRESHOLD < right:
               argon.setMotors(-100, 100)
          elif left > THRESHOLD > right:
               argon.setMotors(100, -100)

     def dark(left: int, right: int) -> None:
          if left < THRESHOLD and right < THRESHOLD:
               argon.setMotors(40, 40)
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
                        pass
               if left > THRESHOLD and right > THRESHOLD:
                    argon.setMotors(-50, 50)
                    on_line = True
                    SetWaitForTime(0.4)
               elif left > THRESHOLD > right:
                    argon.setMotors(-50, 50)
                    SetWaitForTime(0.4)
                    on_line = True
               elif left < THRESHOLD < right:
                    argon.setMotors(-50, 30)
                    SetWaitForTime(0.4)
                    on_line = True
          SetDisplayString(2, "1: Changing to Dark", 0xFFE0, 0x0000)
     def pushObject():
          argon.setMotors(0, 0, 1)
          argon.setMotors(0, 50, 1.2)
          argon.setMotors(50,50,0.3)
          argon.setMotors(50, 0, 1)
          argon.setMotors(50,50,0.4)
          argon.setMotors(50, 0, 0.8)
          argon.setMotors(50 ,50)
     def dodge() -> None:
          SetDisplayString(2, "1: Dodging", 0xFFE0, 0x0000)
          argon.setMotors(-50, 50)
          SetWaitForTime(0.7)
          argon.setMotors(50, 50)
          SetWaitForTime(1.5)
          argon.setMotors(50, 0)
          SetWaitForTime(0.85)
          argon.setMotors(50, 50)
          SetWaitForTime(3)
          argon.setMotors(50, 0)
          SetWaitForTime(0.85)
          argon.setMotors(50, 50)
          SetWaitForTime(0.7)
          SetDisplayString(2, "1: ", 0xFFE0, 0x0000)
          SetDisplayString(4, "2: ", 0xFFE0, 0x0000)
     def satelite() -> None:
          argon.setMotors(0, 0)
          SetWaitForTime(1)
          argon.setMotors(-50, 50) # giro inicial
          SetWaitForTime(0.6)
          argon.setMotors(50, 50) # avanzar para volver a girar
          SetWaitForTime(1.4)
          argon.setMotors(50, 0) # girar 2
          SetWaitForTime(0.8)
          argon.setMotors(50, 50) #avanzar para acoplarse
          SetWaitForTime(0.5)
          argon.setMotors(50, -25) # Acoplarse
          SetWaitForTime(0.9)
          argon.setMotors(50, 50)
          SetDisplayString(4, "3: Waiting Satelite", 0xFFE0, 0x0000)
          while not(GetTouch(6)):
               pass
          SetMotor(3, -100)
          SetDisplayString(4, "3: Satelite Found", 0xFFE0, 0x0000)
          argon.setMotors(0, 0)
          SetWaitForTime(3.2)
          SetMotor(3, 0)
          #regresar
          SetDisplayString(4, "3: ", 0xFFE0, 0x0000)
          argon.setMotors(-50, -50)
          SetWaitForTime(0.5)
          argon.setMotors(50, -50)
          SetWaitForTime(0.6)
          argon.setMotors(50, 50)
          SetWaitForTime(0.5)
          argon.setMotors(0, 0)
          SetWaitForTime(0.1)
def main() -> None:
    SetDisplayStringXY(40, 60, "PoodleBot", 0xFFFF, 0x0000, 1)
    SetDisplayStringXY(50, 60, "GPL Licence V3", 0xFFFF, 0x0000, 1)

    is_light_line = True
    setback = 0
    while True:
          if not argon.detectObstacle(50):
                argonPerformer.followLine(is_light_line)
          elif argon.detectObstacle(42) and setback == 0:
               SetDisplayString(4, "3: Object Detected", 0xFFE0, 0x0000)
               argonPerformer.pushObject()
               setback = True
          elif argon.detectObstacle(23) and setback:
               SetDisplayString(4, "3: Obstacle Detected", 0xFFE0, 0x0000)
               argon.setMotors(0, 0)
               SetWaitForTime(1)
               argonPerformer.dodge()
               argonPerformer.reintegrate()
               argonPerformer.followLine(is_light_line)
               setback=False
          elif argon.detectObstacle(15) and setback == False:
               SetDisplayString(4, "3: Satelite Detected", 0xFFE0, 0x0000)
               argonPerformer.satelite()
               argonPerformer.reintegrate()
               setback = 1

          if (argon.getLigthSensors()[0] < THRESHOLD and argon.getLigthSensors()[1] < THRESHOLD):
               SetDisplayString(1, "0: Changing to Dark", 0xFFE0, 0x0000)
               is_light_line = False
          elif (argon.getLigthSensors()[0] > THRESHOLD and argon.getLigthSensors()[1] > THRESHOLD):
               SetDisplayString(3, "2: Changing to Bright", 0xFFE0, 0x0000)
               is_light_line = True

main()