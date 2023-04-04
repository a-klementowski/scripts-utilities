import json
import os
import subprocess
import sys
import time


def backup():
    if len(sys.argv) != 2:
        print("Wrong arguments")
        sys.exit(1)

    directory = sys.argv[1]
    backup_dir = os.environ.get('BACKUPS_DIR', os.path.expanduser('~\.backups'))

    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)

    timestamp = time.strftime('%Y%m%d%H%M%S')
    dirname = os.path.basename(directory)
    ext = "zip"

    backup_filename = f'{timestamp}-{dirname}.{ext}'
    archive_path = os.path.join(backup_dir, backup_filename)

    subprocess.run(
        ['powershell', '-Command', f'Compress-Archive -Path "{directory}\\*" -DestinationPath "{archive_path}"'])

    history_file = os.path.join(backup_dir, 'backup_history.json')
    backup_date = time.strftime('%Y-%m-%d %H:%M:%S')
    backup_directory = os.path.abspath(directory)

    if not os.path.exists(history_file):
        with open(history_file, 'w') as f:
            backup_history = []
            json.dump(backup_history, f)

    with open(history_file, 'r+') as f:
        backup_history = json.load(f)
        backup_history.append({'date': backup_date, 'directory': backup_directory, 'filename': backup_filename})
        f.seek(0)
        json.dump(backup_history, f)

    print(f'Backup created: {archive_path}')


if __name__ == "__main__":
    backup()
