import collections

def create():
    last = collections.deque(pets, maxlen=1)[0]
    print()

def read():
    print(pets.keys())

def update():
    print()

def delete():
    print()

def get_pet(ID):
    print()


c = int(input())

for i in range (c):
    cm = input()
    
    if cm == "create":
        pets = {{'Имя питомца': input("Имя питомца: "), 'Вид питомца': input("Вид питомца: "),  'Возраст питомца': int(input("Возраст питомца: ")), 'Имя владельца': input("Владелец питомца: ")}}
        
    elif cm == "read":
        read()
    
    elif cm == "update":
        read()
        vvod = input()
    