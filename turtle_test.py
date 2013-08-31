#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      koki
#
# Created:     27/08/2013
# Copyright:   (c) koki 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from turtle import TK,RawTurtle,TurtleScreen,Vec2D
import Tkinter
import time
import math
import random



class Player(RawTurtle):
      def hiding(self):
          print("calle hidding!")
          self.ht()
          self.up()
          self.clear()
          self.k_to_high = 0
          self.k_to_middle = 0
          self.k_to_low = 0
          self.k_to_producer = 0
          self.v -= self.v
          self.setposition(2000,2000)

      def get_K(self,player):
          if player.strengthpower == 3:
             return self.k_to_high
          elif player.strengthpower == 2:
             return self.k_to_middle
          elif player.strengthpower == 1:
             return self.k_to_low
          else:
               return self.k_to_producer

      def __init__(self,turtleScreen,player_type,posVector,k_to_high,k_to_middle,k_to_low,k_to_producer,m,R):
          RawTurtle.__init__(self,turtleScreen)             #タートル生成
          self.up()                                         #軌跡は書かない
          self.setpos(posVector)                            #初期位置
          self.resizemode("user")
          self.shape("circle")                              #プレイヤーの形
          self.shapesize(0.5)
          if player_type == "high_level_predator":
             self.color("red")                              #高域捕食者
             self.strengthpower = 3
             self.shape("triangle")
          elif player_type == "middle_level_predator":
               self.color("yellow")                       #中域捕食者
               self.strengthpower = 2
               self.shape("square")
          elif player_type == "low_level_predator":
               self.color("blue")                       #低域捕食者
               self.strengthpower = 1
               self.shape("turtle")
          else :
               self.color("dark green")                          #生産者
               self.strengthpower = 0
               self.shape("circle")

               #このクラスで新しく追加した変数
          self.acc = Vec2D(0,0)                             #初期加速度ゼロ
          self.v= Vec2D(0,0)                                #初期速度ゼロ
          self.m = m                                        #質量
          self.k_to_high = k_to_high                              #高域捕食者に対するK
          self.k_to_middle = k_to_middle                             #中域捕食者に対するK
          self.k_to_low = k_to_low                              #低域捕食者に対するK
          self.k_to_producer = k_to_producer                         #生産者に対するK
          self.R = R                                        #視野半径
          self.energy = 10




def close(root):
     root.destroy()
     root.quit()



def main():
    player_N = 15
    root = TK.Tk()
    canvas = TK.Canvas(root, width=1200, height=700, bg="#ddffff")
    canvas.pack()

    turtleScreen = TurtleScreen(canvas)
    turtleScreen.bgcolor("gray")
    turtleScreen.tracer(0,0)

    pl = []
    for i in range(player_N):               #プレイヤーの生成
        random.seed()
        window_h = turtleScreen.window_height()/2
        window_w = turtleScreen.window_width()/2
        x = random.uniform(-window_w,window_w)
        y = random.uniform(-window_h,window_h)
        m = random.uniform(1,5)
        R = 600
        pl_type = random.choice(["high_level_predator","middle_level_predator","low_level_predator","producer"])
        k_high = random.uniform(0,150)
        k_middle = random.uniform(0,150)
        k_low = random.uniform(0,150)
        k_producer = random.uniform(0,150)
        if pl_type == "high_level_predator":
           #k_high = 0
           pass
        elif pl_type == "middle_level_predator":
           k_middle = 0
           k_high *= -1
        elif pl_type == "low_level_predator":
             #k_low = 0
             k_high *= -1
             k_middle *= -1
        elif pl_type == "producer":
             #k_producer = 0
             k_high *= -1
             k_middle *= -1
             k_low *= -1
        pl.append(Player(turtleScreen,pl_type,(x,y),k_high,k_middle,k_low,k_producer,m,R))
        turtleScreen.update()
        #time.sleep(1)

    while(1):
             for me in turtleScreen.turtles():
                 me.acc -= me.acc
                 for you in turtleScreen.turtles():
                     r = you.pos()-me.pos()
                     r_d = abs(r)
                     if me != you and r_d<me.R and you.isvisible():
                        me.acc += (me.get_K(you)/(me.m*pow(r_d,3)))*r
                        if me.strengthpower == you.strengthpower:
                           me.acc = 0.3*me.acc+0.7*((r_d/me.R)*me.acc + ((me.R-r_d)/me.R)*you.acc)
                        if r_d<10 :
                           if me.strengthpower > you.strengthpower:
                              you.hiding()
                              me.energy += you.energy
                              me.v -= 1.1*me.v
                           elif me.strengthpower == you.strengthpower:
                                me.v = -0.1*r
                 me.v += me.acc
                 if abs(me.v)>10:
                    me.v = me.v*(10/abs(me.v))
                 me.setpos(me.pos()+me.v)
                 if me.xcor()<-600 or me.xcor()>600 or me.ycor()<-350 or me.ycor()>350:
                    me.v = (-0.5/abs(me.pos()))*me.pos()
                    me.acc -= me.acc
                 #print(me.energy)

             turtleScreen.update()
             time.sleep(0.01)



if __name__ == '__main__':
    main()
