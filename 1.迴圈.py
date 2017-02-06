# -*- coding: utf8 -*-
import turtle               # 匯入turtle套件，允許我們使用turtle指令
window = turtle.Screen()        # 產生畫布以進行畫圖
window.bgcolor("lightgreen")# 設定畫布底色為淺綠色

marry = turtle.Turtle()         # 建立一個海龜turtle，它的名字叫marry

marry.pensize(5)                        # 設定畫筆粗細為5個像素
marry.left(72)
colors = ["yellow", "red", "purple", "blue", "gray"]
for pen_color in colors:
    marry.color(pen_color)
    marry.forward(150)
    marry.right(144)

window.exitonclick


