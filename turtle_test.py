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



class Player(RawTurtle):
      def hiding(self):
          print("calle hidding!")
          self.ht()
          self.up()
          self.k_to_high = 0
          self.k_to_middle = 0
          self.k_to_low = 0
          self.k_to_producer = 0
          self.v -= self.v

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
               self.color("green")                          #生産者
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
          self.R = R                                     #視野半径




def close(root):
     root.destroy()
     root.quit()



def main():

    root = TK.Tk()
    canvas = TK.Canvas(root, width=1200, height=700, bg="#ddffff")
    canvas.pack()

    turtleScreen = TurtleScreen(canvas)
    turtleScreen.bgcolor("light gray")
    turtleScreen.tracer(0,0)


    t = Player(turtleScreen,"high_level_predator",[0,-140],0,100,100,100,6,500)
    t2 = Player(turtleScreen,"middle_level_predator",[500,100],-100,0,100,100,2,500)
    t3 = Player(turtleScreen,"producer",[-300,190],-100,-100,-100,0,1,500)
    t4 = Player(turtleScreen,"producer",[-300,-190],-100,-100,-100,50,3,500)
    t5 = Player(turtleScreen,"low_level_predator",[-600,-300],-100,-100,0,100,2,1000)

    while(1):
             for me in turtleScreen.turtles():
                 if me.isvisible()==0 :
                    break
                 me.acc -= me.acc
                 for you in turtleScreen.turtles():
                     r = you.pos()-me.pos()
                     if me != you and abs(r)<me.R and you.isvisible():
                        me.acc += (me.get_K(you)/(me.m*pow(abs(r),3)))*r
                        if abs(r)<10 :
                           if me.strengthpower > you.strengthpower:
                              you.hiding()
                              me.v -= me.v
                           elif me.strengthpower == you.strengthpower:
                                me.v += 0.1*you.v
                 me.v += me.acc
                 if abs(me.v)>10:
                    me.v = me.v*(10/abs(me.v))
                 me.setpos(me.pos()+me.v)
                 if me.xcor()<-600 or me.xcor()>600 or me.ycor()<-350 or me.ycor()>350:
                    me.v = (-0.5/abs(me.pos()))*me.pos()
                    me.acc -= me.acc

             turtleScreen.update()
             time.sleep(0.01)



if __name__ == '__main__':
    main()
