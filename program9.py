'''
stack implementation
'''
size = int(input("Enter the size of stack:-->"))
stack = []
x = 0


Top = -1
def push():
    global Top
    if len(stack) < size:
        stack.append(int(input("Enter the value : ")))
        Top += 1

    else:
        print("stack Overflow !")
    task()
def pop():
    if len(stack) > 0:
        stack.pop(Top)
    else:
        print("Stack Underflow")
    task()
def display():
    for i in stack:
        print(i)

def task():
    action = input("Press 1 to PUSH element\n Press 2 to POP elements\n Press 3 to DISPLAY elements\n")
    if action == '1':
        push()
    elif action == '2':
        pop()
    elif action == '3':
        display()
    else:
        print("Invalid Input")
task()
