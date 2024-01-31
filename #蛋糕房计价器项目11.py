#蛋糕房计价器项目11
name="小白"
ml_material=3
s_material=2
fruit=1
cake_s=15
cake_m=20
cake_l=25
money=0
print("欢迎光临"+name+"蛋糕房!")
Cake_sml=input("你需要什么型号的蛋糕？s="+str(cake_s)+"元,m="+str(cake_m)+"元,l="+str(cake_l)+"元?:")
Cake_material=input("你需要加一些夹层奶油吗？如果需加大约"+str(s_material)+"元至"+str(ml_material)+"，n or y：")
Cake_fruit=input("你需要加一些水果吗？如需要加则需另加"+str(fruit)+"元，n o ry：")
if Cake_sml.lower() == "s":
    money+=cake_s
elif Cake_sml.lower() == "m":
    money+=cake_m
elif Cake_sml.lower() == "l":
    money+=cake_l
else:
    print("请按照指示回复数字s，m，l，否则计价将不准确。")

if Cake_material.lower() == "y":
    if money == cake_s:
        money += s_material
    else:
        money += ml_material
elif Cake_material.lower() == "n":
    money += 0
else:
    print("请按照指示回复,Y or N,否则计价将不准确。")

if Cake_fruit.lower() == "y":
    money += fruit
elif Cake_fruit.lower() == "n":
    money += 0
else:
    print("请按照指示回复,Y or N,否则计价将不准确。")
print("你本次共消费",str(money),"元")
