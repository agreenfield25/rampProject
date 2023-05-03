from autoroutine import AutoRoutine
from wpimath.controller import PIDController

class DriveStraight(AutoRoutine):

    def __init__(self, drivetrain, goal_in_meters):
        self.drivetrain=drivetrain
        #self.goal=goal_in_meters
        self.pid_distance=PIDController(20,0,0)
        self.pid_distance.setSetpoint(2)
        self.pid_distance.setTolerance(.01)
        #self.kp=-20
        self.pid_controller=PIDController(-20,0,0)
        self.pid_controller.setSetpoint(0)
        self.pid_controller.setTolerance(.05)

    def run(self):

        difference=self.drivetrain.getLeftDistanceMeter()-self.drivetrain.getRightDistanceMeter()
        rotate=self.pid_controller.calculate(difference)
        forward = self.pid_distance.calculate(self.drivetrain.averageDistanceMeter())
        if self.pid_controller.atSetpoint():
            rotate=0
        if self.pid_distance.atSetpoint():
            self.drivetrain.arcadeDrive(0,0)
        else:
            #rotate=0
            #forward=.4
            print(f"Fwd: {forward}, Rot: {rotate}  distance:{self.drivetrain.averageDistanceMeter()} difference:{difference}")
            self.drivetrain.arcadeDrive(rotate, forward)