#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      koki
#
# Created:     17/06/2013
# Copyright:   (c) koki 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import spidev
import time
import wiringpi
import math

#import spi or math ,wiringpi,,,

#communication control
class Communication:
      def __init__(self):
          print "communication class made!"
          self.s = spidev.SpiDev()
          self.s.open(0,0)
          self.s.max_speed_hz=(500000)

          self.cs_md_pin = 25
          self.cs_md = wiringpi.GPIO(wiringpi.GPIO.WPI_MODE_GPIO)
          self.cs_md.pinMode(self.cs_md_pin,self.cs_md.OUTPUT)
          self.cs_md.digitalWrite(self.cs_md_pin,self.cs_md.HIGH)

          self.cs_ADC_pin = [24,23,18,22,17]
          self.cs_ADC =[]
          for i in range(5):
              self.cs_ADC.append(wiringpi.GPIO(wiringpi.GPIO.WPI_MODE_GPIO))
              self.cs_ADC[i].pinMode(self.cs_ADC_pin[i],self.cs_ADC[i].OUTPUT)
              self.cs_ADC[i].digitalWrite(self.cs_ADC_pin[i],self.cs_ADC[i].HIGH)


      def set_mortor_paramertor(self,mortor_number,direction,speed):
          print"sending data to mortor %d ..." % (mortor_number)
          data1 = speed
          data2 = mortor_number<<2 | direction
          self.cs_md.digitalWrite(self.cs_md_pin,self.cs_md.LOW)
          self.s.xfer2([data1,data2])
          self.cs_md.digitalWrite(self.cs_md_pin,self.cs_md.HIGH)

          print"sending data is complete!"

      def get_raw_ADCs_value_array(self):
          print"getting ADC data..."
          data = []
          for i in range(5):
              cash = self.get_one_ADC_value(i)
              for j in range(8):
                  data.append(cash[j])
          for i in range(4):
              data.pop()
          print"getting data is complete!"
          return data

      def get_one_ADC_value(self,ADC_number):
          v = []
          for i in range(8):
              self.cs_ADC[ADC_number].digitalWrite(self.cs_ADC_pin[ADC_number],self.cs_ADC[ADC_number].LOW)
              a = 128|(i<<4)
              r = self.s.xfer2([1,a,0])
              v.append(((r[1]&3)<<8)+r[2])
              self.cs_ADC[ADC_number].digitalWrite(self.cs_ADC_pin[ADC_number],self.cs_ADC[ADC_number].HIGH)
          return v #v is a list having 8 values.





#proofread and proofreading array management
class Proofread:
      def __init__(self,communication_class):
          print "proofread instanse made!"
          self.y_white = 1024 #AD_MAX
          self.y_black = 0    #AD_min
          #self.com = communication_class
          self.com = Communication()
          self.a = []
          self.b = []

      def setting_a_b_array(self):
          k='n'
          while k!='y':
                k = raw_input("all senor on white? [y/n]")
          print"OK!"
          print"i'm getting a ADC value..."
          #get x_white[36]
          x_white = self.com.get_raw_ADCs_value_array()
          print"complete!"
          print"next,put car on black"
          k='n'
          while k!='y':
                k = raw_input("all senor on black? [y/n]")
          print"OK!"
          print"i'm getting  ADC values..."
          #get x_black[36]
          x_black = self.com.get_raw_ADCs_value_array()
          print"complete!"
          print "calculating a array and b array..."
          for i in range(36):
              self.a.append((self.y_white-self.y_black)/(x_white[i]-x_black[i]))
          for i in range(36):
              self.b.append(self.y_white-self.a[i]*x_white[i])
          print "calcrating complete!"

      def convert_to_proofread_values(self,raw_ADC_data_list):
          print "null"
          y = []
          for i in range(36):
              y.append(self.b[i]+self.a[i]*raw_ADC_data_list[i])
          return y






def main():
    c = Communication()
    c.set_mortor_paramertor(0,1,128)
    #c = Proofread()
    #c.setting_a_b_array()

if __name__ == '__main__':
    main()

