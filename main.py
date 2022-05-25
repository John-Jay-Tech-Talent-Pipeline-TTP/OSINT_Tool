from googlesearch import search
import webbrowser
import time
import os
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
    time.sleep(0.0005)

description = "\n The tool uses advanced searching operators in the Google search engine " \
              "to find specific words or phrases which helps in finding any vulnerable web applications. " \
              "It simplifies Google Dorking commands for the user and provides straightforward anaylsis of the " \
              "information. Different information such as contact information, login credentials, files on " \
              "a website, open ports, vulnerability of a specific website, and many more vulnerable information can " \
              "be found online through google dorking. This tool allows you to be able to access that information " \
              "wihout knowing any google dorking commands or strings.  \n"

for col in description:
    print(colors.magneta + col, end="")     # Change text color


disclaimer = " \n This is for educational purposes and user should use it at their own risk. Some of" \
             " the analysis might not be precise due to constant changing of websites and CAUTION is advised when opening the links found " \
             "through the results. \n\n "

for col in disclaimer:
	print(colors.red + col, end="")

print(
    "\033[1;32;40mChoose from 1-8 for specific information or choose 9 for comprehensive search ."
)


# functions:
def searchContactInfo(site):  # Search contact information
	request = 0               # Count the amount of resutls
	counter = 0
	for results in search("site:" + site + " " "intitle:@gmail.com | Contact"):
		counter = counter + 1
		print("[+] ", counter, results)
		time.sleep(0.1)
		request += 1
		if request >= 5:         # Limit the result to 5 
			break
		data = (counter, results)
		time.sleep(0.1)
		
	if request == 0:               # If no results pop up, print out error           
		print(
			"\nnothing found. Please check if you entered a valid website.\n")
			
def ComprehensiveContactInfo(site):                                      # contact information
	request = 0
	counter = 0
	file.write("Contact Information of site: " + site + "\n")                     # Creates a header for contact in the text file 
	file.write("___________________________________________\n")
	
	for results in search("site:" + site + " " "intitle:@gmail.com | Contact"):   # Searches for webpages with gmail.com and contact
		counter = counter + 1
		file.write(results + "\n")                                                # Stores the results in a text file
		time.sleep(0.1)
		request += 1
		if request >= 5:
			break
		data = (counter, results)
		time.sleep(0.1)
		
	if request == 0:
		print(
			"\nnothing found. Please check if you entered a valid website.\n")
			
def ComprehensiveunsecureDomainsofSites(site):
	request = 0
	counter = 0
	file.write("\n\nHttp domains associated with site: " + site + "\n")             
	file.write("_____________________________________________________\n")
	for results in search("site:" + site + " "             # Websites with http instead of https 
				"inurl:http"):                   # Http are unsecure websites
		counter1 = counter + 1
		file.write(results + "\n")
		time.sleep(0.1)
		request += 1
		if request >= 5:
			break
		data = (counter1, results)
		time.sleep(0.1)
		
	if request == 0:
		print(
			"\nnothing found. Please check if you entered a valid website.\n")
			
def ComprehensiveShodanAdvancedSearch(site):
	file.write("\n\nInformation associated with site: " + site + "\n")           
	file.write("_____________________________________________________\n")
	file.write("https://www.shodan.io/search?query=" + site)              # Includes the google dorking command for shodan search in the text file 

def ComprehensivelookUpOpenPorts(site):
	file.write("\n\nOpen ports associated with site: " + site + "\n")
	file.write("_____________________________________________________\n")
	file.write("https://www.shodan.io/search/facet?query=" + site +
			"&facet=port")          # Includes open port links in the text file
			
def ComprehensivelookUpBugBountyDB(site):
	file.write("\n\nBugBounty information associated with site: " + site + "\n")
	file.write("_____________________________________________________________\n")
	file.write("https://www.openbugbounty.org//search/?search=" + site +
		"&type=host")                          # Include link to the results of a search done on openbugbounty
		
def searchFilesOnSite(site, fileType):  # search files on site
	counter = 0
	request = 0
	
	print("searching  . . . .", end=" ")
	for results in search("https://google.com/search?q=" + site + " " + dorkFileCommand + fileType):
		counter = counter + 1
		
		print(counter, results)  # Display results in the console
		time.sleep(0.1)  # Delay
		request += 1
	
		if request >= 5:
			break
		data = (counter, results)  # Limiting console output
		time.sleep(0.1)
	
		print("Searching ", end=" ")
		for i in range(1, 2):
			print('. . . .', end=" ")
	time.sleep(0.1)
	
def searchDomain(site, userSpecific):  # Search domains for titles
	userSpecific = userSpecific.replace(" ", "+")
	
	print("Searching ", end=" ")
	for i in range(1, 2):
		print('. . . ', end=" ")
		time.sleep(2)
		webbrowser.open_new("https://google.com/search?q=" + 
		dorkSiteCommand + site + " " + dorkDomainCommand + userSpecific)  # Display results in a browser tab
		
def unsecureDomainsofSites(site):  # search http Domains of specific sites
	request = 0
	counter = 0
	
	for results in search("site:" + site + " " "inurl:http"):  
		counter = counter + 1
		# Displays results in browser if it works 
		print("[+] ", counter, results)
		time.sleep(0.1)
		request += 1
		if request >= 5:
			break
		data = (counter, results)
		time.sleep(0.1)
	
	if request == 0:
		print("\nnothing found. Please check if you entered a valid website.\n")
	
def lookUpAssociateDomains(site):  # Function for domains
	request = 0
	counter = 0
	splitSite = site.split(".")
	print("Searching ", end=" ")

	for i in range(1, 2):
		print('. . . ', end=" ")
		time.sleep(2)
	webbrowser.open_new("https://google.com/search?q=" + "site:" + "*.*." + splitSite[0])  # Display results in a browser tab
	
