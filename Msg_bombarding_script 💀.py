import pyautogui as auto
import time 

while True:
    auto.write("Hello, world!")
    auto.press('enter')
    time.sleep(1)
    
# The code will bombard any massage box and would make system press on enter button 
# continously (Syccesfull ran of fedora after maneging dependencies)

# requied dependencie to work 
# sudo dnf install python3-devel python3-pip python3-tkinter xorg-x11-server-Xvfb
# pip install pyautogui
# pip install Pillow pymsgbox PyScreeze mouseinfo
# change the package manager depending on the distro and for windows
# it should run ... 

# run it in python shell .. exicution through python3 command or in any code editor might not work ..
