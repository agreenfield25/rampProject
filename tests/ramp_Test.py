import pytest
from pytest import MonkeyPatch
from unittest.mock import MagicMock


import rampstop
from drivetrain import Drivetrain
from rampstop import ClimbRamp
@pytest.fixture
def drivetrain()->Drivetrain:
        drive = Drivetrain()
        drive.leftEncoder=MagicMock()
        drive.rightEncoder=MagicMock()
        drive.left_motor=MagicMock()
        drive.right_motor=MagicMock()
        drive.drive=MagicMock()
        drive.gyro=MagicMock()
        return drive

@pytest.mark.parametrize(('gyro_number','output'),((2,True),(5,False) ))
def test_reached_top(drivetrain: Drivetrain, monkeypatch: MonkeyPatch,gyro_number,output)->None:
        ramp = ClimbRamp(drivetrain)

        def mock_gyro(self):
                return gyro_number

        monkeypatch.setattr(mock_gyro,Drivetrain, 'getGyroAngleY', mock_gyro)
        #action
        top=ramp.reached_top()
        #assert
        assert top== output
@pytest.mark.parametrize(('gyro_value','on_ramp'),((8,True),(6,False) ))
def test_did_tip_up(drivetrain: Drivetrain, monkeypatch: MonkeyPatch,gyro_value,on_ramp)->None:
        halfway = ClimbRamp(drivetrain)

        def mock_gyro(self):
                return gyro_value

        monkeypatch.setattr(mock_gyro, Drivetrain, 'getGyroAngleY', mock_gyro)
        # action
        top = halfway.did_tip_up()
        # assert
        assert top == on_ramp

def test_reset(drivetrain: Drivetrain)->None:
        halfway = ClimbRamp(drivetrain)
        halfway.forward = .7
        halfway.ended_ramp=True
        halfway.started_ramp=True

        ClimbRamp.reset()

        assert halfway.ended_ramp == False
        assert halfway.started_ramp == False
        assert halfway.forward == .8











