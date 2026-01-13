import wpilib
from subsytems.drivetrain import Drivetrain

class myRobot(wpilib.TimedRobot):
    def robotInit(self):
        self.drivetrain = Drivetrain()
        self.leftJoystick = wpilib.Joystick(0)
        self.rightJoystick = wpilib.Joystick(1)
        self.gamepad = wpilib.Joystick(2)

    def teleopPeriodic(self):
        driveSpeed = -self.gamepad.getRawAxis(1)
        steerSpeed = -self.gamepad.getRawAxis(4)
        self.drivetrain.drive(driveSpeed, steerSpeed)

    def disabledInit(self):
        self.drivetrain.drive(0, 0)