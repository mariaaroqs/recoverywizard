import os
import shutil
import subprocess
from datetime import datetime

class RecoveryWizard:
    def __init__(self):
        self.backup_dir = "C:\\RecoveryWizard\\Backups"
        self.create_backup_dir()

    def create_backup_dir(self):
        """Create a directory for backups if it doesn't exist."""
        if not os.path.exists(self.backup_dir):
            os.makedirs(self.backup_dir)

    def backup_data(self, source_path):
        """Backup data from the source path to the backup directory."""
        try:
            if os.path.exists(source_path):
                timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
                backup_path = os.path.join(self.backup_dir, f"backup_{timestamp}")
                shutil.copytree(source_path, backup_path)
                print(f"Backup created successfully at {backup_path}")
            else:
                print("Source path does not exist.")
        except Exception as e:
            print(f"Failed to create backup: {e}")

    def restore_data(self, backup_name, destination_path):
        """Restore data from a backup to the specified destination path."""
        try:
            backup_path = os.path.join(self.backup_dir, backup_name)
            if os.path.exists(backup_path):
                shutil.copytree(backup_path, destination_path)
                print(f"Data restored successfully to {destination_path}")
            else:
                print("Backup does not exist.")
        except Exception as e:
            print(f"Failed to restore data: {e}")

    def create_system_restore_point(self):
        """Create a system restore point."""
        try:
            command = 'wmic.exe /Namespace:\\\\root\\default Path SystemRestore Call CreateRestorePoint "RecoveryWizard Restore Point", 100, 7'
            result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if result.returncode == 0:
                print("System restore point created successfully.")
            else:
                print(f"Failed to create restore point: {result.stderr.decode()}")
        except Exception as e:
            print(f"Failed to create restore point: {e}")

    def list_backups(self):
        """List all backups available in the backup directory."""
        try:
            backups = os.listdir(self.backup_dir)
            if backups:
                print("Available backups:")
                for backup in backups:
                    print(f"- {backup}")
            else:
                print("No backups found.")
        except Exception as e:
            print(f"Failed to list backups: {e}")

if __name__ == "__main__":
    wizard = RecoveryWizard()
    # Example usage:
    # wizard.backup_data("C:\\User\\ExampleData")
    # wizard.restore_data("backup_20230101123000", "C:\\User\\RestoredData")
    # wizard.create_system_restore_point()
    # wizard.list_backups()