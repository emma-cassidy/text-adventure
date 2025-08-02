import os
import sys

print("UWU")
print("owo")





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