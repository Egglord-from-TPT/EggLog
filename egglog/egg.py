import sys
import time
import os
from pathlib import Path
os.makedirs(os.path.join(os.path.expanduser("~"), "Documents"), exist_ok=True)
os.chdir(os.path.join(os.path.expanduser("~"), "Documents"))
log=open("Log.txt", "a")
class logs():
    file=open(Path.home()/"Documents"/"Log.txt", "a")
    def write(self,text):
        open(Path.home()/"Documents"/"Log.txt", "a")
        self.file.write("["+str(time.strftime("%Y-%m-%d %H:%M:%S"))+"] "+text.replace("\n","\n["+str(time.strftime("%Y-%m-%d %H:%M:%S"))+"] ")+"\n")
        self.flush()
    def flush(self):
        log.flush()
sys.stdout=logs()
sys.stderr=logs()
