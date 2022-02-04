import pyfiglet
import sys
import socket
from datetime import datetime
   
ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)

# Defining a target
if len(sys.argv) == 2:
      
    # translate hostname to IPv4
    target = socket.gethostbyname(sys.argv[1]) 
    print(target)
else:
    print("Invalid ammount of Argument")

# Enter target
target = input("Input target address: ")
target = socket.gethostbyname(target)

# Use sys. stdout to redirect print output to a text file

#    sys. stdout = open("test.txt", "w")
#    print("Hello World")
#    sys. stdout.

## sys.stdout = open("PortScanner.txt","w")
# Add Banner 
print("-" * 50)
print("Scanning Target: " + target)
print("Scanning started at:" + str(datetime.now()))
print("-" * 50)

try:
    # will scan ports between 1 to 65,535
    for port in range(1,500):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        # returns an error indicator
        result = s.connect_ex((target,port))
        if result ==0:
            print("Port {} is open".format(port))
        s.close()

          
except KeyboardInterrupt:
        print("\n Exitting Program !!!!")
        sys.exit()
except socket.gaierror:
        print("\n Hostname Could Not Be Resolved !!!!")
        sys.exit()
except socket.error:
        print("\ Server not responding !!!!")
        sys.exit()

## sys.stdout