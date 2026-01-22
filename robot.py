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
        driveSpeed = -0.5 * self.leftJoystick.getRawAxis(1)
        steerSpeed = -0.75 * self.rightJoystick.getRawAxis(0)
        self.drivetrain.drive(driveSpeed, steerSpeed)

       #Intake and Flywheel
            #Left Button
        if self.gamepad.getRawButton(5):
            intakeSpeed = 0.3
            #Right Button
        elif self.gamepad.getRawButton(6):
            intakeSpeed = 0.8
        else:
            intakeSpeed = 0

        self.intakeandshooter.setIntakeSpeed(intakeSpeed)

        #Middlebar
            #Left Button
        if self.gamepad.getRawButton(5):
            middleBarSpeed = -0.7
            #Right Button
        elif self.gamepad.getRawButton(6):
            middleBarSpeed = 0.5
        else:
            middleBarSpeed = 0
        self.intakeandshooter.setShooterSpeed(middleBarSpeed)

    def disabledInit(self):
        self.drivetrain.drive(0, 0)
        self.intakeandshooter.setIntakeSpeed(0)
        self.intakeandshooter.setShooterSpeed(0)