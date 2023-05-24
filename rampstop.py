from wpimath.controller import PIDController
from autoroutine import AutoRoutine
from drivetrain import Drivetrain
class ClimbRamp(AutoRoutine):
    forward_rate = .8
    ended_ramp = False
    started_ramp = False
    def __init__(self, drivetrain: Drivetrain):
        self.drivetrain = drivetrain
        self.drivetrain.resetGyro()
        self.direction_controller = PIDController(4 / 10000, 2 / 10000, 0)
        self.direction_controller.setSetpoint(0)
        self.direction_controller.setTolerance(10)
        self.drivetrain.resetEncoders()
        self.reset()
    def run(self):
        if not (self.started_ramp or self.ended_ramp):
            self.drive_straight()
            self.started_ramp = self.did_tip_up()
        elif self.started_ramp and not self.ended_ramp:
            self.drive_straight()
            self.ended_ramp = self.reached_top()
        else:
            self.drivetrain.arcadeDrive(0, 0)
    def drive_straight(self):
        error = self.drivetrain.getLeftEncoderCount() -self.drivetrain.getRightEncoderCount()
        rotate = self.direction_controller.calculate(error)
        at_set_point = self.direction_controller.atSetpoint()
        print(f"{at_set_point=} {rotate=} {error=}")
        if not at_set_point:
            self.drivetrain.arcadeDrive(rotate, self.forward_rate)
        else:
            self.drivetrain.arcadeDrive(0, self.forward_rate)
    def did_tip_up(self) -> bool:
        tip = self.drivetrain.getGyroAngleY()
        print(f"{tip=}")
        if tip > 7:
            print("On Ramp")
            self.forward_rate = .5
            return True
        return False
    def reached_top(self) -> bool:
        tip = self.drivetrain.getGyroAngleY()
        print(f"{tip=}")
        if tip < 4:
            print("Finished Ramp")
            self.forward_rate = 0
            return True
        return False
    def reset(self) -> None:
        self.ended_ramp = False
        self.started_ramp = False
        self.forward_rate = .8
