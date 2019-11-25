import regex as re
f = open('food.txt','r+')

def readdd(item, file):
        x = list(file.readlines())
        print(x)
        a = re.compile('item',x)
        print(a)

food = input(str("enter name of food"))
readdd(food, f)