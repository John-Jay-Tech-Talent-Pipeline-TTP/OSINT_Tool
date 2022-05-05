import time
from googlesearch import search
import sys


class colors:
	red = "\033[1;31;40m"
	green = "\033[1;32;40m"
	blue = "\033[1;34;40m"
	magneta = "\033[1;35;40m"
title = ("""
			▒┌───┬───┬──┬─┐▒┌┬────┐▒▒▒▒▒▒▒▒▒▒▒
			▒│┌─┐│┌─┐├┤├┤│└┐││┌┐┌┐│▒▒▒▒▒▒▒▒▒▒▒
			▒││▒││└──┐│││┌┐└┘├┘││└┘▒▒▒▒▒▒▒▒▒▒▒
			▒││▒│├──┐│││││└┐││▒││▒▒▒▒▒▒▒▒▒▒▒▒▒
			▒│└─┘│└─┘├┤├┤│▒│││▒││▒▒▒▒▒▒▒▒▒▒▒▒▒
			▒└───┴───┴──┴┘▒└─┘▒└┘▒▒▒▒▒▒▒▒▒▒▒▒▒
			▒▒▒▒▒▒▒▒▒▒▒▒▒┌───┬───┬───┬┐┌─┬───┐
			▒▒▒▒▒▒▒▒▒▒▒▒▒└┐┌┐│┌─┐│┌─┐│││┌┤┌─┐│
			▒▒▒▒▒▒▒▒▒▒▒▒▒▒│││││▒││└─┘│└┘┘│└──┐
			▒▒▒▒▒▒▒▒▒▒▒▒▒▒│││││▒││┌┐┌┤┌┐│└──┐│
			▒▒▒▒▒▒▒▒▒▒▒▒▒┌┘└┘│└─┘│││└┤││└┤└─┘│
			▒▒▒▒▒▒▒▒▒▒▒▒▒└───┴───┴┘└─┴┘└─┴───┘
""")

for col in title:
	print(colors.blue + col, end= "")
	sys.stdout.flush()
	time.sleep(0.0025)
	
description = "\n The tool uses advanced searching operators in the Goggle search engine to find specfic words or phrases which helps in finding any vulnerable web applications. It simplifies Google Dorking commands for the user and provides straightforward anaylsis of the information. Different information such as contact information, login credentials, files on a website, open ports, vulnerability of a specific website, and many more juicy stuff can be found online through google dorking. This tool allows you to be able to access that information wihout knowing any google dorking commands or strings.  \n"

for col in description:
	print(colors.magneta + col, end = "")
	sys.stdout.flush()
	time.sleep(0.01)
	
disclaimer = " \n This is for educational purposes and user should use it at their own risk. Some of the anaylsis might not be precise and CAUTION is advised when opening the links found through the results. \n\n "

for col in disclaimer:
	print(colors.red + col, end = "")
	sys.stdout.flush()
	time.sleep(0.01)
	
print("\033[1;32;40mHave fun hakcing *Hacker music in background*\n\n")

# uses console or default browser to display results.

#####################################################
# References
#
# https://exposingtheinvisible.org/en/guides/google-dorking/
# https://kit.exposingtheinvisible.org/en/how/google-dorking.html
# https://www.youtube.com/watch?v=u_gOnwWEXiA&ab_channel=NullByte
#
#########################################################

# menu
def menu():
    print("\033[1;37;40m1. Search for files on site")
    print("2. Search websites under a domain with a specific word")
    print("3. Search penetration and vulnerability reports on sites")
    print("4. Search for contact information")
    print("5. Search for http protocol")


time.sleep(.5)

# dorking commands
dorkSiteCommand = "site:"
dorkFileCommand = "filetype:"
dorkDomainCommand = "intitle:"
dorkUrl = "inurl:"

# vulnerability assessment reference
v1 = "qualys"
v2 = "acunetix"
v3 = "nessus"
v4 = "netsparker"
v5 = "nmap"

menu()

# taking user input
userInput = int(input("Choose an option: "))

if userInput == 1:
    site = input("Enter the site: ")                                # site to search
    fileType = input("Enter files you want to search: ")            # files to search
    counter = 0
    request = 0

    for results in search("https://google.com/search?q=" + site + " " + dorkFileCommand + fileType):
        counter = counter + 1
        print("[+] ", counter, results)        # display results in the console
        time.sleep(0.1)                        # delay
        request += 1
        if request >= 5:
            break
        data = (counter, results)              # limiting console output
        time.sleep(0.1)

    webbrowser.open_new("https://google.com/search?q=" + dorkSiteCommand + site + " " + dorkFileCommand + fileType)

if userInput == 2:
    site = input("Enter the site: ")
    userSpecific = input("Specific word or words you want to search: ")
    userSpecific = userSpecific.replace(" ", "+")

    print("Searching ", end=" ")
    for i in range(1, 2):
        print('. . . ', end=" ")
        time.sleep(2)

    webbrowser.open_new("https://google.com/search?q=" + dorkSiteCommand + site + " " + dorkDomainCommand +
                        userSpecific)           # display results in a browser tab

if userInput == 3:
    site = input("Enter the site: ")
    fileType = input("Enter files you want to search: ")

    print("Searching ", end=" ")
    for i in range(1, 2):
        print('. . . ', end=" ")
        time.sleep(2)

    webbrowser.open_new(
        "https://google.com/search?q=" + dorkDomainCommand + "\"report\"" + " " + "(" + v1 + " " + "|" + " " + v2 + " " +
        "|" + " " + v3 + " " + "|" + " " + v4 + " " + "|" +
        " " + v5 + ")" + " " + dorkFileCommand + fileType + " " + dorkUrl + site)

if userInput == 4:
    site = input("Enter the site: ")
    request = 0
    counter = 0

    for results in search("site:" + site + " " "intitle:@gmail.com | Contact"):
        counter = counter + 1                   
        print("[+] ", counter, results)
        time.sleep(0.1)
        request += 1
        if request >= 5:                         #displays 5 results. Limited the results to 5 for now so that it does not take too long.
            break
        data = (counter, results)
        time.sleep(0.1)
      
    webbrowser.open_new("https://google.com/search?q=" + dorkSiteCommand + site + " " + dorkDomainCommand +  "@gmail.com | Contact")
   

if userInput == 5:
    site = input("Enter the site: ")
    request = 0
    counter = 0

    for results in search("site:" + site + " " "inurl:http"):  # still working on it
        counter = counter + 1
        print("[+] ", counter, results)
        time.sleep(0.1)
        request += 1
        if request >= 5:
            break
        data = (counter, results)
        time.sleep(0.1)
