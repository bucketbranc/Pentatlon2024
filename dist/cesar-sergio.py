import rcu

VAR_SET_BANDERA = 0

def task1():
  global VAR_SET_BANDERA
  VAR_SET_BANDERA = 0
  while True:
    if (VAR_SET_BANDERA == 0):
      ter_block()
      if (rcu.GetUltrasound(3) < 20):
        rcu.SetMotor(1,0)
        rcu.SetMotor(2,0)
        VAR_SET_BANDERA = 1
    if (VAR_SET_BANDERA == 1):
      Hakim_block()
      VAR_SET_BANDERA = 2
    if (VAR_SET_BANDERA == 2):
      Piqu_block()

def Hakim_block():
  global VAR_SET_BANDERA
  rcu.SetMotor(1,0)
  rcu.SetMotor(2,50)
  rcu.SetWaitForTime(0.75)
  rcu.SetMotor(1,50)
  rcu.SetMotor(2,50)
  rcu.SetWaitForTime(1.5)
  rcu.SetMotor(1,50)
  rcu.SetMotor(2,0)
  rcu.SetWaitForTime(0.75)
  rcu.SetMotor(1,50)
  rcu.SetMotor(2,50)
  rcu.SetWaitForTime(1.5)
  rcu.SetMotor(1,50)
  rcu.SetMotor(2,0)
  rcu.SetWaitForTime(0.75)
  rcu.SetMotor(1,50)
  rcu.SetMotor(2,50)
  rcu.SetWaitForTime(2)

def Piqu_block():
  global VAR_SET_BANDERA
  if ((rcu.GetLightSensor(1) > 2000) and (rcu.GetLightSensor(2) > 2000)):
    rcu.SetMotor(1,0)
    rcu.SetMotor(2,0)
  if ((rcu.GetLightSensor(1) < 2000) and (rcu.GetLightSensor(2) > 2000)):
    rcu.SetMotor(1,-30)
    rcu.SetMotor(2,30)
  if ((rcu.GetLightSensor(1) > 2000) and (rcu.GetLightSensor(2) < 2000)):
    rcu.SetMotor(1,30)
    rcu.SetMotor(2,-30)
  if ((rcu.GetLightSensor(1) < 2000) and (rcu.GetLightSensor(2) < 2000)):
    rcu.SetMotor(1,30)
    rcu.SetMotor(2,30)

def ter_block():
  global VAR_SET_BANDERA
  if ((rcu.GetLightSensor(1) > 2000) and (rcu.GetLightSensor(2) > 2000)):
    rcu.SetMotor(1,30)
    rcu.SetMotor(2,30)
  if ((rcu.GetLightSensor(1) < 2000) and (rcu.GetLightSensor(2) > 2000)):
    rcu.SetMotor(1,-30)
    rcu.SetMotor(2,30)
  if ((rcu.GetLightSensor(1) > 2000) and (rcu.GetLightSensor(2) < 2000)):
    rcu.SetMotor(1,30)
    rcu.SetMotor(2,-30)
  if ((rcu.GetLightSensor(1) < 2000) and (rcu.GetLightSensor(2) < 2000)):
    rcu.SetMotor(1,0)
    rcu.SetMotor(2,0)

task1()