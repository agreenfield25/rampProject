import wpilib

from drivestraight import DriveStraight
from rampstop import Rampstop
from drivetrain import Drivetrain
from autoroutine import AutoRoutine

class RobotContainer:

    def __init__(self):
        self.controller = wpilib.Joystick(0)
        self.drivetrain = Drivetrain()
        self.chooser = wpilib.SendableChooser()
        self._configure()

    def _configure(self):
        self.chooser.setDefaultOption("Ramp", Rampstop(self.drivetrain, .5))
        wpilib.SmartDashboard.putData(self.chooser)

    def get_autonomous(self):
        return self.chooser.getSelected()