# Welcome to the great code of Andre Segura B.
# Code for the pentatlon 2024 by Netica
# Code under MIT licence
import rcu

umbral = 2000
# sensor = ["Andre", 0, 0] # inutil, no comprendo su funcion

def inicio():
    while True:
        #sensor[1] = GetLightSensor(1)
        #sensor[2] = GetLightSensor(4)
        control(GetLightSensor(1),True)
        control(GetLightSensor(4),False)




def control(ligth,direccion): # Controlador principal para los motores

    if ligth > 2000 : # ehhh, blanco
        SetMotor(1,-40)
        SetMotor(2,40)
    elif ligth < 2000 : # Negro! yay!
            if direccion :
                SetMotor(1,50)
                SetMotor(2,50)
            else :
                SetMotor(1,-50)
                SetMotor(2,-50)

inicio()