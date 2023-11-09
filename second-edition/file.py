def openclose():
    with open('todo.txt') as tasks:
        for chore in tasks:
            print(chore, end='')
            