from machine import Pin, PWM
from config import *


IN1 = Pin(DOC_IN1, Pin.OUT)
IN2 = Pin(DOC_IN2, Pin.OUT)
IN3 = Pin(DOC_IN3, Pin.OUT)
IN4 = Pin(DOC_IN4, Pin.OUT)

PWM_PIN = Pin(PWM_IN)
pwm_pin = PWM(PWM_PIN, freq=1000)
pwm_pin.duty(512)  # 50% speed


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
