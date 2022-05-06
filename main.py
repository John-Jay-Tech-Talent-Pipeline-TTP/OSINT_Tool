from googlesearch import search
import webbrowser
import time
import sys


# uses console or default browser to display results.

#####################################################
# References
#
# https://exposingtheinvisible.org/en/guides/google-dorking/
# https://kit.exposingtheinvisible.org/en/how/google-dorking.html
# https://www.youtube.com/watch?v=u_gOnwWEXiA&ab_channel=NullByte
# https://www.youtube.com/watch?v=sXBLqnAulhQ
#
#########################################################


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
    print(colors.blue + col, end="")
    sys.stdout.flush()
    time.sleep(0.0025)

description = "\n The tool uses advanced searching operators in the Goggle search engine " \
              "to find specfic words or phrases which helps in finding any vulnerable web applications. " \
              "It simplifies Google Dorking commands for the user and provides straightforward anaylsis of the " \
              "information. Different information such as contact information, login credentials, files on " \
              "a website, open ports, vulnerability of a specific website, and many more juicy stuff can " \
              "be found online through google dorking. This tool allows you to be able to access that information " \
              "wihout knowing any google dorking commands or strings.  \n"

for col in description:
    print(colors.magneta + col, end="")
    sys.stdout.flush()
    time.sleep(0.01)

disclaimer = " \n This is for educational purposes and user should use it at their own risk. Some of" \
             " the analysis might not be precise and CAUTION is advised when opening the links found " \
             "through the results. \n\n "

for col in disclaimer:
    print(colors.red + col, end="")
    sys.stdout.flush()
    time.sleep(0.01)

print("\033[1;32;40mHave fun hacking *Hacker music in background*\n\n")


# functions:
def searchContactInfo(site):  # search contact information
    request = 0
    counter = 0

    for results in search("site:" + site + " " "intitle:@gmail.com | Contact"):
        counter = counter + 1
        print("[+] ", counter, results)
        time.sleep(0.1)
        request += 1
        if request >= 5:
            break
        data = (counter, results)
        time.sleep(0.1)


def ComprehensiveContactInfo(site):
    # contact information
    request = 0
    counter = 0
    file.write("Contact Information of site: " + site + "\n")
    file.write("___________________________________________\n")

    for results in search("site:" + site + " " "intitle:@gmail.com | Contact"):
        counter = counter + 1
        file.write(results + "\n")
        time.sleep(0.1)
        request += 1
        if request >= 5:
            break
        data = (counter, results)
        time.sleep(0.1)


def ComprehensiveunsecureDomainsofSites(site):
    request = 0
    counter = 0
    file.write("\n\nHttp domains associated with site: " + site + "\n")
    file.write("_____________________________________________________\n")
    for results in search("site:" + site + " " "inurl:http"):  # still working on it
        counter1 = counter + 1
        file.write(results + "\n")
        time.sleep(0.1)
        request += 1
        if request >= 5:
            break
        data = (counter1, results)
        time.sleep(0.1)


def ComprehensiveShodanAdvancedSearch(site):
    file.write("\n\nInformation associated with site: " + site + "\n")
    file.write("_____________________________________________________\n")
    file.write("https://www.shodan.io/search?query=" + site)


def ComprehensivelookUpOpenPorts(site):
    file.write("\n\nOpen ports associated with site: " + site + "\n")
    file.write("_____________________________________________________\n")
    file.write("https://www.shodan.io/search/facet?query=" +
               site + "&facet=port")


def ComprehensivelookUpBugBountyDB(site):
    file.write("\n\nBugBounty information associated with site: " + site + "\n")
    file.write("_____________________________________________________________\n")
    file.write("https://www.openbugbounty.org//search/?search=" +
               site + "&type=host")


def searchFilesOnSite(site, fileType):  # search files on site
    counter = 0
    request = 0

    print("searching  . . . .", end=" ")
    for results in search("https://google.com/search?q=" + site + " " + dorkFileCommand + fileType):
        counter = counter + 1

        print(counter, results)  # display results in the console
        time.sleep(0.1)  # delay
        request += 1
        if request >= 5:
            break
        data = (counter, results)  # limiting console output
        time.sleep(0.1)

        print("Searching ", end=" ")
        for i in range(1, 2):
            print('. . . .', end=" ")
    time.sleep(0.1)


def searchDomain(site, userSpecific):  # search domains for titles
    userSpecific = userSpecific.replace(" ", "+")

    print("Searching ", end=" ")
    for i in range(1, 2):
        print('. . . ', end=" ")
        time.sleep(2)

    webbrowser.open_new("https://google.com/search?q=" + dorkSiteCommand + site + " " + dorkDomainCommand +
                        userSpecific)  # display results in a browser tab


