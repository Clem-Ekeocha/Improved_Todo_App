"""
Development of a To-do Program
"""

from functions import get_todos, write_todos
import time as tm

now = tm.strftime("%b %d, %Y %H:%M:%S")
print(f"The current time is {now}")

while True:
    user_action = input("Type add, show, edit, delete or exit:")
    user_action = user_action.strip()  # Strip the input of the user of any possible space

    if user_action.startswith("add"):
        todo = user_action[4:]
        todo = todo.capitalize()  # capitalize only the first letter of the sentence or word
        todos = get_todos()
        todos.append(todo + '\n')  # Append the new todos to the todos variable
        write_todos("todos.txt", todos)  # Open the todos file and write the new members to the text file

    elif user_action.startswith("show"):  # Bitwise operator to either run when show or display is used
        todos = get_todos()
        new_todos = [item.strip('\n') for item in todos]  # list comprehension to remove '\n' causing extra lines
        for index, item in enumerate(new_todos):
            item = item.title()  # capitalize the first letter of every word in the sentence
            index = index + 1
            output = f"{index}-{item}"
            print(output)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])  # Get input from user to edit on the list
            number = number - 1
            todos = get_todos()
            new_todo = input("Enter the replacement todo: ")
            todos[number] = new_todo + '\n'
            write_todos("todos.txt", todos)  # Open the todos file and add the new member to the text file
            print(f"The {new_todo} edit process has been completed")
        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith("delete"):
        try:
            num = int(user_action[7:])  # Accept the index number of the to-do and delete
            num = num - 1  # Match the input with the list indexing
            todos = get_todos()
            todo_to_remove = todos[num].strip('\n')  # The actual todos to remove
            todos.pop(num)
            write_todos("todos.txt", todos)  # Open the todos file and add the new member to the text file
            print(f"The {todo_to_remove} delete process has been completed")
        except IndexError:
            print("There is no item with that number")
            continue

    elif user_action.startswith("exit"):  # exit to end the loop and end the program
        break

    else:
        print("Command is not valid")

print("Bye!")
