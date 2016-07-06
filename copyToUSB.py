import logging
import datetime as date
import subprocess
import os
import re

# logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

logger.info("Start of the programme")

list = []
for line in subprocess.check_output(["lsblk", "-l"]).splitlines():
  line = line.decode("utf-8")
  if "media" in line:
    list = re.split('\s+', line)
    logger.debug(list)
 
targetDir = list[-1]
print(targetDir)
if os.path.exists(targetDir):
  targetDir = os.environ.get("HOME", "/home/santosh")
#   print(targetDir)
  
pic = date.datetime.now().strftime('%H%M%S%f')[:-3]
cmd = "ffmpeg -y -i rtsp://192.168.1.88:554/stander/livestream/0/0 -r 10 -f image2 %s/%s.jpg" %(targetDir,pic)
 
p = subprocess.call(cmd, shell=True, stderr=subprocess.PIPE)
logger.debug(cmd)

