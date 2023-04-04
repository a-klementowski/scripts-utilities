import json
import os
import subprocess
import sys


def restore():
    if len(sys.argv) == 1:
        directory = os.getcwd()
    elif len(sys.argv) == 2:
        directory = sys.argv[1]
    else:
        print("Wrong arguments")
        sys.exit(1)

    backup_dir = os.environ.get('BACKUPS_DIR', os.path.expanduser('~\.backups'))

    if not os.path.exists(backup_dir):
        print("Directory doesn't exist")
        sys.exit(1)

    history_file = os.path.join(backup_dir, 'backup_history.json')
    if not os.path.exists(history_file):
        print("No backups were created")
        sys.exit(1)

    with open(history_file, 'r') as f:
        backup_history = json.load(f)

    print("Select a backup to restore:")
    for i, backup in enumerate(backup_history):
        print(f"{i}. {backup['date']} - {backup['directory']}")

    try:
        selection = int(input("Enter the number of the backup: "))
        selected_backup = backup_history[selection]
    except ValueError:
        print("Invalid selection")
        sys.exit(1)

    backup_path = os.path.join(backup_dir, selected_backup['filename'])
    for f in os.listdir(directory):
        os.remove(os.path.join(directory, f))
    subprocess.run(['powershell', '-Command', f'Expand-Archive -Path "{backup_path}" -DestinationPath "{directory}"'])

    print(f"Directory restored: {selected_backup['filename']} to {directory}")


if __name__ == "__main__":
    restore()
