
def Menu():

    option = 0
    while option != 6:
        print(''' 
        -=-=-=-=-=-= Menu =-=-=-=-=-=-=-=-=
            Insert your option:
            [1] Create
            [2] Read
            [3] Update
            [4] Delete
            [5] Show All
            [6] Close program
        -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=      
            ''')
        option = int(input("Set your option: "))

        if option == 1:
            createPerson()

        elif option == 2:
            readPerson()

        elif option == 3:
            updatePerson()

        elif option == 4:
            deletePerson()

        elif option == 5:
            showPeople()

        elif option == 6:
            print("Thank you")        

        else:
            "invalid option"

def createPerson():
    name = str(input("Write a name: "))
    cpf = int(input("Write his/her cpf: "))

    if people.get(name):
        print("This name already exist: ")

    else:
        people[name] = cpf
        print("Person created")


def readPerson():
    name = str(input("Write a name to read: "))

    if people.get(name):
        print(name, people[name])
  
    else:
        print("This name does not exist")
  

def updatePerson():
    name = str(input("Write a person that you want to update: "))
    cpf = int(input("Write his/her new cpf: "))

    if name in people.keys():
        people[name] = cpf
        print("Cpf updated!")

    else:
        print("This person does not exist")


def deletePerson():
    name = str(input("Write a person you want to delete: "))

    if people.get(name):
        people.pop(name)
        print("Person deleted!")

    else:
        print("This person does not exist")


def showPeople():
    for name in people.keys():
        print("Name: ", name, "CPF: ", people[name])

people = {}
Menu()
