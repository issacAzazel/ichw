#!/usr/bin/env python3

'''planet.py: 绘制模拟太阳系八大行星的动态图

__author__ = "xhL"
__pkuid__  = "1800011791"
__email__  = "linxiaohan@pku.edu.cn"
'''

import turtle
import math#两个模块

colors=['red', 'yellow', 'blue', 'green', 'orange',
        'purple', 'white', 'gray', 'brown', 'sea green']#十种颜色


def ellipse_a(r,e):
    '''通过半长轴和离心率算a
    '''
    return r/2
def ellipse_b(r,e):
    '''通过半长轴和离心率算b
    '''
    return((r/2)*math.sqrt(1-e**2))
def ellipse_c(r,e):
    '''通过半长轴和离心率算c
    '''
    return((r/2)*e)


def pra_ellipse(planet,r,e,i):
    '''椭圆参数方程对应的点
    '''
    planet.goto(ellipse_c(r,e)+ellipse_a(r,e)*math.cos(math.radians(i)),ellipse_b(r,e)*math.sin(math.radians(i)))#椭圆参数方程函数位置坐标函数


def preparing(planet,r,e,color,size,t):
    '''让所有的行星到达自己的初始位置并做好各种准备
    '''
    planet.penup()
    planet.goto(ellipse_c(r,e)+ellipse_a(r,e),0)
    planet.pendown()
    planet.color(colors[color])
    planet.shape('circle')
    planet.shapesize(size,size,size)
    planet.speed(0)#运动前准备函数


def main():
    '''main module
    '''

    
solar_system=turtle.Screen()
solar_system.bgcolor("black")
solar_system.screensize(900, 600)#设置背景和背景色


sun=turtle.Pen()
sun.dot(50,colors[4])
sun.hideturtle()#画一个橘红色的太阳


water_planet=turtle.Turtle()
gold_planet=turtle.Turtle()
earth_planet=turtle.Turtle()
fire_planet=turtle.Turtle()
tree_planet=turtle.Turtle()
dust_planet=turtle.Turtle()
skyking_planet=turtle.Turtle()
seaking_planet=turtle.Turtle()
halei_planet=turtle.Turtle()#命名行星


preparing(water_planet,60,0,1,0.25,80)
preparing(gold_planet,100,0,2,0.5,150)
preparing(earth_planet,125,0.03,3,0.5,300)
preparing(fire_planet,150,0.05,5,0.25,600)
preparing(tree_planet,300,0.1,6,1.5,1000)
preparing(dust_planet,400,0.2,7,1.2,2000)
preparing(skyking_planet,500,0.1,8,0.75,4000)
preparing(seaking_planet,600,0.1,9,0.75,6000)
preparing(halei_planet,1500,0.967,6,0.75,5000)#行星准备#哈雷彗星小彩蛋！在画布上也看不见orz甚至要和太阳撞上啦！


while True:
    sign=solar_system.textinput("死循环警告", "是否退出(请填是或否)")
    if sign=='是':
        break
    else:
        for i in range(5760):
            pra_ellipse(water_planet,60,0,4*i)
            pra_ellipse(gold_planet,100,0,1.5*i)
            pra_ellipse(earth_planet,125,0.03,i)
            pra_ellipse(fire_planet,150,0.05,0.75*i)
            pra_ellipse(tree_planet,300,0.1,0.5*i)
            pra_ellipse(dust_planet,400,0.2,0.25*i)
            pra_ellipse(skyking_planet,500,0.1,0.125*i)
            pra_ellipse(seaking_planet,600,0.1,0.0625*i)
            pra_ellipse(halei_planet,1500,0.967,0.5*i)#行星运动死循环以及退出

        
if __name__ == '__main__':
    main()
