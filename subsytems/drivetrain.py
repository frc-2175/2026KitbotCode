import rev
from wpilib.drive import DifferentialDrive
class Drivetrain:
    def __init__(self):
      self.leftDriveMotor = rev.SparkMax(10, rev.SparkLowLevel.MotorType.kBrushless)
      self.rightDriveMotor = rev.SparkMax(11, rev.SparkLowLevel.MotorType.kBrushless)

    def drive(self, driveSpeed: float, steerSpeed: float):
      speeds = DifferentialDrive.arcadeDriveIK(driveSpeed, steerSpeed)
      self.leftDriveMotor.set(speeds.left)
      self.rightDriveMotor.set(speeds.right)