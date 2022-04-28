from googlesearch import search
import webbrowser
import time


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
    print("1. Search for files on site")
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
