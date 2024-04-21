# Rastreador
> por Andre Segura, Santiago garcia

## 1. Seguir la linea negra
El principio para seguir una linea es muy basico.

1. **Configuración del Robot**:
     - Use una plataforma de robot de dos ruedas con un microcontrolador (E6-RCU) y los componentes necesarios.
    - Instale dos motores (uno para cada rueda).
    - Agrege dos sensores de luz a los lados del robot

## 2. Esquivar la caja
Para hacer el robot esquivar la caja, hay que seguir estos pasos generales:

1. **Configuración de hardware**:
    - Use una plataforma de robot de dos ruedas con un microcontrolador (E6-RCU) y los componentes necesarios.
    - Instale dos motores (uno para cada rueda).
    - Agregue un sensor ultrasónico para detectar obstáculos frente al robot.
    - Inetgre un sensor de color() para poder identificar la linea
    - Instale un motor dadasd

2. **Detección de obstáculos**:
    - Use el sensor ultrasónico para medir la distancia al obstáculo (en este caso, la caja).
    - Establezca un valor de distancia umbral en el que el robot debe comenzar a esquivar el obstáculo.

    Introduzca una funcion dentro del ciclo para checar si hay un obstaculo al frente
    ```py
    def detectar_obstaculo(distancia) -> bool:
        return GetUltrasound(3) < distancia
    ```
3. **Dodificación de algoritmo**:
    - Cuando la distancia medida es menor que el umbral, inicie la rutina de esquivación.
    - La rutina de esquivar puede involucrar los siguientes pasos:
      a. Detén ambas ruedas para un breve momento.
      b. Gire una rueda en la dirección opuesta (por ejemplo, la rueda izquierda hacia atrás y la rueda derecha hacia adelante) durante una corta duración para que el robot gire.
      C. Una vez girado, mueva ambas ruedas hacia adelante para una distancia o tiempo específico para evitar el obstáculo.
      d. Gire las ruedas en la dirección opuesta nuevamente para enderezar el camino del robot.
      mi. Reanude el movimiento normal.

4. **Control del motor**:
    - Use el controlador del motor y el microcontrolador para controlar la velocidad y la dirección de cada motor de forma independiente.
    - Ajuste la velocidad y la duración de la rotación en función del tamaño del robot y el radio de giro deseado.

5. **Monitoreo continuo**:
    - Controle continuamente las lecturas del sensor ultrasónico mientras el robot se mueve.
    - Si se detecta otro obstáculo, repita la rutina de esquivar.

Aquí hay un ejemplo básico para la rutina de esquivar:

```py
        # Girar 90° a la izquierda en 0.6 segundos ⬏
        SetMotor(1,-100)#
        SetMotor(2,50) 
        SetWaitForTime(0.6)
        # Avanzar 10cm(aprox) con los dos motores a 50% por 1.5 segundos para ⬏↑ 
        SetMotor(1,50)
        SetMotor(2,50)
        SetWaitForTime(1.5)
        # Girar 90° a la derecha en 0.6 segundos ⬏↑↱
        SetMotor(1,50)
        SetMotor(2,-90)
        SetWaitForTime(0.6)
        # Avanzar 60cm(aprox) con los dos motores a 50% por 2 segundos segundos ⬏↑↱→
        SetMotor(2,50)
        SetWaitForTime(2)
        # Girar 90° a la derecha en 0.7 segundos para retomar la linea negra ⬏↑↱→⤵
        SetMotor(1,50)
        SetMotor(2,-50)
        SetWaitForTime(0.7)
        # Avanzar hasta encontrar la linea ⬏↑↱→⤵🡓
        SetMotor(1,50)
        SetMotor(2,50)
        SetWaitForTime(0.5)
        '''
         ↱→→→→⤵
         ↑    🡓
        ⬏
```

Este es un esquema básico, y deberá ajustar los valores y duraciones en función de las dimensiones, la velocidad y las características del sensor de su robot específico. Además, es posible que desee agregar manejo de errores, ajuste fino y características adicionales como algoritmos de evitación de obstáculos o capacidades de siguientes a la línea.
