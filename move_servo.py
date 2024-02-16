from pymavlink import mavutil



#master = mavutil.mavlink_connection('com5')
#master = mavutil.mavlink_connection('com5')
master = mavutil.mavlink_connection('/dev/ttyUSB0')
def set_servo_pwm(servo_n, microseconds):
    master.mav.command_long_send(
        master.target_system, master.target_component,
        mavutil.mavlink.MAV_CMD_DO_SET_SERVO,
        0,            # first transmission of this command
        servo_n,  # servo instance, offset by 8 MAIN outputs
        microseconds, # PWM pulse-width
        0,0,0,0,0     # unused parameters
    )


set_servo_pwm(16, 5)