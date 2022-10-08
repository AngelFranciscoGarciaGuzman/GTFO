import random
import time
from time import sleep

#Proyecto escolar desarrollado por: 
#Ángel Francisco García Guzmán A01704203

#Inventario del jugador

inventory = {"health_pack": 0, "ammo_pack": 0, "access_key": 0}

character_values = [[100],[100]]
#lista anidada con las estadisticas del jugador (Health y Ammo), la verdad prefiero el metodo anterior de guardar cada uno como una variable en vez de utilizar listas, esto lo hago para el avance del proyecto "listas anidadas" pero si me agrada como funciona el diccionario para el inventario del jugador

rundown_number=""

#Asignar valor de busqueda para que no pueda buscar mas de una vez en la misma zona
search_value = 1

#Funcion sencilla para imprimir puntos con sleep

def dot_sleep (t):
    time.sleep(1)
    while t > 0:
        print(".")
        t -= 1
        time.sleep(1)


#Inicio del juego

time.sleep(1)

print("[Initializing... HYDROSTATIS DIAGNOSTIC protocol]")

dot_sleep(3)

print("[HYDROSTATIS DIAGNOSTIC protocol terminated]")

time.sleep(1)

print("[cmd load rndwn.prt]")

time.sleep(1)

print("[cmd run rndwn.prt]")

time.sleep(1)

print("[initializing... RUNDOWN protocol]")


prisoner_id = random.randint(10000000, 999999999)

time.sleep(2)
print("PRISONER ID",prisoner_id)
time.sleep(2)
print("SECTION",random.randint(1, 9),"ENTRYPOINT B3")

dot_sleep(3)


#Preguntar por nombre de jugador
name = input("ALIAS NAME NOT RECOGNIZED, PLEASE ENTER YOUR ALIAS NAME: ")

dot_sleep(3)
print("PRISONER",name)
time.sleep(1)
print("ID",prisoner_id)
time.sleep(1)
print("READY FOR CORTEX INTERFACE INJECTION\n")
time.sleep(1)

def select_rundown ():
    time.sleep(1)
    global rundown_number
    desition = 0
    while desition != 1:
        time.sleep(1)
        print("Please select a rundown number:\n")
        time.sleep(1)
        print("A1\n|\n|B1\n|\n|C1\n")
        rundown_number = str(input())
        if rundown_number == "A1":
            time.sleep(1)
            i = input("rundown number A1 selected, do you wish to continue? y/n: ")
            if i == 'y':
                desition = 1
            else:
                desition = 0
        elif rundown_number == "B1":
            time.sleep(1)
            i = input("rundown number B1 selected, do you wish to continue? y/n: ")
            if i == 'y':
                desition = 1
            else:
                desition = 0
        elif rundown_number == "C1":
            time.sleep(1)
            i = input("rundown number C1 selected, do you wish to continue? y/n: ")
            if i == 'y':
                desition = 1
            else:
                desition = 0
        else:
            time.sleep(1)
            print("Please enter a valid rundown number")
            time.sleep(1)


def selectitem (inventory):
    time.sleep(1)
    print("1. Ammo Pack\n2. Health Pack")
    item = int(input())
    if item == 1:
        time.sleep(1)
        print("You have selected Ammo Pack")
        #Asignar valor 1 a Ammo Pack en la lista Inventory
        inventory["ammo_pack"] = 1
    elif item == 2:
        time.sleep(1)
        print("You have selected Health Pack")
        #Asignar valor 1 a Health Pack en la lista Inventory
        inventory["health_pack"] = 1        

def check_inventory(inventory):
    time.sleep(1)
    print("This is your inventory: ")
    time.sleep(1)
    print(inventory)

def search(x, y, z):
    global search_value
    ammo_pack = x
    health_pack = y
    access_key = z
    if search_value == 1:
        search_value = search_value - 1
        if ammo_pack == 5:
            time.sleep(1)
            print("You've found: ammo_pack")
            inventory["ammo_pack"] = inventory["ammo_pack"] + 1
            if inventory["ammo_pack"] == 2:
                time.sleep(1)
                print("You can not have more than one (1) ammo_pack")
                inventory["ammo_pack"] = inventory["ammo_pack"] - 1
        else:
            time.sleep(1)
            print("You've found no ammo_pack")

        if health_pack == 5:
            time.sleep(1)
            print("You've found: health_pack")
            inventory["health_pack"] = inventory["health_pack"] + 1
            if inventory["health_pack"] == 2:
                time.sleep(1)
                print("You can not have more than one (1) health_pack")
                inventory["health_pack"] = inventory["health_pack"] - 1
        else:
            time.sleep(1)
            print("You've found no health_pack")
        
        if access_key == 10:
            time.sleep(1)
            print("You've found the acces_key")
            inventory["access_key"] = inventory["access_key"] + 1
            time.sleep(1)
            print("[Expedition completed]")
            time.sleep(1)
            print("[Prisoner:",name,"Id:",prisoner_id,"have survived]")
            exit()
        else:
            time.sleep(1)
            print("There is no access_key here")
    else:
        print("You've already searched this area")

    time.sleep(1)
    actions()

