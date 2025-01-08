# RecoveryWizard

RecoveryWizard is a Python-based tool designed to assist with data recovery and system restore on Windows. It helps prevent data loss by providing functionalities to backup and restore data as well as create system restore points.

## Features

- **Data Backup**: Easily create backups of your important data to a designated backup directory.
- **Data Restore**: Restore data from a selected backup to a specified location.
- **System Restore Point**: Create a system restore point to safeguard your system settings.
- **List Backups**: List all available backups for easy restoration.

## Installation

1. Ensure you have Python installed on your Windows machine.
2. Clone this repository or download the `recovery_wizard.py` file.

## Usage

To use RecoveryWizard, run the `recovery_wizard.py` script. You can call the following methods:

- `backup_data(source_path)`: Create a backup of data from the specified source path.
- `restore_data(backup_name, destination_path)`: Restore data from the specified backup to the destination path.
- `create_system_restore_point()`: Create a Windows system restore point.
- `list_backups()`: List all available backups.

### Example

```python
wizard = RecoveryWizard()
wizard.backup_data("C:\\User\\ExampleData")
wizard.restore_data("backup_20230101123000", "C:\\User\\RestoredData")
wizard.create_system_restore_point()
wizard.list_backups()
```

## Note
- Ensure you have sufficient permissions to create and restore backups as well as system restore points.
- The script is intended for use on Windows systems.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.