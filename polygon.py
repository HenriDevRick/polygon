import turtle

t = turtle.Turtle()

colors = {
    1: 'red',
    2: 'orange',
    3: 'black',
    4: 'green',
    5: 'indigo',
    6: 'blue',
    7: 'purple',
    8: 'violet',
    9: 'gold',
    10: 'cyan',
    11: 'rainbow'
}

def user_choice():
    print("What color would you like your polygon to be?")
    print("1- Red        6- Blue")
    print("2- Orange     7- Purple")
    print("3- Black      8- Violet")
    print("4- Green      9- Gold")
    print("5- Indigo     10- Cyan")
    print("11- Rainbow (random)")
    choice = int(input("Choice? "))
    return choice
    
def draw_polygon(sides, length, color):

    if color == 'rainbow':
        colors_list = ['red', 'orange', 'gold', 'green', 'blue', 'indigo', 'violet']
        for i in range(sides):
            t.color(random.choice(colors_list))
            t.fd(length)
            t.left(360 / sides)
    else:
        t.color(color)
        for _ in range(sides):
            t.fd(length)
            t.left(360 / sides)

    t.hideturtle()
    turtle.done()
    
def main():
    choice = user_choice()
    color = colors.get(choice, 'black')
    sides = int(input("How many sides for your polygon? "))
    length = int(input("What side length will your polygon have? "))

    draw_polygon(sides, length, color)

if __name__ == "__main__":
    main()