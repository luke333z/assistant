from ai import AI
import pyjokes
from todo import Todo,Item
import json
athena = AI()
todo = Todo ()

def joke():
    funny = pyjokes.get_joke()
    print(funny)
    athena.say(funny)   

def add_todo()->bool:
    item = Item()
    athena.say("What do you want to add to the list?")
    
    data = athena.listen()
    if data is not None:
        phrase = data[0].get('transcript')
        item.title = phrase
        todo.new_item(item)
        message = "Added " + item.title
        athena.say(message)
        return True
    
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
    data = athena.listen()
    if data is not None:
        phrase = data[0].get('transcript')
        item_title = phrase
        if item_title:
            item_title.lower()
        athena.say(todo.remove_item(title=item_title))
        return True


def item_age():
    athena.say("Which item do you want to see the age of?")
    item_title = athena.listen()
    #not finished

def tucafe():
    file = open('tucafe.txt', 'r')
    for line in file:
        athena.say(line)
    file.close


#testing area






#testing area
state = True
command = ""
def findCommand():
    data = athena.listen()
    if data is not None:
        for dictionary in data:
            command = dictionary.get('transcript')
            command = command.lower()
            print(command)
            if command == "tell me a joke":
                joke()
                command = ""
                break
            if command == "test voice":
                athena.say("Testing voice..")
                athena.say("The quick brown fox jumps over the lazy dog.")
                break
            if command == "add item":
                add_todo()
                command = ""  
                break
            if command == "list items":
                list_todos()
                command = ""
                break
            if command == "remove item":
                remove_todo()
                command = ""
                break
            if command == "terminate":
                state=False
            if command == 'coffee':
                tucafe()
                command = ""
                break
                
                
while state and command != 'testing':
    data = athena.listen()
    if data is not None:
        for dictionary in data:
            wakeword = dictionary.get('transcript')
            print(wakeword)
            if wakeword is None:
                print("watafaq")
            if wakeword is not None:
                wakeword = wakeword.lower()
                print(wakeword)
                if "activate" in wakeword:
                    print("activated. Listening for command")
                    findCommand()
                    break

athena.say("Shutting Down...")