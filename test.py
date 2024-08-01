def suq(string):
    queue = []
    i = 0
    for char in string:
        if char == queue[i]:
            return char
        queue.append(char)
        i = i + 1
    return None


string1 = "hello"
print(suq(string1))  # Output will be 'l'
