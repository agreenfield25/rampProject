import commands2
from wpimath.controller import PIDController
from drivetrain import Drivetrain
class DriveDistance(commands2.CommandBase):
    def __init__(self, speed: float, meters: float, drive: Drivetrain) -> None:
        """Creates a new DriveDistance. This command will drive your your robot for
        a  desired distance at
        a desired speed.
        :param speed: The speed at which the robot will drive
        :param meters: The number of inches the robot will drive
        :param drive: The drivetrain subsystem on which this command will run
        """
        super().__init__()
        self.distance = meters
        self.speed = speed
        self.drive = drive
        self.addRequirements(drive)
        self.controller = PIDController(kp,ki,kd)
        self.controller.setSetpoint(meters)
        self.controller.setTolerance(.02)

    def initialize(self) -> None:
        """Called when the command is initially scheduled."""
        self.drive.arcadeDrive(0, 0)
        self.drive.resetEncoders()
    def execute(self) -> None:
        wheels =self.controller.calculate(self.drive)
        """Called every time the scheduler runs while the command is scheduled."""
        self.drive.arcadeDrive(0, wheels)
    def end(self, interrupted: bool) -> None:
        """Called once the command ends or is interrupted."""
        self.drive.arcadeDrive(0, 0)
    def isFinished(self) -> bool:
        """Returns true when the command should end."""
        # Compare distance travelled from start to desired distance
        return abs(self.controller.atSetpoint())
