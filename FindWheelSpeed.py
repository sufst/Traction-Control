import numpy as np
from simple_pid import PID

#PID(kp, ki, kd, setpoint=optimal_wheel_speed)
pid.sample_time = 0.01


p1 = 10.5
p2 = 34.60
wheel_radius_m = 10 * 2.54 / 2
driving == True

lamda_p = p2 ** -0.5

#Optimal slip ratio is always constant
pid = PID(1, 0.1, 0.05, setpoint= lamda_p)


def calculate_wheel_speed(vx_mps, lamda_p, case):
    if case == "brake":
        wheel_angular_velocity_radps = (1 - lamda_p) * vx_mps / wheel_radius_m
    elif case == "accel":
        wheel_angular_velocity_radps = (lamda_p + 1) * vx_mps / wheel_radius_m
    
    return wheel_velocity_mps

def calculate_current_slip_ratio(vehicle_speed_mps, wheel_speed_mps, case):
    if case == "brake":
        lamda_actual = (vehicle_speed_mps - wheel_speed_mps) / vehicle_speed_mps
    elif case == "accel":
        lamda_actual = (wheel_speed_mps - vehicle_speed_mps) / vehicle_speed_mps
        
    return lamda_actual

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



class Controller():
    last_motor_torque = 0
    def __init__(self, inverter_CAN_ID)
        self.inverter_ID = inverter_CAN_ID
        
    
    def calculate_accel_torque_request(current_lamda):
        ratio = lamda_p / current_lamda
        torque_request = last_motor_torque * ratio
        last_motor_torque = torque_request
        
        #Send the accelerating torque request
        
    def calculate_brake_torque_request(current_lamda):
        ratio = lamda_p / current_lamda
        torque_request = last_motor_torque * ratio
        last_motor_torque = torque_request
        
        #Send the braking torque request

    def adjust_motor_torque(self)
        case = which_pedal()
        vehicle_speed_mps = read_ground_speed_sensor_mps()
        wheel_speed_mps = read_encoder()
        optimal_wheel_speed = calculate_optimal_wheel_speed(vehicle_speed_mps, lamda_p, case)
        current_lamda = calculate_current_slip_ratio(vehicle_speed_mps, wheel_speed_mps, case)
        compensated_lamda = pid(current_lamda)
        new_target_wheel_speed_mps = calculate_wheel_speed(vehicle_speed_mps, compensated_lamda, case)
        
        if case == "brake":
            calculate_brake_torque_request(current_lamda)
        if case == "accel":
            calculate_accel_torque_request(current_lamda)
        
        return
        


controller = Controller("0xA3")




while driving == True:
    controller.adjust_motor_torque()
   
    

