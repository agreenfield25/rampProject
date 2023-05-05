import os

import wpilib

from wpilib import TimedRobot
from robotcontainer import RobotContainer


class Robot(TimedRobot):

    def robotInit(self) -> None:
        self.container = RobotContainer()

    def robotPeriodic(self) -> None:
        ...

    def teleopInit(self) -> None:
        ...

    def teleopPeriodic(self) -> None:
        forward = self.container.controller.getRawAxis(1)
        rotate = self.container.controller.getRawAxis(0)
        self.container.drivetrain.arcadeDrive(rotate, forward)
        print(f"Forward: {forward}, Rotate: {rotate}")

    def autonomousInit(self) -> None:
        self.auto = self.container.get_autonomous()

    def autonomousPeriodic(self) -> None:
        self.auto.run()

    def autonomousExit(self) -> None:
        self.container.drivetrain.resetEncoders()
        self.container.drivetrain.resetGyro()

    def disabledInit(self) -> None:
        pass


if __name__ == "__main__":
    os.environ["HALSIMWS_HOST"] = "10.0.0.2"
    os.environ["HALSIMWS_PORT"] = "3300"

    wpilib.run(Robot)