def shodanAdvancedSearch(site):       # Function for shodan search 
	print("Searching ", end=" ")
	for i in range(1, 2):
		print('. . . ', end=" ")
		time.sleep(2)
		
	# Display results in a browser tab
	webbrowser.open_new("https://www.shodan.io/search?query=" + site)
	
def lookUpOpenPorts(site):           # Function for open ports in shodan search 
	print("Searching ", end=" ")
	for i in range(1, 2):
		print('. . . ', end=" ")
		time.sleep(2)
		
	webbrowser.open_new("https://www.shodan.io/search/facet?query=" + site + "&facet=port")  # Display results in a browser tab 
	
def lookUpBugBountyDB(site):           # Function for OpenBugBounty
	print("Searching ", end=" ")
	for i in range(1, 2):
		print('. . . ', end=" ")
		time.sleep(2)
		
	webbrowser.open_new("https://www.openbugbounty.org//search/?search=" + site + "&type=host")  # Display results in a browser tab 
	
# Menu. The options are printed out
def menu():
	print("\n")
	print("1. Search for files on site")
	print("2. Search websites under a domain with a specific word")
	print("3. Search for contact information")
	print("4. Search for sites with http protocol")
	print("5. Look up site associated domains")
	print("6. Shodan advanced search")
	print("7. Look up open ports on a site")
	print("8. Look up BugBounty database")
	print("9. Comprehensive website search")
	
time.sleep(.5)

# Dorking commands
dorkSiteCommand = "site:"
dorkFileCommand = "filetype:"
dorkDomainCommand = "intitle:"
dorkUrl = "inurl:"

menu()
print("\n")
while True:
	try:           # Infinite loop if invalid characters are chosen 
		userInput = int(input("Choose an option: "))          # Taking user input
		if userInput not in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9):
			raise ValueError                              
		while True:			# Another loop to when the correct input are taken 
			if userInput == 1:  # Search  files on site
				site = input("Enter the site: ")  # Site to search
				fileType = input("Enter files you want to search: ")  # Files to search
				searchFilesOnSite(site, fileType)
				menu()
				userInput = int(input("Choose another option or enter 0 to quit: "))
				# Webbrowser.open_new("https://google.com/search?q=" + dorkSiteCommand + site + " " + dorkFileCommand + fileType)
				# Uncomment and reformat for it to open up in a new browser tab....
			elif userInput == 2:  # Search domains for titles
				site = input("Enter the site: ")
				userSpecific = input("Specific word or words you want to search: ")		
				userSpecific = userSpecific.replace(" ", "+")
				searchDomain(site, userSpecific)
				menu()
				userInput = int(input("Choose another option or enter 0 to quit: "))

			elif userInput == 3:  # Search contact information on sites
				site = input("Enter the site: ")
				searchContactInfo(site)
				menu()
				userInput = int(input("Choose another option or enter 0 to quit: "))

			elif userInput == 4:  # Search http Domains of specific country domains
				site = input("Enter the site: ")
				unsecureDomainsofSites(site)
				menu()
				userInput = int(input("Choose another option or enter 0 to quit: "))
				
			elif userInput == 5:  # Look up domains associated domains
				site = input("Enter the site: ")
				lookUpAssociateDomains(site)
				menu()
				userInput = int(input("Choose another option or enter 0 to quit: "))
				
			elif userInput == 6:  # Shodan advanced search
				site = input("Enter the site: ")
				shodanAdvancedSearch(site)
				menu()
				userInput = int(input("Choose another option or enter 0 to quit: "))
				
			elif userInput == 7:  # Lookup open ports on sites via shodan
				site = input("Enter the site: ")
				lookUpOpenPorts(site)
				menu()
				userInput = int(input("Choose another option or enter 0 to quit: "))
				
			elif userInput == 8:  # Look up BugBounty database
				site = input("Enter the site: ")
				lookUpBugBountyDB(site)
				menu()
				userInput = int(input("Choose another option or enter 0 to quit: "))
				
			elif userInput == 9:  # Comprehensive search
				print("Comprehensive Search includes: contact info, http protocol," +
				"site associated domains, shodan advanced websearch, open ports," +
				"and BugBounty database\n")
				
				site = input("Enter the site: ")
				userFile = input("Enter a name for your file: ")
				userFile = userFile + ".txt"
				
				check = os.path.exists(userFile)   # Checks if the file name already exists
				
				if check:             
					print("Directory contains same file name. Consider a different name. \n")
					userFile = input("Enter a different name for your file: ")
					userFile = userFile + ".txt"         # Gives option to change the file name if the filename already exists
					
				file = open(userFile, "w") 
				
				print("Working . . . . ", end=" ")
				for i in range(1, 5):
					print('\n. . . . . . . . ', end=" ")
					time.sleep(2)
					
				ComprehensiveContactInfo(site)               # Calls out the functions and prints the results in the comprehensive search text file
				ComprehensivelookUpBugBountyDB(site)
				ComprehensiveShodanAdvancedSearch(site)
				ComprehensivelookUpOpenPorts(site)
				ComprehensiveunsecureDomainsofSites(site)
				file.close()
				print("\nDone. . . . . .")
				break					# Closes the program when comprehensive search is done 
				
			elif userInput == 0:                            # Closes program when entered 0 
				print("\nClosing Program. . . . . .")
				break                                   # Stops the function 
		break							# Stops the loop 
	except ValueError:       # Print specific text when ValueError occurs
		print("\033[1;31;40m\nSorry, that is not one of the options. Please try again or enter '0' to exit.\033[1;32;40m\n"
		)
		
	
	

