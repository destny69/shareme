for i in range(0, 5):
    text = "H" * i
    textt = "H"
    text1 = text.rjust(4, " ")
    text2 = textt.center(0, " ")
    text3 = text.ljust(4, " ")
    print(text1 + text2 + text3)

for i in range(0, 5):
    text = "H" * 5
    text1 = text.ljust(10, " ")
    text2 = text.center(20, " ")

    print(text1 + text2)

for i in range(0, 3):
    text = "H" * 5
    text1 = text.ljust(10, "H")
    text2 = text.center(0, "H")
    text3 = text.rjust(10, "H")

    print(text1 + text2 + text3)

for i in range(0, 5):
    text = "H" * 5
    text1 = text.ljust(10, " ")
    text2 = text.center(20, " ")

    print(text1 + text2)


for i in range(0, 5):
    text = "H" * (4 - i)
    textt = "H"
    text1 = text.rjust(20, " ")
    text2 = textt.center(0, " ")
    text3 = text.ljust(4, " ")
    print(text1 + text2 + text3)
