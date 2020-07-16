'''

Implementation of queue.
'''
size = int(input("enter the size of queue : "))
queue = []
def push():
    if len(queue) < size:
        queue.append(int(input("Enter the value of element : ")))
    else:
        print("Queue Overflow !")
    task()
def pop():
    if len(queue) > 0:
        queue.pop(0)
    else:
        print("Queue Underflow !")
    task()
def display():
    for i in queue:
        print(i)
def task():
    action = input("Press 1 to push\n Press 2 to pop\n Press 3 to display\n")
    if action == '1':
        push()
    elif action == '2':
        pop()
    elif action == '3':
        display()
    else:
        print("Invalid Input")
task()

