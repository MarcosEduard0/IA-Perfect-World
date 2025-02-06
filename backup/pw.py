from tkinter import *
import webbrowser
import time, datetime
import re
import base64
 
 
 
open_icon = open("pw.ico","rb") #pw.icon is the icon you want to put in
b64str = base64.b64encode(open_icon.read()) #Read in base64 format
open_icon.close()
write_data = "img=%s" % b64str
f = open("img.py","w+") #Write the data read above into the img array of qq.py
f.write(write_data)
f.close() 