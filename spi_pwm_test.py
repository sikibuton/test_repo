﻿import spidev
import time
import wiringpi
import math

from class1 import Communication
from class1 import Proofread
#日本語OK？




if __name__ == '__main__':
   com = Communication()
   pr = Proofread(com)
   while True:
         rad = input('degree-->')
         speed = input('speed[0-255]-->')
         com.set_mortor_paramertor(0,1,speed)
         print com.get_raw_ADCs_value_array()
#ok?



