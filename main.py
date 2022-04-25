import webbrowser
import time


# site:ug.edu.gh " " filetype:pdf
# uses default browser by default.
# webbrowser.get('C:/Users/PrxncE _ LixH/Tor Browser/Browser/firefox.exe %s').open_new(
# "https://google.com/search?q=" + dorkSiteCommand + site + " " + dorkDomainCommand + userSpecific)

def menu():
    print("1. Search for files on site")
    print("2. Search websites under a domain with a specific word")


dorkSiteCommand = "site:"
dorkFileCommand = "filetype:"
dorkDomainCommand = "intitle:"

menu()
userInput = int(input("Choose an option: "))

if userInput == 1:
    site = input("Enter the site: ")
    fileType = input("Enter files you want to search: ")

    print("Searching ", end=" ")
    for i in range(1, 2):
        print('. . . ', end=" ")
        time.sleep(2)

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
                        userSpecific)
