#Permanent alias & crontab
import os
import sys
from time import sleep
import os





from time import sleep

print("Welcome to ...")

print("1) Create a Permanent Alias(bashrc)")
print("2) Create a command that execute every seconds/minutes/hours/months/years(crontab) ")

choice = input("Enter Choise : ")
choice = choice.strip()

if (choice == "1"):
    print("Creation of a Permanent Alias")
    print("Type the alias you whant to create :")
    alias = input("Enter Alias :")
    sleep(1)
    print("Type the command to be executed for the Alias : ")
    command = input("Enter command :")
    sleep(1)
    full_alias = ("{} = {}".format(alias ,command))
    print ("Confirm the alias : {}".format(full_alias))
    aliasconfirm = input("yes/no : ")
    aliasconfirm = aliasconfirm.strip()
    sleep(1)
    if (aliasconfirm == "yes"):
        print("yes")
        os.system('echo -e \'alias {}="{}"\' >> ~/.bashrc && source ~/.bashrc'.format(alias, command))    
    elif (aliasconfirm == "no"):
        print("Restarting ...")
        sleep(1)
        os.execl(sys.executable, sys.executable, *sys.argv)
    else :
        print("Wrong answer, restarting ...")
        sleep(1)
        os.execl(sys.executable, sys.executable, *sys.argv)



if (choice == "2"):
    print("Create a command that execute every minutes/hours/days/months/years")
    print("This will persist even after the system restarted")
    print("Choose how often the command should be executed :")
    print("1 - Every X Minutes")
    print("2 - Every X Hours")
    print("3 - Every X Days ")
    print("4 - Every X Month")
    print("5 - Every X Years")
    cronchoice = input("Choice : ")
    cronchoice = cronchoice.strip()
    if (cronchoice == "1"):
        print("Choose a number of Minutes ")
        numberofminutes = input("Choice [1-59] : ")
        numberofminutes = numberofminutes.strip()
        if numberofminutes == ("1"):
            cronstart = ("* * * * *")
        else:
            cronstart = ("*/{} * * * *".format(numberofminutes))
    if (cronchoice == "2"):
        print("Choose a number of Hours ")
        numberofhours = input("Choice [1-24] : ")
        numberofhours = numberofhours.strip()
        if numberofhours == ("1"):
            cronstart = ("0 * * * *")
        if numberofhours == ("24"):
            cronstart = ("0 0 * * *")
        else:
            cronstart = ("0 */{} * * * ".format(numberofhours))
    if (cronchoice == "3"):
        print("Choose a number of days")
        numberofdays = input("Choice :")
        numberofdays = numberofdays.strip()
        if numberofdays == ("1"):
            cronstart = ("0 0 * * *")
        else:
            cronstart=("0 0 */{} * *".format(numberofdays))
    if (cronchoice == "4"):
        print("Choose a number of Months")
        numberofmonths = input("Choice :")
        numberofmonths = numberofmonths.strip()
        if numberofmonths == ("1"):
            cronstart = ("0 0 1 * *")
        else:
            cronstart = ("0 0 1 */{} *".format(numberofmonths))
    if (cronchoice == "5"):
        print("Choose a number of years")
        numberofyears = input()
        numberofyears = numberofyears.strip()
        if numberofyears == ("1"):
            cronstart = ("0 0 1 1 *")
        else:
            cronstart = ("0 0 1 1 */{}".format(numberofyears))
    print("Enter the command to be executed :")
    command = input("Command : ")
    sleep(1)
    print("---------------------------------")
    print("There is a copy of the line that will be added to the crontab file :")
    print("{} {}".format(cronstart, command))
    print("---------------------------------")
    sleep(1)
    print('(crontab -u $(whoami) -l; echo "{} {}" ) | crontab -u $(whoami) -'.format(cronstart, command))
    os.system('(crontab -u $(whoami) -l; echo "{} {}" ) | crontab -u $(whoami) -'.format(cronstart, command))
    print("Done")


