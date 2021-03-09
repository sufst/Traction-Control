import numpy as np

p1 = 10.5
p2 = 34.60
wheel_radius_m = 10 * 2.54 / 2
driving == True

lamda_p = p2 ** -0.5



def calculate_wheel_speed(vx_mps, lamda_p, wheel_radius_m, case):
    if case == "brake":
        wheel_angular_velocity_radps = (1 - lamda_p) * vx_mps / wheel_radius_m
    elif case == "accel":
        wheel_angular_velocity_radps = (lamda_p + 1) * vx_mps / wheel_radius_m
    
    return wheel_angular_velocity_mps

def set_wheel_speed(wheel_angular_velocity_radps):
    #Send torque request to inverter and use some sort of controller
    return 0

def read_ground_speed_sensor_mps():
    speed = 0
    return speed

def read_encoder_mps():
    speed = 0
    return speed

def which_pedal():
    #Return "brake" or "accel"
    return "brake"

def send_torque_request(torque_Nm):
    #CAN
    success = True
    

class Controller():
    def __init__(self)
        self.vx_initial_mps = read_ground_speed_sensor_mps()
        self.wheel_velocity_initial_mps = read_wheel_speed_mps()
        self.vxs = []
        self.wheel_speeds = []
        self.vxs.append(vx_initial)
        self.wheel_speeds.append(wheel_velocity_initial_mps)

    def adjust_motor_torque(self)
        pedal = which_pedal()
        wheel_velocity_mps = read_encoder_mps()
        vx_mps = read_ground_speed_sensor_mps()
        ideal_wheel_velocity_mps = calculate_wheel_speed(vx_mps, lamda_p, wheel_radius_m, pedal)
        #Do some controller stuff

        torque_request_Nm = 0
        send_torque_request(torque_request_Nm)
        self.vxs.append(vx_mps)
        self.wheel_speeds.append(wheel_velocity_mps)


controller = Controller("some stuff")

from simple_pid import PID
pid = PID(1, 0.1, 0.05, setpoint= wheel_angular_velocity_mps )
pid.sample_time = 0.01

while driving == True:
    controller.adjust_motor_torque()
    controlled_slip = pid(current_wheelspeed)
    

