from machine import Pin, PWM


IN1 = Pin(12, Pin.OUT)
IN2 = Pin(13, Pin.OUT)
IN3 = Pin(14, Pin.OUT)
IN4 = Pin(15, Pin.OUT)

PWM_PIN = PWM(Pin(14), freq=1000)
PWM_PIN.duty(512)  # 50% speed


def forward():
    IN1.value(1)
    IN2.value(0)
    IN3.value(1)
    IN4.value(0)


def backward():
    IN1.value(0)
    IN2.value(1)
    IN3.value(0)
    IN4.value(1)


def turn_right():
    IN1.value(0)
    IN2.value(1)
    IN3.value(1)
    IN4.value(0)


def turn_left():
    IN1.value(1)
    IN2.value(0)
    IN3.value(0)
    IN4.value(1)


def stop():
    IN1.value(0)
    IN2.value(0)
    IN3.value(0)
    IN4.value(0)


command_mapper = {
    "FORWARD": forward,
    "BACKWARD": backward,
    "RIGHT": turn_right,
    "LEFT": turn_left,
    "STOP": stop
}
