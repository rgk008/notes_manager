import os
from pymongo.mongo_client import MongoClient
from add import add
from view import view
from delete import delete
from about_us import about_us
from donate_us import donate_us




print("""
##    ##  #######  ######## ########  ######     ##     ##    ###    ##    ##    ###     ######   ######## ########  
###   ## ##     ##    ##    ##       ##    ##    ###   ###   ## ##   ###   ##   ## ##   ##    ##  ##       ##     ## 
####  ## ##     ##    ##    ##       ##          #### ####  ##   ##  ####  ##  ##   ##  ##        ##       ##     ## 
## ## ## ##     ##    ##    ######    ######     ## ### ## ##     ## ## ## ## ##     ## ##   #### ######   ########  
##  #### ##     ##    ##    ##             ##    ##     ## ######### ##  #### ######### ##    ##  ##       ##   ##   
##   ### ##     ##    ##    ##       ##    ##    ##     ## ##     ## ##   ### ##     ## ##    ##  ##       ##    ##  
##    ##  #######     ##    ########  ######     ##     ## ##     ## ##    ## ##     ##  ######   ######## ##     ## 
""")

db_uri = "mongodb+srv://rgk008:pilota380@cluster0.4o9zwji.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(db_uri)
print(client)
db = client["notes_manager"]

print()
input("Press any key to continue :)")
print("here are the some modification tools are provided.What modification do you want to do?")
while True:
    os.system("cls")
    print("Wecome to notes app")
    print("                            Menu")
    print("1.Add\n2.View\n3.Delete\n4.About us\n5.Donate us\n6.Exit")
    print()
    op=int(input("Choose an option:"))
    
    #To add the data
    if op == 1:
        add(db)
        input("Do you want to save (y/n): ")
        print()
        
    #To view the data
    if op == 2:
        view(db)
        
        print()

    #To delete the data
    if op == 3:
        delete(db)
        
        print()

    #About us
    if op == 4:
        about_us(db)
        input("press any key to go back:") 

    #Donate us
    if op == 5:
        donate_us()
        input("press any key to go back: ")

    #Exit
    if op == 6:
        print("Thank you for using the program")
        input("press any key to go exit:")
        break     