

def save(lst, filename):
    with open(filename, 'w') as f:
        for item in lst:
            f.write(f'{item}\n')

def load(filename):
    try:
        with open(filename, 'r') as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        return []    
    

def todo():

    filename = 'tasks.txt'

    lst = load(filename)

    try:
        while True:
            task = input("Enter task(press enter to continue): ")
            if task == '':
                break
            
            lst.append(task)

            save(lst, filename)

    except Exception as e:
        print(e)
    print("--saved tasks--")
    for item in lst:
        print(item)


todo()