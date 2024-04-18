from rcu import *

VAR_umbral = 0
bandera = 0


def task1():
    global VAR_umbral, bandera
    bandera = 0
    while True:
        if bandera == 0:
            if (GetLightSensor(1) < 2000) and (GetLightSensor(2) < 2000):
                SetDisplayString(1, "0: Changing to Dark", 0xFFE0, 0x0000)
                SetMotor(1, 0)
                SetMotor(2, 0)
                bandera = 2
            performer.detectObject()
            performer.brigth(GetLightSensor(1), GetLightSensor(2))
        # Sensor Ultrasonico
        if bandera == 1:
            SetDisplayString(2, "1: Stopped", 0xFFE0, 0x0000)
            SetMotor(1, 0)
            SetMotor(2, 0)
            performer.dodge()
            bandera = 2
            if not ((GetUltrasound(3) < 30)):
                SetDisplayString(2, "1: Resuming", 0xFFE0, 0x0000)
                bandera = 0
        #oscuro
        if bandera == 2:
            if (GetLightSensor(1) > 2000) and (GetLightSensor(2) > 2000):
                SetDisplayString(3, "2:Changing to Brigth", 0xFFE0, 0x0000)
                SetMotor(1, 0)
                SetMotor(2, 0)
                bandera = 0
            performer.detectObject()
            performer.dark(GetLightSensor(1), GetLightSensor(2))


class performer:
    def brigth(Left, Rigth):
        global VAR_umbral, bandera
        VAR_umbral = 2000
        if (Left > VAR_umbral) and (Rigth > VAR_umbral):
            SetMotor(1, 35)
            SetMotor(2, 35)
        # Left Touches Black && Rigth Detects White
        #  - Both Motors Go Forward -
        if (Left < VAR_umbral) and (Rigth > VAR_umbral):
            SetMotor(1, -100)
            SetMotor(2, 100)
        # Left detects white a && Rigth Touches black
        # - M1 go 50 M2 go -50 -
        if (Left > VAR_umbral) and (Rigth < VAR_umbral):
            SetMotor(1, 100)
            SetMotor(2, -100)

    def dark(Left, Rigth):
        global VAR_umbral, bandera
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
        global VAR_umbral, bandera
        VAR_umbral = 2000
        out = True
        line=False
        SetDisplayString(2, "1: Reintegrating", 0xFFE0, 0x0000)
        while out:
            if (Left < VAR_umbral) and (Rigth < VAR_umbral):
                SetMotor(1, 35)
                SetMotor(2, 35)
                if (line):
                    bandera = 2
                    out=False
                    break
            # Left Touches Black && Rigth Detects White
            #  - Both Motors Go Forward -
            if (Left > VAR_umbral) and (Rigth < VAR_umbral):
                SetMotor(1, -100)
                SetMotor(2, 100)
                line=True
                # Left detects white a && Rigth Touches black
                # - M1 go 50 M2 go -50 -
            if (Left < VAR_umbral) and (Rigth > VAR_umbral):
                SetMotor(1, 100)
                SetMotor(2, -100)
                line=True
        SetDisplayString(2, "1: Changing to Dark", 0xFFE0, 0x0000)

    def dodge():
        SetDisplayString(2, "1: Dodging", 0xFFE0, 0x0000)
        SetMotor(1,-100)
        SetMotor(2,50)
        SetWaitForTime(0.6)
        SetMotor(1,50)
        SetMotor(2,50)
        SetWaitForTime(1.5)
        SetMotor(1,50)
        SetMotor(2,-90)
        SetWaitForTime(0.6)
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
        global VAR_umbral, bandera
        if GetUltrasound(3) < 15:
            SetDisplayString(4, "2: Stoping", 0xFFE0, 0x0000)
            SetMotor(1, 0)
            SetMotor(2, 0)
            bandera = 1


task1()
