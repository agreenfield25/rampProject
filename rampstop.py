import wpilib

from wpimath.controller import PIDController


class Rampstop():

    def __init__(self, drivetrain,ontheramp,current_reading):
        self.drivetrain=drivetrain
        #self.goal=goal_in_meters
        #self.kp=-20
        self.pid_controller=PIDController(-20,0,0)
        self.pid_controller.setSetpoint(0)
        self.pid_controller.setTolerance(.05)
        self.ontheramp = 0
        self.current_reading = 0

    def run(self):
        self.current_reading = self.drivetrain.getGyroAngleY()

        difference = self.drivetrain.getLeftDistanceMeter() - self.drivetrain.getRightDistanceMeter()
        rotate = self.pid_controller.calculate(difference)

        if self.ontheramp==0:
            forward = .5
        if self.current_reading>10:
            forward = .3
            self.ontheramp=1
            print("On The Ramp")

        if self.ontheramp==1 and self.current_reading<2:
            self.drivetrain.arcadeDrive(0,0)

        if self.pid_controller.atSetpoint():
            rotate = 0
        else:
            print( f"Fwd: {forward}, Rot: {rotate}  distance:{self.drivetrain.averageDistanceMeter()} difference:{difference}")
            self.drivetrain.arcadeDrive(rotate, forward)