import wpilib

from wpilib.drive import DifferentialDrive
import math
from wpilib import Spark
import romi
class Drivetrain:


    def __init__(self):
        self.kCountsPerRevolution = 1440.0
        self.kWheelDiameterMeter = 0.07
        self.left_motor=Spark(0)
        self.right_motor=Spark(1)
        self.leftEncoder=wpilib.Encoder(4,5)
        self.rightEncoder=wpilib.Encoder(6,7)
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

    def resetEncoders(self) -> None:
        """Resets the drive encoders to currently read a position of 0."""
        self.leftEncoder.reset()
        self.rightEncoder.reset()

    def getLeftEncoderCount(self) -> int:
        return self.leftEncoder.get()

    def getRightEncoderCount(self) -> int:
        return self.rightEncoder.get()

    def getLeftDistanceMeter(self) -> float:
        return self.leftEncoder.getDistance()

    def getRightDistanceMeter(self) -> float:
        return self.rightEncoder.getDistance()

    def averageDistanceMeter(self) -> float:
        return (self.getRightDistanceMeter() + self.getLeftDistanceMeter()) / 2.0

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