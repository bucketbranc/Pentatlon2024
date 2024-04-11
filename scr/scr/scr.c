#define _TASK_1_ 1
#include <GetLightSensor.h>
#include <SetDisplayString.h>
#include <SetMotor.h>
#include <GetUltrasound.h>
#include <SetWaitForTime.h>

volatile double VAR_umbral = 0;
volatile double bandera = 0;

void task1(void);
void brigth(double Left,double Rigth);
void dark(double Left,double Rigth);
void dodge();

void task1(void)
{
    bandera = 0;
    for(;;){
        if (bandera == 0){
            if ((GetLightSensor(1) < 2000) && (GetLightSensor(2) < 2000)){
                SetDisplayString(1,"0: Changing to Dark",0xFFE0,0x0000);
                SetMotor(1,0);
                SetMotor(2,0);
                bandera = 2;
            }
            if (GetUltrasound(3) < 20){
                SetDisplayString(1,"0: Stoping",0xFFE0,0x0000);
                SetMotor(1,0);
                SetMotor(2,0);
                bandera = 1;
            }
            brigth(GetLightSensor(1),GetLightSensor(2));
        }
        if (bandera == 1){
            if (GetUltrasound(3) > 20){
                SetDisplayString(1,"1: Starting Over",0xFFE0,0x0000);
                bandera = 0;
            } else {
                SetDisplayString(1,"1: Dodging",0xFFE0,0x0000);
                SetMotor(1,0);
                SetMotor(2,0);
                dodge();
            }
        }
        if (bandera == 2){
            if ((GetLightSensor(1) > 2000) && (GetLightSensor(2) > 2000)){
                SetDisplayString(3,"2:Changing to Brigth",0xFFE0,0x0000);
                SetMotor(1,0);
                SetMotor(2,0);
                bandera = 0;
            }
            if (GetUltrasound(3) < 10){
                SetDisplayString(4,"2: Stoping",0xFFE0,0x0000);
                SetMotor(1,0);
                SetMotor(2,0);
                bandera = 1;
            }
            dark(GetLightSensor(1),GetLightSensor(2));
        }
    }
}

void brigth(double Left,double Rigth)
{
    VAR_umbral = 2000;
    if ((Left > VAR_umbral) && (Rigth > VAR_umbral)){
        SetMotor(1,50);
        SetMotor(2,50);
    }
    if ((Left < VAR_umbral) && (Rigth > VAR_umbral)){
        SetMotor(1,-50);
        SetMotor(2,50);
    }
    if ((Left > VAR_umbral) && (Rigth < VAR_umbral)){
        SetMotor(1,50);
        SetMotor(2,-50);
    }
}

void dark(double Left,double Rigth)
{
    VAR_umbral = 2000;
    if ((Left < VAR_umbral) && (Rigth < VAR_umbral)){
        SetMotor(1,50);
        SetMotor(2,50);
    }
    if ((Left > VAR_umbral) && (Rigth < VAR_umbral)){
        SetMotor(1,-50);
        SetMotor(2,50);
    }
    if ((Left < VAR_umbral) && (Rigth > VAR_umbral)){
        SetMotor(1,50);
        SetMotor(2,-50);
    }
}

void dodge()
{
    SetDisplayString(5,"5: Dodge",0xFFE0,0x0000);
/*    SetMotor(2,50);
    SetWaitForTime((3));
    SetMotor(1,50);
    SetMotor(2,50);
    SetWaitForTime((2));
    SetMotor(1,50);
    SetWaitForTime((3));
    SetMotor(1,50);
    SetMotor(2,50);
    SetWaitForTime((3));
    SetMotor(1,50);
    SetWaitForTime((3));
    SetMotor(1,50);
    SetMotor(2,50);
    SetWaitForTime((2));
    SetMotor(2,50);
    SetWaitForTime((3));*/
}