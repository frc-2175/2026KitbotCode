import rev

class IntakeAndShooter:
    def __init__(self):
        self.intakeMotor = rev.SparkMax(20, rev.SparkLowLevel.MotorType.kBrushed)
        self.shooterMotor = rev.SparkMax(21, rev.SparkLowLevel.MotorType.kBrushed)

    def setIntakeSpeed(self, intakeSpeed: float):
        self.intakeMotor.set(intakeSpeed)

    def setShooterSpeed(self, shooterSpeed: float):
        self.shooterMotor.set(shooterSpeed)
