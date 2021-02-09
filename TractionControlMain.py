# Basic Traction Control codes
import numpy as np
 
 #Variables
wheel_radius = 0.2032 #meters
wheel_speed_rpm = 180
vehicle_speed = 2 #meter/second
torque_motor = 50 #newton/meters
driving = True
 
#If wheel speed = revolutions per revolutions per minute
c = 2 * np.pi * wheel_radius #Circumfrence of Wheel in meters
wheel_speed_ms = (wheel_speed_rpm * c) / 60 #Gives wheel speed in m/s 
print("wheel speed = ", wheel_speed_ms)


def is_slipping(wheel_speed_ms, vehicle_speed):
    if vehicle_speed < wheel_speed_ms:
        return True
    else:
        return False
    



while driving:
  slipping = is_slipping(wheel_speed_ms, vehicle_speed)
    if slipping and wheel_speed_ms > 0:
        torque_motor_new = torque_motor
        torque_motor_new -= torque_motor * (vehicle_speed / wheel_speed_ms)
        torque_motor = torque_motor_new
        print("new motor torque =", torque_motor_new)
