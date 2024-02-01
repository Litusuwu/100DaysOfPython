# from turtle import Turtle, Screen

# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("cyan1")
# timmy.forward(120)
# timmy.left(100)
# timmy.forward(200)
# my_screen = Screen()
# print(my_screen.canvheight)

# my_screen.exitonclick()
from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water","Fire"])
print(table.align)
table.align = "r"
print(table)
