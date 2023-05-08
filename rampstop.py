import wpilib

from wpimath.controller import PIDController


class Rampstop():

    def __init__(self, drivetrain):
        self.drivetrain=drivetrain
        #self.goal=goal_in_meters
        #self.kp=-20
        self.pid_controller=PIDController(-20,0,0)
        self.pid_controller.setSetpoint(0)
        self.pid_controller.setTolerance(.05)
        self.ontheramp=False
        self.current_reading = 0

    def run(self):
        forward=0
        self.current_reading = self.drivetrain.getGyroAngleY()

        difference = self.drivetrain.getLeftDistanceMeter() - self.drivetrain.getRightDistanceMeter()
        rotate = self.pid_controller.calculate(difference)

        if not self.ontheramp:
            forward = .3
            print (f"gyro:{self.current_reading}")
        if self.current_reading>3:
            forward = .2
            self.ontheramp=True
            print("On The Ramp")
            print (f"gyro:{self.current_reading}")

        if self.ontheramp==True and self.current_reading>5:
            self.drivetrain.arcadeDrive(0,0)

        if self.pid_controller.atSetpoint():
            self.rotate=0
        else:
            print( f"Fwd: {forward}, Rot: {rotate}  distance:{self.drivetrain.averageDistanceMeter()} difference:{difference}")

        self.drivetrain.arcadeDrive(forward,rotate)