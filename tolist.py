
def save(lst, filename):

    with open(filename, 'w') as todo:
        for item in lst:
            todo.write(f"{item}\n")



def load(filename):

    try:
        with open(filename, 'r') as todo:
            return [line.strip() for line in todo.readlines()]
    except FileNotFoundError:
        return []


def todo():

    filename = "todo.txt"
    lst = load(filename)

    try:
        while True:
            task = input("Enter task(press enter continue): ")
            if task == '':
                break
            lst.append(task)
        
        save(lst, filename)
    except Exception as e:
        print(e)
    print("---your saved task---")
    for item in lst:
        print(item)


todo()


