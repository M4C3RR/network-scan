#!/usr/bin/python3

import os

# Ping Function

def new_ping():
    if choice == "y" or choice == "yes":
        y = input("How many times would you like to ping this IP? ")
        pings = os.system('ping -c '+y+' '+x)
        print(pings)
        new_scan()

# Nmap Scan

def new_scan():
    choice2 = input("Would you like to perform a port scan on this ip? [y/n]: ")
    if choice2 == "y" or choice2 == "yes":
        scan = os.system('nmap '+x+' -Pn')
        ssh_connect()

    else:
        choice3 = input("No worries. Would you like to attempt an SSH connection? [y/n]: ")
        if choice3 == "y" or choice3 == "yes":
            usr = input("What username will you try?: ")
            port = input("What port you would like to use for SSH?: ")
            ssh = os.system('ssh -p'+port+' '+usr+'@'+x)

        else:
            print("There is nothing left to do. Goodbye.")

# SSH Funtion 1

def ssh_connect():
    choice4 = input("Would you like to attempt to connect via SSH? [y/n]:")

    if choice4 == "y" or choice4 == "yes":
        usr = input("What username will you try?: ")
        port = input("What port you would like to use for SSH?: ")
        ssh = os.system('ssh -p'+port+' '+usr+'@'+x)

    elif choice4 == "n" or choice4 == "no":
        print("Goodbye")

    else: print("Invalid Entry")


# Main Display

choice = input("Would you like to initiate a network scan? [y/n]: ")
x = input("Enter an ip: ")

# Main Program

if choice == "y" or choice == "yes":
    new_ping()

elif choice =="n" or choice =="no":
    new_scan()

else:
    print("Invalid Inputs")


