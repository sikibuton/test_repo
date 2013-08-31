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

      def __init__(self,turtleScreen,player_type,posVector):
          RawTurtle.__init__(self,turtleScreen)             #タートル生成
          self.up()                                         #軌跡は書かない
          self.setpos(posVector)                            #初期位置
          self.resizemode("user")
          self.shape("circle")                              #プレイヤーの形
          self.shapesize(0.1)
          if player_type == "high_level_predator":
             self.color("red")                              #高域捕食者の色
          elif player_type == "middle_level_predator":
               self.color("yellow")                         #中域捕食者の色
          elif player_type == "low_level_predator":
               self.color("blue")                           #低域捕食者の色
          else :
               self.color("green")

               #このクラスで新しく追加した変数
          self.acc = Vec2D(0,0)                             #初期加速度ゼロ
          self.v= Vec2D(0,0)                                #初期速度ゼロ
          self.m = 1                                        #質量

          self.k_to_high = 100                              #高域捕食者に対するK
          self.k_to_middle = 0.01                           #中域捕食者に対するK
          self.k_to_low = 0.01                              #低域捕食者に対するK
          self.k_to_producer = 0.01                         #生産者に対するK




def main():

    root = TK.Tk()
    canvas = TK.Canvas(root, width=1200, height=700, bg="#ddffff")
    canvas.pack()

    turtleScreen = TurtleScreen(canvas)
    turtleScreen.bgcolor("gray")
    turtleScreen.tracer(0,0)


    t = Player(turtleScreen,"high_level_predator",[120,-100])
    t.down()
    t2 = Player(turtleScreen,"middle_level_predator",[210,-300])
    t3 = Player(turtleScreen,"low_level_predator",[200,-310])
    #t4 = Player(turtleScreen,"producer",[100,0])


    while(1):
             #for me in turtleScreen.turtles():
                # me.color("red")
             #加速度の決定
             r = t2.pos()-t.pos()                #tからt2へのベクトル
             if r.__abs__()<0:
                t.v = -t.v
             t.acc = (t.k_to_high/(t.m*pow(r.__abs__(),3)))*r

             r = t3.pos()-t.pos()                #tからt3へのベクトル
             if r.__abs__()<0:
                t.v = -t.v
             t.acc += (t.k_to_high/(t.m*pow(r.__abs__(),3)))*r


             #更新と値の制限処理
             t.v += t.acc
             if  math.sqrt(t.v[0]*t.v[0]+t.v[1]*t.v[1])>10 :
                t.v = t.v*(10/abs(t.v))
             if t.xcor()<-600 or t.xcor()>600:
                t.setpos(t.pos()*0.99)
                t.v -= 1.3*t.v
             if t.ycor()<-350 or t.ycor()>350:
                t.setpos(t.pos()*0.99)
                t.v -= 1.3*t.v
             t.setpos(t.pos()+t.v)

             print(t.pos())

             turtleScreen.update()
             time.sleep(0.01)

    time.sleep(2)
    root.destroy()
    root.quit()


if __name__ == '__main__':
    main()
