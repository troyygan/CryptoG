import commands 
import os
from datetime import datetime, date, time
from pyDes import *

@profile
def aes_dec():
  print "AES Decrytion Started ..."
  before_time = datetime.now()
  #print "Time before AES Encryption Starts :", before_time
  os.system("python aes.py -d testfile_encrytped_AES.txt -o testfile_decrypted_AES.txt ")
  after_time = datetime.now()
  #print "Time after AES Encryption completes :", after_time
  total_time = after_time - before_time
  print "Total Time conceeded by AES Decryption", total_time

aes_dec()
