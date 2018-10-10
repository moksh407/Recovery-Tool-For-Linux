#!/usr/bin/python

import Tkinter
import tkFileDialog
import os
import tkMessageBox
import getpass

username = getpass.getuser()

Tkinter.Tk().withdraw() # Close the root window

result = tkMessageBox.askyesno('Recovery Tool for Linux',"Welcome!\nWould you like to start recovering JPEGs?")

if result == True:
                 fileName = tkFileDialog.askopenfilename(initialdir = "/home/"+username+"/",title="Select Image File",filetypes = ( ("Image Files","*.raw"),("All Files","*.*") ))

                 if fileName:
                            os.system("./a.out " + fileName)
                            os.system("mkdir ~/Desktop/recovered_jpegs")
                            os.system("mv ./*.jpg ~/Desktop/recovered_jpegs")
                            tkMessageBox.showinfo('Success',"JPEGs recovered successfully!!\nLocation of recovered JPEGs ~/Desktop/recovered_jpegs\nThank you for using Recovery Tool.\nWe hope you like it.")

                 else:
                     tkMessageBox.showinfo('Message',"File Not selected or found!")

else:
     tkMessageBox.showinfo('Message',"Thank you for using Recovery Tool!\nHope to see you next time!")
