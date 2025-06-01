from machine import Pin, PWM
from config import *


IN1 = Pin(DOC_IN1, Pin.OUT)
IN2 = Pin(DOC_IN2, Pin.OUT)
IN3 = Pin(DOC_IN3, Pin.OUT)
IN4 = Pin(DOC_IN4, Pin.OUT)

PWM_PIN = Pin(PWM_IN)
pwm_pin = PWM(PWM_PIN, freq=1000)
pwm_pin.duty(0)

CURRENT_DUTY = 0

def pwm_control(target_duty, step=10, delay=5):
    global CURRENT_DUTY

    while CURRENT_DUTY != target_duty:
        if CURRENT_DUTY < target_duty:
            CURRENT_DUTY += step
        elif CURRENT_DUTY > target_duty:
            CURRENT_DUTY -= step

        CURRENT_DUTY = min(max(CURRENT_DUTY, 0), 1023)
        PWM_PIN.duty(CURRENT_DUTY)


def forward(intensity):
    IN1.value(1)
    IN2.value(0)
    IN3.value(1)
    IN4.value(0)
    pwm_control(int(1023 * intensity))




def backward(intensity):
    IN1.value(0)
    IN2.value(1)
    IN3.value(0)
    IN4.value(1)
    pwm_control(int(1023 * intensity))


def turn_right(intensity):
    IN1.value(0)
    IN2.value(1)
    IN3.value(1)
    IN4.value(0)
    pwm_control(int(1023 * intensity))


def turn_left(intensity):
    IN1.value(1)
    IN2.value(0)
    IN3.value(0)
    IN4.value(1)
    pwm_control(int(1023 * intensity))


def stop(intensity):
    pwm_control(0)
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
