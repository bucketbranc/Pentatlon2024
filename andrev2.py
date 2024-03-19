# Welcome to the great code of Andre Segura B.
# Code for the pentatlon 2024 by Netica
# Code under MIT licence
import rcu

bandera = 0
VAR_umbral = 0

def task1():
  global VAR_umbral
  rcu.SetLCDClear(0xFFE0)
  VAR_umbral = 2000
  rcu.SetDisplayString(1,"MIT Licence Two",0xFFE0,0x0000)
  rcu.SetDisplayStringXY(100,20,"Poodle Robot X",0xF800,0x0000,1)
  if bandera == 0:
    rcu.SetDisplayString(1,"Bandera 0",0xFFE0,0x0000)
    while True:
      brigth(rcu.GetLightSensor(1),(50 == 50))
      brigth(rcu.GetLightSensor(2),(0 == 50))
      if (rcu.GetUltrasound(1) < 10):
        bandera = 1
        break
  if bandera == 1:
    rcu.SetDisplayString(1,"Bandera 1",0xFFE0,0x0000)
    rcu.SetMotor(1,0)
    rcu.SetMotor(2,0)

def brigth(ligth,direction):
  global VAR_umbral
  if (ligth > 2000):
    rcu.SetMotor(1,30)
    rcu.SetMotor(2,30)
  else:
    if (ligth < 2000):
      if direction:
        rcu.SetMotor(1,-100)
        rcu.SetMotor(2,100)
      else:
        rcu.SetMotor(1,100)
        rcu.SetMotor(2,-100)

task1()