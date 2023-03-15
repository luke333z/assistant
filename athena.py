from ai import AI
import pyjokes
from todo import Todo,Item

athena = AI()
todo = Todo ()

def joke():
    funny = pyjokes.get_joke()
    print(funny)
    athena.say(funny)   

def add_todo()->bool:
    item = Item()
    athena.say("What do you want to add to the list?")
    try:
        item.title = athena.listen()
        todo.new_item(item)
        message = "Added " + item.title
        athena.say(message)
        return True
    except:
        print("An error has occured")
        return False

def list_todos():
    if len(todo) > 0:
        athena.say("Here is your list")
        for item in todo:
            print(item.title, item.creation_date)
            athena.say(item.title)
    else:
        athena.say("The list is empty")

def remove_todo()->bool:
    athena.say("Which item do you want to remove?")
    item_title = athena.listen()
    if item_title:
        item_title.lower()
    athena.say(todo.remove_item(title=item_title))
    return True


def item_age():
    athena.say("Which item do you want to see the age of?")
    item_title = athena.listen()
    #not finished

#testing area



remove_todo()
list_todos()
remove_todo()



#testing area
command = "terminate"
while True and command != "terminate":
    try:
        athena.listen(command)
        command = command.lower()
    except:
        print("error")
        command = ""
    print(command)
    if command == "tell me a joke":
        joke()
        command = ""
    if command == "test volume" or command == "best volume":
        athena.say("Testing volume..")
        athena.say("The quick brown fox jumps over the lazy dog.")

    if command == "add item":
        add_todo()
        command = ""
        
    if command == "list items":
        list_todos()
        command = ""
    if command == "remove item":
        remove_todo()
        command = ""

athena.say("Shutting Down...")