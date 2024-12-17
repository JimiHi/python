
# prompt user to add items to their to-do list

task = int(input("""
Select one of the following options:
1. Add New Task:
2. View Current and Update Current Tasks:
3. Delete Task
4. Quit Program
: """)) 

def new_task():
    new_task = input("Enter new task:")
    tasks = []
    tasks.append(new_task)
    print(tasks)

def view_update_tasks():
    print("Hello")

def delete_task():
    print("placeholder")

def quit_program():
    print("placerholder")

if __name__ == "__main__":

    if task == 1:
        new_task()
    elif task == 2:
        view_update_tasks()
    elif task == 3:
        delete_task()
    elif task == 4:
        quit_program()
    else:
        print("You entered an invalid option. Try again")



# display to-do list

# allow user to enter = done when completed