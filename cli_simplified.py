prompt0 = "Type add or exit:"
prompt1 = "Type add, show, edit, complete or exit:"
prompt2 = "Enter a todo:"
while True:
    file = open("todos.txt", "r")
    tasklist = file.readlines()
    file.close()
    length = len(tasklist)
    print(f"Items on the todo list: {length}")
    user_action = input(prompt1)
    user_action = user_action.strip()
    user_action = user_action.casefold()
    match user_action:
        case 'add':
            todo = input(prompt2) + "\n"
            tasklist.append(todo.capitalize())
            file = open("todos.txt", "w")
            file.writelines(tasklist)
            file.close()

        case 'show' | 'display':
            print("Here is your todo list:")
            new_list = [item.strip('\n') for item in tasklist]
            for index, item in enumerate(new_list):
                print(f"{index + 1}. {item}")

        case 'edit':
            number = int(input("Type number of the todo to edit (type 0 to display the list): "))
            if number == 0:
                print("Here is your todo list:")
                new_list = [item.strip('\n') for item in tasklist]
                for index, item in enumerate(new_list):
                    print(f"{index + 1}. {item}")
                number = int(input("Type number of the todo to edit:"))
                number = number - 1
                todo_to_edit = tasklist[number]
                print("Current todo:", todo_to_edit)
                edited_todo = input("Enter the edited todo:") + "\n"
                tasklist[number] = edited_todo.capitalize()
            else:
                number = number - 1
                todo_to_edit = tasklist[number]
                print("Todo to edit:", todo_to_edit)
                edited_todo = input("Enter the edited todo:")
                tasklist[number] = edited_todo.capitalize() + "\n"
            file = open("todos.txt", "w")
            file.writelines(tasklist)
            file.close()

        case 'complete':
            number = int(input("Number of the todo to complete (type 0 to display the list): "))
            if number == 0:
                print("Here is your todo list:")
                new_list = [item.strip('\n') for item in tasklist]
                for index, item in enumerate(new_list):
                    print(f"{index + 1}. {item}")
                number = int(input("Number of the todo to complete:"))
                number = number - 1
                tasklist.pop(number)
            else:
                number = number - 1
                tasklist.pop(number)
            file = open("todos.txt", "w")
            file.writelines(tasklist)
            file.close()
        case 'exit':
            break
        case _:
            print("Command not understood.")

