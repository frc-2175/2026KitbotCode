import rev

import configs

from wpilib.drive import DifferentialDrive
class Drivetrain:
    def __init__(self):
      self.leftDriveMotor = rev.SparkMax(19, rev.SparkLowLevel.MotorType.kBrushed)
      self.leftDriveFollowerMotor = rev.SparkMax(18, rev.SparkLowLevel.MotorType.kBrushed)
      self.rightDriveMotor = rev.SparkMax(16, rev.SparkLowLevel.MotorType.kBrushed)
      self.rightDriveFollowerMotor = rev.SparkMax(15, rev.SparkLowLevel.MotorType.kBrushed)

      leftDriveConfig = rev.SparkMaxConfig()
      leftDriveConfig.apply(configs.driveMotorConfig)
      leftDriveConfig.inverted(True)

      leftDriveFollowerConfig = rev.SparkMaxConfig()
      leftDriveFollowerConfig.apply(configs.driveMotorConfig)
      leftDriveFollowerConfig.follow(self.leftDriveMotor)

      self.leftDriveMotor.configure(leftDriveConfig, rev.ResetMode.kResetSafeParameters, rev.PersistMode.kPersistParameters)
      self.leftDriveFollowerMotor.configure(leftDriveFollowerConfig, rev.ResetMode.kResetSafeParameters, rev.PersistMode.kPersistParameters)

      rightDriveFollowerConfig = rev.SparkMaxConfig()
      rightDriveFollowerConfig.apply(configs.driveMotorConfig)
      rightDriveFollowerConfig.follow(self.rightDriveMotor)

      self.rightDriveMotor.configure(configs.driveMotorConfig, rev.ResetMode.kResetSafeParameters, rev.PersistMode.kPersistParameters)
      self.rightDriveFollowerMotor.configure(rightDriveFollowerConfig, rev.ResetMode.kResetSafeParameters, rev.PersistMode.kPersistParameters)

    def drive(self, driveSpeed: float, steerSpeed: float):
      speeds = DifferentialDrive.arcadeDriveIK(driveSpeed, steerSpeed)
      self.leftDriveMotor.set(speeds.left)
      self.rightDriveMotor.set(speeds.right)