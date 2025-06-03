import os
import subprocess
import sys


def update_and_restart():
  '''
  Update the client by pulling the latest changes from the git repository
  and restart the client if there are new changes.
  '''
  old_hash = subprocess.check_output(['git', 'rev-parse', 'HEAD']).strip()
  subprocess.run(['git', 'pull'], check=True)
  new_hash = subprocess.check_output(['git', 'rev-parse', 'HEAD']).strip()

  if old_hash != new_hash:
    print('[INFO] New version detected. Restarting...')
    python = sys.executable
    os.execv(python, [python] + sys.argv)
  else:
    print('[INFO] Already up to date. No restart needed.')
