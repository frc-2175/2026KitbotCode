import wpilib
from subsytems.drivetrain import Drivetrain
from subsytems.intakeandshooter import IntakeAndShooter

class myRobot(wpilib.TimedRobot):
    def robotInit(self):
        self.drivetrain = Drivetrain()
        self.intakeandshooter = IntakeAndShooter()
        self.leftJoystick = wpilib.Joystick(0)
        self.rightJoystick = wpilib.Joystick(1)
        self.gamepad = wpilib.Joystick(2)

    def teleopPeriodic(self):
        #Drive
        driveSpeed = -self.leftJoystick.getRawAxis(1)
        steerSpeed = -self.rightJoystick.getRawAxis(4)
        self.drivetrain.drive(driveSpeed, steerSpeed)

        #Intake
        intakeSpeed = 0.5 if self.gamepad.getRawButton(1) else 0
        self.intakeandshooter.setIntakeSpeed(intakeSpeed)

        #Shooter
        shooterSpeed = 0.5 if self.gamepad.getRawButton(2) else 0
        self.intakeandshooter.setShooterSpeed(shooterSpeed)

    def disabledInit(self):
        self.drivetrain.drive(0, 0)