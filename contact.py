import time
from googlesearch import search



def main():
	dork = input("Enter the website: ")
	print ("1. Search for contact information")
	print ("2. Search for http protocol")
#	time.sleep(.5)
	
	choice = int(input("Choose 1 or 2: "))
	
	
	if choice == 1:
		requ = 0
		counter = 0
		for results in search("site:" + dork + " " "intitle:@gmail.com | Contact"):
			counter = counter + 1
			print ("[+] ", counter, results)
			time.sleep(0.1)
			requ += 1
			if requ >= 5:
				break
			data = (counter, results)
		
			time.sleep(0.1)
	if choice == 2:
		requ = 0
		counter = 0
		for results in search("site:" + dork + " " "inurl:http"):   #still working on it
			counter = counter + 1
			print ("[+] ", counter, results)
			time.sleep(0.1)
			requ += 1
			if requ >= 5:	
				break
			data = (counter, results)
			time.sleep(0.1)
			
main()

	