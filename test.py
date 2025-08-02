import os
import sys

print("UWU")
print("owo")

rooms = "grasp of many"

print('there is a \"' + rooms + '\" enemy in here!')


while True:
        dave = str(input("test input here: "))

        if dave == "yes":
                print("uwu") 
                continue
        
        elif dave == "no":
                os.execv(sys.executable, ['python'] + sys.argv)

        else:
                print("what do want from me")
                continue