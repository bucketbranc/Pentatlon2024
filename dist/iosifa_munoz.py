import rcu

VAR_bandera = 0

def lineablanca():
  global VAR_bandera
  if ((rcu.GetLightSensor(1) < 1800) and (rcu.GetLightSensor(2) < 1800)):
    rcu.SetMotor(1,40)
    rcu.SetMotor(2,40)
  if ((rcu.GetLightSensor(1) > 1800) and (rcu.GetLightSensor(2) < 1800)):
    rcu.SetMotor(1,-40)
    rcu.SetMotor(2,40)
  if ((rcu.GetLightSensor(1) > 1800) and (rcu.GetLightSensor(2) < 1800)):
    rcu.SetMotor(1,40)
    rcu.SetMotor(2,-40)
  if ((rcu.GetLightSensor(1) > 1800) and (rcu.GetLightSensor(2) > 1800)):
    rcu.SetMotor(1,0)
    rcu.SetMotor(2,0)

def task1():
  global VAR_bandera
  VAR_bandera = 0
  while True:
    if (VAR_bandera == 0):
      lineanegra()
    if (rcu.GetUltrasound(3) < 20):
      VAR_bandera = 1
    if (VAR_bandera == 1):
      empujar()
      VAR_bandera = 2
    if (VAR_bandera == 2):
      lineanegra()
      if (rcu.GetUltrasound(3) < 20):
        rcu.SetMotor(1,0)
        rcu.SetMotor(2,0)
        VAR_bandera = 3
    if (VAR_bandera == 3):
      esquivar()
      VAR_bandera = 4
    if (VAR_bandera == 4):
      lineablanca()
      if (rcu.GetUltrasound(3) < 20):
        rcu.SetMotor(1,0)
        rcu.SetMotor(2,0)
        VAR_bandera = 5
    if (VAR_bandera == 5):
      satelite()
      VAR_bandera = 6
    if (VAR_bandera == 6):
      lineablanca()

def lineanegra():
  global VAR_bandera
  if ((rcu.GetLightSensor(1) > 1800) and (rcu.GetLightSensor(2) > 1800)):
    rcu.SetMotor(1,40)
    rcu.SetMotor(2,40)
  if ((rcu.GetLightSensor(1) < 1800) and (rcu.GetLightSensor(2) > 1800)):
    rcu.SetMotor(1,-40)
    rcu.SetMotor(2,40)
  if ((rcu.GetLightSensor(1) > 1800) and (rcu.GetLightSensor(2) < 1800)):
    rcu.SetMotor(1,40)
    rcu.SetMotor(2,-40)
  if ((rcu.GetLightSensor(1) < 1800) and (rcu.GetLightSensor(2) < 1800)):
    rcu.SetMotor(1,0)
    rcu.SetMotor(2,0)

def esquivar():
  global VAR_bandera
  rcu.SetMotor(1,0)
  rcu.SetMotor(2,0)
  rcu.SetWaitForTime(0.5)
  rcu.SetMotor(1,50)
  rcu.SetMotor(2,0)
  rcu.SetWaitForTime(0.8)
  rcu.SetMotor(1,50)
  rcu.SetMotor(2,50)
  rcu.SetWaitForTime(1)
  rcu.SetMotor(1,0)
  rcu.SetMotor(2,50)
  rcu.SetWaitForTime(1.3)
  rcu.SetMotor(1,50)
  rcu.SetMotor(2,50)
  rcu.SetWaitForTime(2)
  rcu.SetMotor(1,0)
  rcu.SetMotor(2,50)
  rcu.SetWaitForTime(1.4)
  rcu.SetMotor(1,50)
  rcu.SetMotor(2,50)
  rcu.SetWaitForTime(1)

def empujar():
  global VAR_bandera
  rcu.SetMotor(1,0)
  rcu.SetMotor(2,0)
  rcu.SetWaitForTime(1)
  rcu.SetMotor(1,35)
  rcu.SetMotor(2,0)
  rcu.SetWaitForTime(1)

def satelite():
  global VAR_bandera
  pass

task1()