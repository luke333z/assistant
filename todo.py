from datetime import date
from datetime import datetime
from datetime import timedelta
from enum import Enum
from uuid import uuid4
import os
class Status(Enum):
    NOT_STARTED = 0
    IN_PROGRESS = 1
    COMPLETED = 2

class Priority(Enum):
    LOW = 0
    MEDIUM = 1
    HIGH = 2

class Item():
    __creation_date = datetime.now()
    __title = "empty"
    __status = Status.NOT_STARTED
    __priority = Priority.LOW
    __url = ""
    __notes = ""
    __icon = ""

    def __init__(self, title:str=None):
        if title is not None:
            self.__title = title
        self.__id = str(uuid4())

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value:str):
        self.__title = value

    @property
    def priority(self):
        return self.__priority.name
    
    @priority.setter
    def priority(self, value:Priority):
        self.__priority = value

    @property
    def creation_date(self):
        return self.__creation_date

    @creation_date.setter
    def creation_date(self, value):
        self.__creation_date = value

    @property
    def age(self):
        t1=timedelta(self.__creation_date)
        t2=timedelta(datetime.today())
        t=t2-t1
        return t.total_seconds/3600
    
    @property
    def status(self):
        return self.__status.name
    @status.setter
    def status(self, value:Status):
        self.__status = value

    @property
    def id(self):
        return self.__id

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, value:str):
        self.__url = value
    
    @property
    def icon(self):
        return self.__icon

    @icon.setter
    def icon(self, value:str):
        self.__icon = value

    @property
    def notes(self):
        return self.__notes

    @notes.setter
    def notes(self, value:str):
        self.__notes = value
        

class Todo():
    __todos = []

    def __init__(self):
        print("new todolist created")
        self._current = -1
        file = open("todo.txt", "r")
        count = 0
        for line in file:
            try:
                count+=1
                module = line.strip().split("<<>>")
                item1 = Item()
                item1.title=module[0]
                item1.creation_date=datetime.strptime(module[1],'%Y-%m-%d %H:%M:%S.%f')
                item1.status=module[2]
                item1.priority=module[3]
                item1.url=module[4]
                item1.notes=module[5]
                item1.icon= module[6]
                self.__todos.append(item1)
            except:
                pass
        file.close()
        

    def __iter__(self):
        return self
    
    def __next__(self):
        if self._current < len(self.__todos)-1:
            self._current+=1
            print(self.__todos[self._current].title)
            return self.__todos[self._current]
        else:
            self._current=-1
        raise StopIteration
    
    def __len__(self):
        return len(self.__todos)

    def new_item(self, item:Item):
        self.__todos.append(item)
        file = open("todo.txt", "a")
        file.write(item.title+"<<>>"+str(item.creation_date)+"<<>>"+item.status+"<<>>"+item.priority+"<<>>"+item.url+"<<>>"+item.notes+"<<>>"+item.icon+'\n')
        file.close()


    @property
    def items(self)->list:
        return self.__todos
    
    def show(self):
        print("*"*80)
        for item in self.__todos:
            print(item.title, item.status, item.priority)
    
    def remove_item(self, uuid:str=None, title: str=None)->bool:
        ok = False
        if title is None and uuid is None:
            return "You need to provide some details blah blah"
        if uuid is None and title:
            for item in self.__todos:
                if item.title == title:
                    self.__todos.remove(item)
                    ok=True
                    break
            if ok is True:   
                with open("todo.txt", "r") as fp:
                    lines = fp.readlines()
                with open("todo.txt", "w") as fp:
                    for line in lines:   
                        print(line)
                        if line.strip("\n") != str(item.title+"<<>>"+str(item.creation_date)+"<<>>"+item.status+"<<>>"+item.priority+"<<>>"+item.url+"<<>>"+item.notes+"<<>>"+item.icon):
                            fp.write(line)
                message = 'removed'+ item.title
                return message             
            message = "Item wirh title"+ title+ "not found"
            return message
    
    def age_item(self, title:str=None):
        
        return True
            
    


    

       