from rcu import *

VAR_umbral = 0
VAR_bandera = 0


def task1():
    global VAR_umbral, VAR_bandera
    VAR_bandera = 0
    while True:
        if VAR_bandera == 0:
            if (GetLightSensor(1) < 2000) and (GetLightSensor(2) < 2000):
                SetDisplayString(1, "0: Changing to Dark", 0xFFE0, 0x0000)
                SetMotor(1, 0)
                SetMotor(2, 0)
                VAR_bandera = 2
            performer.detectObject()
            performer.brigth(GetLightSensor(1), GetLightSensor(2))
        # Sensor Ultrasonico
        if VAR_bandera == 1:
            SetDisplayString(2, "1: Stopped", 0xFFE0, 0x0000)
            SetMotor(1, 0)
            SetMotor(2, 0)
            performer.dodge()
            performer.reintegrate(GetLightSensor(1), GetLightSensor(2))
            if not ((GetUltrasound(3) < 30)):
                SetDisplayString(2, "1: Resuming", 0xFFE0, 0x0000)
                VAR_bandera = 0
        if VAR_bandera == 2:
            if (GetLightSensor(1) > 2000) and (GetLightSensor(2) > 2000):
                SetDisplayString(3, "2:Changing to Brigth", 0xFFE0, 0x0000)
                SetMotor(1, 0)
                SetMotor(2, 0)
                VAR_bandera = 0
            performer.detectObject()
            performer.dark(GetLightSensor(1), GetLightSensor(2))


class performer:
    def brigth(Left, Rigth):
        global VAR_umbral, VAR_bandera
        VAR_umbral = 2000
        if (Left > VAR_umbral) and (Rigth > VAR_umbral):
            SetMotor(1, 35)
            SetMotor(2, 35)
        # Left Touches Black && Rigth Detects White
        #  - Both Motors Go Forward -
        if (Left < VAR_umbral) and (Rigth > VAR_umbral):
            SetMotor(1, -50)
            SetMotor(2, 50)
        # Left detects white a && Rigth Touches black
        # - M1 go 50 M2 go -50 -
        if (Left > VAR_umbral) and (Rigth < VAR_umbral):
            SetMotor(1, 50)
            SetMotor(2, -50)

    def dark(Left, Rigth):
        global VAR_umbral, VAR_bandera
        VAR_umbral = 2000
        if (Left < VAR_umbral) and (Rigth < VAR_umbral):
            SetMotor(1, 35)
            SetMotor(2, 35)
        # Left Touches Black && Rigth Detects White
        #  - Both Motors Go Forward -
        if (Left > VAR_umbral) and (Rigth < VAR_umbral):
            SetMotor(1, -100)
            SetMotor(2, 100)
        # Left detects white a && Rigth Touches black
        # - M1 go 50 M2 go -50 -
        if (Left < VAR_umbral) and (Rigth > VAR_umbral):
            SetMotor(1, 100)
            SetMotor(2, -100)

    def reintegrate(Left, Rigth):
        global VAR_umbral, VAR_bandera
        VAR_umbral = 2000
        SetDisplayString(2, "1: Resuming", 0xFFE0, 0x0000)
        while True:
        
            if (Left < VAR_umbral) and (Rigth < VAR_umbral):
                SetMotor(1, 35)
                SetMotor(2, 35)
                SetWaitForTime(0.2)
                break
            if (Left > VAR_umbral):
                SetMotor(1, -100)
                SetMotor(2, 100)
                SetWaitForTime(0.2)
                break
            if (Rigth > VAR_umbral):
                SetMotor(1, 100)
                SetMotor(2, -100)
                SetWaitForTime(0.2)
                break
            if (Rigth > VAR_umbral) and (Left > VAR_umbral):
                SetMotor(1, 100)
                SetMotor(2, -100)
                SetWaitForTime(0.2)
                break

    def dodge():
        SetDisplayString(2, "1: Dodging", 0xFFE0, 0x0000)
        SetMotor(1,-100)
        SetMotor(2,50)
        SetWaitForTime(0.5)
        SetMotor(1,50)
        SetMotor(2,50)
        SetWaitForTime(2)
        SetMotor(1,50)
        SetMotor(2,-50)
        SetWaitForTime(0.5)
        SetMotor(1,50)
        SetMotor(2,50)
        SetWaitForTime(2)
        SetMotor(1,50)
        SetMotor(2,-50)
        SetWaitForTime(0.7)
        SetMotor(1,50)
        SetMotor(2,50)
        SetWaitForTime(0.5)
        SetDisplayString(2, "1: ", 0xFFE0, 0x0000)

    def detectObject():
        global VAR_umbral, VAR_bandera
        if GetUltrasound(3) < 20:
            SetDisplayString(4, "2: Stoping", 0xFFE0, 0x0000)
            SetMotor(1, 0)
            SetMotor(2, 0)
            VAR_bandera = 1


task1()
