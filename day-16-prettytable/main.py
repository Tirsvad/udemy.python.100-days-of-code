# from turtle import Turtle, Screen
#
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("DarkGreen")
# timmy.forward(100)
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

students = [
    [
        1163,
        "Jens"
    ],
    [
        1164,
        "Neisamani"
    ],
    [
        1165,
        "Victoria"
    ],
    [
        1166,
        "Carl"
    ],
]

table = PrettyTable(
    [
        "ID",
        "name"
    ]
)

table.title = "Students"
for student in students:
    table.add_row(student)
table.align = "l"
print(table)