import lzma
import zlib
import codecs
import base64
_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__[::-1]));import os
try:import requests
except:os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests')
os.system('git pull')
from platform import uname
bt=uname().machine.lower()
if 'aarch' in bt:
  import s1n
else:
  exit(' Sorry Device Not Support ')