#Funcion de usar objeto para usuario, agragando y removiendo de la lista Inventory 
def use_object():
    global character_values
    i = False
    check_inventory(inventory)
    while i == False:
        time.sleep(1)
        print("What are you using on you? Type the key word")
        use = str(input())
        if use == "health_pack":
            if inventory["health_pack"] == 1:
                inventory["health_pack"] = inventory["health_pack"] - 1
                if character_values[0][0] >= 100:
                    time.sleep(1)
                    print("You use the health_pack, but you health is already at 100%")
                else:
                    character_values[0][0] = character_values[0][0] + 25
                    if character_values[0][0] > 100:
                        character_values[0][0] = 100
                        
                    time.sleep(1)
                    print("Your health is now",character_values[0][0])

            else:
                time.sleep(1)
                print("You have no health_pack left")
            i = True 
        elif use == "ammo_pack":
            if inventory["ammo_pack"] == 1:
                inventory["ammo_pack"] = inventory["ammo_pack"] - 1
                character_values[1][0] = character_values[1][0] + 25
                time.sleep(1)
                print("Your ammo is now:",character_values[1][0])
            else:
                time.sleep(1)
                print("You have no ammo_pack left")
            i = True
        else:
            time.sleep(1)
            print("Please enter a valid key word")
            i = False
    actions()

#Funcion para moverse entre zona y zona, cambiando el valor de search_value para que le permita volver a buscar objetos en la zona
def move_sector():
    global character_values
    global search_value

    search_value = search_value + 1
    if search_value > 1:
        search_value = 1
    time.sleep(1)
    print("You are moving to the next sector")
    dot_sleep(3)
    print("You've found:",random.randint(2,7),"sleepers")
    time.sleep(1)
    if random.randint(1,2) == 2:
        character_values[1][0] = character_values[1][0] - random.randint(7, 14)
        if character_values[1][0] <= 0:
            print("You've ran out of ammo")
            death()   
        time.sleep(1)     
        print("You kill them without waking them up")
        time.sleep(1)
        print("Your ammo is now:",character_values[1][0])
        actions()
    else:
        character_values[0][0] = character_values[0][0] - random.randint(20,31)
        if character_values[0][0] <= 0:
            time.sleep(1)
            print("You have 0 health points left")
            time.sleep(1)
            death()
        character_values[1][0] = character_values[1][0] - random . randint(15,37)
        if character_values[1][0] <= 0:
            time.sleep(1)
            print("You've ran out of ammo")
            time.sleep(1)
            death()  
        time.sleep(1)
        print("You've woken them up")
        time.sleep(1)
        print("Your ammo left is:",character_values[1][0])
        time.sleep(1)
        print("You've taken damage, your health is now:",character_values[0][0])
        actions()


#Funcion de muerte del jugador 
def death():
    time.sleep(1)
    print("[Expedition failed]")
    time.sleep(1)
    print("[Prisoner:",name,"Id:",prisoner_id,"have died in sector",rundown_number,"]")
    exit()


#Funcion de acciones para el usuario
def actions():
    time.sleep(1)
    print("1. Search location\n2. Use object from your inventory\n3. Go to the next sector")
    option = int(input())
    i = False
    while i == False:
        if option == 1:
            search(random.randint(1,5), random.randint(1,5), random.randint(1,10))
            i == True
        elif option == 2:
            use_object()
            i == True
        elif option == 3:
            move_sector()
            i == True
        else:
            print("Please enter a valid action")
            i = False


select_rundown()

dot_sleep(3)

print("You have selected rundown:",rundown_number)

time.sleep(1)

print("Before the rundown you must select a starting item")

selectitem(inventory)

check_inventory(inventory)

dot_sleep(3)

print("prisoner vitals at: 100%")
time.sleep(1)
print("prisoner ammo at: 100%\n")
time.sleep(1)
print("prepare for landing at sector:",rundown_number)
time.sleep(1)
print("objective: find the acces_key and get out... alive")

dot_sleep(5)
print("You have arrived, what are you doing?")
time.sleep(1)

actions()
