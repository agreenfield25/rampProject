import wpilib

from wpilib.drive import DifferentialDrive
import math
from wpilib import Spark
import romi
class Drivetrain:


    def __init__(self):
        self.left_motor=Spark(0)
        self.right_motor=Spark(1)
        # Set up the differential drive controller
        self.drive = wpilib.drive.DifferentialDrive(self.left_motor, self.right_motor)
        # Use meters as unit for encoder distances
        self.leftEncoder.setDistancePerPulse(
            (math.pi * self.kWheelDiameterMeter) / self.kCountsPerRevolution
        )
        self.rightEncoder.setDistancePerPulse(
            (math.pi * self.kWheelDiameterMeter) / self.kCountsPerRevolution
        )
        self.resetEncoders()

        self.gyro=romi.RomiGyro()

        self.accelerometer=wpilib.BuiltInAccelerometer()

    def arcadeDrive(self, rot: float, fwd: float) -> None:
        """
        Drives the robot using arcade controls.

        :param fwd: the commanded forward movement
        :param rot: the commanded rotation
        """
        self.drive.arcadeDrive(rot, fwd)

    def getGyroAngleY(self):
        """
        Give the twist of the robot
        :return: the current twist angle in degrees
        """

        return self.gyro.getAngleY()

    def resetGyro(self):
        """Resets the angles to all be 0."""

        self.gyro.reset()