def unsecureDomainsofSites(site):  # search http Domains of specific sites
    request = 0
    counter = 0

    for results in search("site:" + site + " " "inurl:http"):  # still working on it
        counter = counter + 1
        # and should be displayed via browser if it works
        print("[+] ", counter, results)
        time.sleep(0.1)
        request += 1
        if request >= 5:
            break
        data = (counter, results)
        time.sleep(0.1)


def lookUpAssociateDomains(site):
    request = 0
    counter = 0
    splitSite = site.split(".")

    print("Searching ", end=" ")

    for i in range(1, 2):
        print('. . . ', end=" ")
        time.sleep(2)

    webbrowser.open_new(
        "https://google.com/search?q=" + "site:" + "*.*." + splitSite[0])  # display results in a browser tab


def shodanAdvancedSearch(site):
    print("Searching ", end=" ")
    for i in range(1, 2):
        print('. . . ', end=" ")
        time.sleep(2)

    # display results in a browser tab
    webbrowser.open_new("https://www.shodan.io/search?query=" + site)


def lookUpOpenPorts(site):
    print("Searching ", end=" ")
    for i in range(1, 2):
        print('. . . ', end=" ")
        time.sleep(2)

    webbrowser.open_new("https://www.shodan.io/search/facet?query=" +
                        site + "&facet=port")  # display results in a
    # browser tab


def lookUpBugBountyDB(site):
    print("Searching ", end=" ")
    for i in range(1, 2):
        print('. . . ', end=" ")
        time.sleep(2)

    webbrowser.open_new("https://www.openbugbounty.org//search/?search=" +
                        site + "&type=host")  # display results in a
    # browser tab


# menu
def menu():
    print("1. Search for files on site")
    print("2. Search websites under a domain with a specific word")
    print("3. Search for contact information")
    print("4. Search for sites with http protocol")
    print("5. Look up site associated domains")
    print("6. Shodan advanced search")
    print("7. look up open ports on a site")
    print("8. Look up BugBounty database")
    print("9. Comprehensive website search")


time.sleep(.5)

# dorking commands
dorkSiteCommand = "site:"
dorkFileCommand = "filetype:"
dorkDomainCommand = "intitle:"
dorkUrl = "inurl:"

menu()
print("\n")

# taking user input
userInput = int(input("Choose an option: "))

if userInput == 1:  # search  files on site
    site = input("Enter the site: ")  # site to search
    fileType = input("Enter files you want to search: ")  # files to search
    searchFilesOnSite(site, fileType)

# webbrowser.open_new("https://google.com/search?q=" + dorkSiteCommand + site + " " + dorkFileCommand + fileType)
# uncomment and reformat for it to open up in a new browser tab....

if userInput == 2:  # search domains for titles
    site = input("Enter the site: ")
    userSpecific = input("Specific word or words you want to search: ")
    userSpecific = userSpecific.replace(" ", "+")
    searchDomain(site, userSpecific)

if userInput == 3:  # search contact information on sites
    site = input("Enter the site: ")
    searchContactInfo(site)

if userInput == 4:  # search http Domains of specific country domains
    site = input("Enter the site: ")
    unsecureDomainsofSites(site)

if userInput == 5:  # look up domains associated domains
    site = input("Enter the site: ")
    lookUpAssociateDomains(site)

if userInput == 6:  # Shodan advanced search
    site = input("Enter the site: ")
    shodanAdvancedSearch(site)

if userInput == 7:  # lookup open ports on sites via shodan
    site = input("Enter the site: ")
    lookUpOpenPorts(site)

if userInput == 7:  # look up BugBounty database
    site = input("Enter the site: ")
    lookUpBugBountyDB(site)

if userInput == 9:  # comprehensive search
    print("Comprehensive Search includes: contact info, http protocol,"
          + "site associated domains, shodan advanced websearch, open ports," +
          "and BugBounty database\n")

    site = input("Enter the site: ")
    file = open("Comprehensive Search.txt", "w")

    print("Working . . . . ", end=" ")
    for i in range(1, 5):
        print('\n. . . . . . . . ', end=" ")
        time.sleep(2)

    ComprehensiveContactInfo(site)
    ComprehensivelookUpBugBountyDB(site)
    ComprehensiveShodanAdvancedSearch(site)
    ComprehensivelookUpOpenPorts(site)
    ComprehensiveunsecureDomainsofSites(site)

    print("\nDone. . . . . .")
    file.close()
