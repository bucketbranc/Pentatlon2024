import rcu

VAR_umbral = 0
VAR_bandera = 0


def task1():
    global VAR_umbral, VAR_bandera
    VAR_bandera = 0
    while True:
        if VAR_bandera == 0:
            if (rcu.GetLightSensor(1) < 2000) and (rcu.GetLightSensor(2) < 2000):
                rcu.SetDisplayString(1, "0: Changing to Dark", 0xFFE0, 0x0000)
                rcu.SetMotor(1, 0)
                rcu.SetMotor(2, 0)
                VAR_bandera = 2
            performer.detectObject()
            performer.brigth(rcu.GetLightSensor(1), rcu.GetLightSensor(2))
        # Sensor Ultrasonico
        if VAR_bandera == 1:
            rcu.SetDisplayString(2, "1: Stopped", 0xFFE0, 0x0000)
            rcu.SetMotor(1, 0)
            rcu.SetMotor(2, 0)
            if not ((rcu.GetUltrasound(3) < 30)):
                rcu.SetDisplayString(2, "1: Resuming", 0xFFE0, 0x0000)
                VAR_bandera = 0
        if VAR_bandera == 2:
            if (rcu.GetLightSensor(1) > 2000) and (rcu.GetLightSensor(2) > 2000):
                rcu.SetDisplayString(3, "2:Changing to Brigth", 0xFFE0, 0x0000)
                rcu.SetMotor(1, 0)
                rcu.SetMotor(2, 0)
                VAR_bandera = 0
            performer.detectObject()
            performer.dark(rcu.GetLightSensor(1), rcu.GetLightSensor(2))


class performer:
    def brigth(Left, Rigth):
        global VAR_umbral, VAR_bandera
        VAR_umbral = 2000
        if (Left > VAR_umbral) and (Rigth > VAR_umbral):
            rcu.SetMotor(1, 35)
            rcu.SetMotor(2, 35)
        # Left Touches Black && Rigth Detects White
        #  - Both Motors Go Forward -
        if (Left < VAR_umbral) and (Rigth > VAR_umbral):
            rcu.SetMotor(1, -50)
            rcu.SetMotor(2, 50)
        # Left detects white a && Rigth Touches black
        # - M1 go 50 M2 go -50 -
        if (Left > VAR_umbral) and (Rigth < VAR_umbral):
            rcu.SetMotor(1, 50)
            rcu.SetMotor(2, -50)

    def dark(Left, Rigth):
        global VAR_umbral, VAR_bandera
        VAR_umbral = 2000
        if (Left < VAR_umbral) and (Rigth < VAR_umbral):
            rcu.SetMotor(1, 35)
            rcu.SetMotor(2, 35)
        # Left Touches Black && Rigth Detects White
        #  - Both Motors Go Forward -
        if (Left > VAR_umbral) and (Rigth < VAR_umbral):
            rcu.SetMotor(1, -50)
            rcu.SetMotor(2, 50)
        # Left detects white a && Rigth Touches black
        # - M1 go 50 M2 go -50 -
        if (Left < VAR_umbral) and (Rigth > VAR_umbral):
            rcu.SetMotor(1, 50)
            rcu.SetMotor(2, -50)

    def dodge():
        global VAR_umbral, VAR_bandera
        rcu.SetMotor(2, 50)
        rcu.SetWaitForTime(3)
        rcu.SetMotor(1, 50)
        rcu.SetMotor(2, 50)
        rcu.SetWaitForTime(2)
        rcu.SetMotor(1, 50)
        rcu.SetWaitForTime(3)
        rcu.SetMotor(1, 50)
        rcu.SetMotor(2, 50)
        rcu.SetWaitForTime(3)
        rcu.SetMotor(1, 50)
        rcu.SetWaitForTime(3)
        rcu.SetMotor(1, 50)
        rcu.SetMotor(2, 50)
        rcu.SetWaitForTime(2)
        rcu.SetMotor(2, 50)
        rcu.SetWaitForTime(3)

    def detectObject():
        global VAR_umbral, VAR_bandera
        if rcu.GetUltrasound(3) < 30:
            rcu.SetDisplayString(4, "2: Stoping", 0xFFE0, 0x0000)
            rcu.SetMotor(1, 0)
            rcu.SetMotor(2, 0)
            VAR_bandera = 1


task1()
