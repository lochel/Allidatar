import os
import subprocess
import sys

from allidatar.version import version_tuple


def run_command(command):
  print(f'[INFO] Running command: {" ".join(command)}')
  subprocess.run(command, check=True, stdout=subprocess.DEVNULL)


def update_and_restart():
  '''
  Update the client by pulling the latest changes from the git repository
  and restart the client if there are new changes.
  '''
  current_hash = subprocess.check_output(['git', 'rev-parse', 'HEAD']).strip().decode('utf-8')
  print("[INFO] Current version:", version_tuple)
  print("[INFO] Current hash:", current_hash)
  run_command(['git', 'pull'])
  new_hash = subprocess.check_output(['git', 'rev-parse', 'HEAD']).strip().decode('utf-8')

  if current_hash != new_hash:
    print('[INFO] New version detected. Restarting...')
    python = sys.executable
    run_command([python, '-m', 'build'])
    run_command([python, '-m', 'pip', 'install', '-e', '.[dev]'])
    os.execv(python, [python] + sys.argv)
  else:
    print('[INFO] Already up to date. No restart needed.')
