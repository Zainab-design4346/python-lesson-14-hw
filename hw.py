import os
sd = input("Shutdown computer? (yes or no):")
if sd == 'no':
    exit()
else:
    os.system("shutdown /s /t 1")