﻿#!/usr/bin/python																# Allows the use of Non-ASCII characters (password) in app
# -*- coding: utf-8 -*-
 
from CC import *																# pack() is for stacking, while place() is for a more
from Tkinter import *															# accurate placing of widgets. grid() is for tables
from profilePageGUI import profilePageGUI
from PIL import ImageTk, Image
import os, sys, glob, time

defaultEntryStyle = ("Tahoma", 12)												# Initial font settings for styling
defaultLabelStyle = ("Tahoma", 9)
defaultCreateStyle = ("Tahoma", 14)
defaultLogoStyle = ("Verdana", 18)
signatureColor = "orange"														# Shortcut labels for custom color styling
toplayerColor = "#555555"
backgroundColor = "#EEEEEE"

a=-0.05																			# Adjuster for widget's y-value placement

class loginPageGUI(Frame):														# The login GUI class Interface!
	def __init__(self, master=None):	
		Frame.__init__(self, master)
		self.createWidgets()
		
	def createWidgets(self):
		self.master.title("Welcome to Caffy!")
		topLayer = Frame(self, height=80, width=1000, bg=toplayerColor)			# Code here for the Log-in classes
		topLayer.pack()		
		Label(topLayer, text="Username", fg="#FFF", bg=toplayerColor, font=defaultLabelStyle).place(anchor=CENTER, relx=0.5379, rely=0.28)	# Labels for the entry fields
		Label(topLayer, text="Password", fg="#FFF", bg=toplayerColor, font=defaultLabelStyle).place(anchor=CENTER, relx=0.7163, rely=0.28)	# Labels for the entry fields	
		self.usernameVariable = StringVar()
		self.usernameInput = Entry(topLayer, fg=toplayerColor, width=17, textvariable=self.usernameVariable, font=defaultEntryStyle, relief=FLAT)	# Entry field for the username
		self.usernameInput.place(anchor=CENTER,relx=0.59, rely=0.59)
		self.usernameInput.focus()												# Puts the cursor automatically at the user_name field
		self.passwordVariable = StringVar()
		self.passwordInput = Entry(topLayer, fg=toplayerColor, width=17, show="•", textvariable=self.passwordVariable, font=defaultEntryStyle, relief=FLAT)	# Entry field for the password
		self.passwordInput.place(anchor=CENTER, relx=0.77, rely=0.59)
		Label(topLayer, text="caffy", font=("Verdana", 28), justify=LEFT, bg=toplayerColor, fg="orange").place(anchor=W, relx=0.08, rely=0.5)
		self.coffcup = Label(topLayer, text="☕", font=("Tahoma", 28), justify=LEFT, bg=toplayerColor, fg="#FFFFFF")
		self.coffcup.place(anchor=W, relx=0.175, rely=0.48)
		self.verifyLoginLabel = Label(topLayer, text="", fg="orange", bg=toplayerColor, font=defaultLabelStyle) 	# For warning purposes of login entries
		self.verifyLoginLabel.place(anchor=E, relx=0.5, rely=0.59)
		self.coffcup.bind("<Enter>", lambda f: self.coffcup.config(fg="orange"))
		self.coffcup.bind("<Leave>", lambda f: self.coffcup.config(fg="white"))
		
		midLayer = Frame(self, width=1000, height=490)		# Code here for the CREATE class
		midLayer.pack()
		
		canvasSky = Canvas(midLayer, width=1000, height=490, highlightthickness=0, bg=backgroundColor)
		canvasSky.pack()
		sky = ImageTk.PhotoImage(file="GUIE\\LoginSky.png")
		canvasSky.create_image(500, 245, image=sky)
		canvasSky.image = sky								#Reference to image so that garbage wont be collected
		
		layer1 = Frame(midLayer, width=379, height=40, bg="#FFFFFF")
		layer1.place(anchor=CENTER, relx=0.7, rely=0.3+a)
		layer2 = Frame(midLayer, width=379, height=40, bg="#FFFFFF")
		layer2.place(anchor=CENTER, relx=0.7, rely=0.45+a)
		layer3 = Frame(midLayer, width=379, height=40, bg="#FFFFFF")
		layer3.place(anchor=CENTER, relx=0.7, rely=0.6+a)
		self.newUsernameVariable = StringVar()
		self.newUsernameInput = Entry(layer1, fg=toplayerColor, width=35, textvariable=self.newUsernameVariable, font = defaultCreateStyle, relief=FLAT)
		self.newUsernameInput.place(anchor=CENTER, relx=0.5, rely=0.5+a)		
		self.newPasswordVariable = StringVar()
		self.newPasswordInput = Entry(layer2, fg=toplayerColor, width=35, show="•", textvariable=self.newPasswordVariable, font = defaultCreateStyle, relief=FLAT)
		self.newPasswordInput.place(anchor=CENTER, relx=0.5, rely=0.5+a)
		self.newPasswordVerifyVariable = StringVar()
		self.newPasswordVerifyInput = Entry(layer3, fg=toplayerColor, width=35, show="•", textvariable=self.newPasswordVerifyVariable, font = defaultCreateStyle, relief=FLAT)
		self.newPasswordVerifyInput.place(anchor=CENTER, relx=0.5, rely=0.5+a)
		Label(midLayer, text="Pick a username:", bg=backgroundColor, fg=toplayerColor).place(anchor=W, relx=0.508, rely=0.23+a)
		Label(midLayer, text="Create a password:", bg=backgroundColor, fg=toplayerColor).place(anchor=W, relx=0.508, rely=0.38+a)
		Label(midLayer, text="Reenter your password:", bg=backgroundColor, fg=toplayerColor).place(anchor=W, relx=0.508, rely=0.53+a)
		Label(midLayer, text="Take a    break!\nSign up!", font=("Tahoma", 35), justify=LEFT, bg=backgroundColor, fg=toplayerColor).place(anchor=W, relx=0.08, rely=0.345+a)
		self.coffcup2 = Label(midLayer, text="☕", font=("Tahoma", 35), justify=LEFT, bg=backgroundColor, fg=toplayerColor)
		self.coffcup2.place(anchor=W, relx=0.23, rely=0.28+a)
		self.coffcup2.bind("<Enter>", lambda f: self.coffcup2.config(fg="orange"))
		self.coffcup2.bind("<Leave>", lambda f: self.coffcup2.config(fg=toplayerColor))
		Label(midLayer, text="Caffy lets you connect and share with\nfriends from around the corner.", font=("Tahoma", 15), justify=LEFT, bg=backgroundColor, fg=toplayerColor).place(anchor=W, relx=0.08, rely=0.58+a)
		Label(midLayer, text="By signing up, you agree with our Terms and Conditions.", font=("Tahoma", 9), justify=RIGHT, bg=backgroundColor, fg="#999999").place(anchor=E, relx=0.8956, rely=0.7+a)
		self.verifyCreateLabel = Label(midLayer, text="", bg=backgroundColor, justify=LEFT)		# Initialization of the create warnings
		self.verifyCreateLabel.place(anchor=W, relx=0.509, rely=0.75)		
		
		bottomLayer = Frame(self, width=1000, height=30, bg=toplayerColor)		# Code here for the extra details
		bottomLayer.pack()
		Label(bottomLayer, text="Thank you for choosing Caffy™ | Copyright © 2014. All rights are reserved", fg="#FFFFFF", bg=toplayerColor, font=("Tahoma", 8)).place(anchor=CENTER, relx=0.5, rely=0.5)

class notifSystemGUI(Frame):													# The TOPLAYER GUI. Included here are mainly the Notifications bar, along with the Logout / Profile / Home Navigation Buttons
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.pack()
		self.createWidgets()
		
	def createWidgets(self):
		notifLayer = Frame(self, width=1000, height=50, bg=toplayerColor)
		notifLayer.pack(anchor=NW)
		Label(notifLayer, text="caffy", font=defaultLogoStyle, bg=toplayerColor, fg="orange").place(anchor=CENTER, relx=0.2, rely=0.5)
		self.coff = Label(notifLayer, text="☕", font=defaultLogoStyle, bg=toplayerColor, fg="#FFFFFF")
		self.coff.place(anchor=CENTER, relx=0.245, rely=0.48)
		self.coff.bind("<Enter>", lambda f: self.coff.config(fg="orange"))
		self.coff.bind("<Leave>", lambda f: self.coff.config(fg="white"))
		
class homePageGUI(Frame):														# This is the GUI for the Newsfeed sections
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.place(in_=master)
		self.createWidgets()
	
	def createWidgets(self):
		homepageMainWindow = Frame(self, width=1000, height=550, bg="blue")
		homepageMainWindow.pack()
		Label(homepageMainWindow, text="YOU JUST GOT CAFFIED!", font=("Tahoma", 30, "bold"), fg="#000000").place(anchor=CENTER, relx=0.5, rely=0.5)

class Singleton:																# Singleton Design Pattern retrieved from
    __single = None																# Python Help Manual Website: http://www.python.org/workshops/1997-10/proceedings/savikko.html
    def __init__(self):
        if Singleton.__single:
            raise Singleton.__single
        Singleton.__single = self  
		
class activePageGUI(Frame, Singleton):											# This is basically a SINGLETON class or maybe a FACADE for containing all the active sessions of a user... Included: Profile Page, Newspage, and everything else while logged in.
	def __init__(self, master=None):
		Frame.__init__(self, master)
		Singleton.__init__(self)

		self.topLayerObject = notifSystemGUI(self)

		container2 = Frame(self, width=1000, height=550)
		container2.pack()

		self.profilePageObject = profilePageGUI(container2)		
		self.homePageObject = homePageGUI(container2)

		canvasActiveShadow = Canvas(width=1000, height=550, highlightthickness=0)
		canvasActiveShadow.place(in_=container2)
		activeShadow = ImageTk.PhotoImage(file="GUIE\\activePageShadow.png")
		canvasActiveShadow.create_image(500, 275, image=activeShadow)
		canvasActiveShadow.image = activeShadow
				
		self.profilePageObject.lift()
		self.createWidgets()
			
	def createWidgets(self):
		pass		

class navClass(Frame):															# A GUI that combines the Login and Active Windows. Basically another Faҫade design pattern. Called navClass because of navigation (button fxns)
	def __init__(self, master=None):
		Frame.__init__(self, master)
		
		self.val = validation()													# Initial functions for the verifications
		self.loginCC = CC()
		self.createCC = CC()
		self.cre = creation()

		container = Frame(self, width=1000, height=600)							# Frame for all the to-be-children pages
		container.pack()	

		self.activePageObject = activePageGUI()
		self.activePageObject.place(in_=container)

		self.loginPageObject = loginPageGUI()
		self.loginPageObject.place(in_=container)
		self.loginPageObject.lift()

		#`self.activePageObject.lift()											# Displays first ever page, which is the login page		

		self.pack()
		self.createWidgets()
		
	def createWidgets(self):			
		
		self.loginButton = Button(self.loginPageObject, text="Log In", width=7, height=1, font=("Tahoma", 9, "bold"), relief=FLAT, fg="#FFFFFF", bg=signatureColor, command=self.verifyLogin)
		self.loginButton.place(anchor=CENTER, relx=0.904, rely=0.0786)			# Button of the LoginPage (click to verify entries)
		
		self.loginPageObject.usernameInput.bind("<Return>", lambda event: self.loginButton.invoke())	#Allows the use of the Enter key when loggin in
		self.loginPageObject.passwordInput.bind("<Return>", lambda event: self.loginButton.invoke())
		
		self.createButton = Button(self.loginPageObject, text="Sign Me Up!", width=12, font=("Tahoma", 13, "bold"), relief=FLAT, fg="#FFFFFF", bg="#52A41D", command=self.verifyCreate)
		self.createButton.place(anchor=CENTER, relx=0.82, rely=0.75)
		
		self.loginPageObject.newUsernameInput.bind("<Return>", lambda event: self.createButton.invoke())	#Allows the use of the Enter key when creating accounts
		self.loginPageObject.newPasswordInput.bind("<Return>", lambda event: self.createButton.invoke())
		self.loginPageObject.newPasswordVerifyInput.bind("<Return>", lambda event: self.createButton.invoke())
			
	def eraseContents(self, *args):												# Function allows unlimited number of arguments by the *args keyword
		for x in args:															# The *args is a tuple, so every element in it must be iterated
			x.delete(0, END)													# to delete the value of all the 3 Create Entries
	
	def verifyLogin(self):														# Method executed whenever "Log In" button is pressed
		responses=["USERNAME IS BLANK", "PASSWORD IS BLANK", "ACCOUNT DOES NOT EXIST", "INVALID PASSWORD"]
		self.loginCC.set_name(self.loginPageObject.usernameVariable.get())				# Accessors!
		self.loginCC.set_password(self.loginPageObject.passwordVariable.get())
		self.answer = self.val.guiv(self.loginCC.get_name(), self.loginCC.get_password())
		if self.answer in responses:										# If return value from imported class CC is inside the list,		
			self.loginPageObject.verifyLoginLabel.config(text=self.answer)				# display the possible warnings and perform some formatting actions like clear the entry field:
			if self.answer == responses[0]:
				self.eraseContents(self.loginPageObject.passwordInput)
				self.loginPageObject.usernameInput.focus()
			elif self.answer == responses[1]:
				self.loginPageObject.passwordInput.focus()
			elif self.answer == responses[2]:
				self.eraseContents(self.loginPageObject.usernameInput, self.loginPageObject.passwordInput)
				self.loginPageObject.usernameInput.focus()
			else:
				self.eraseContents(self.loginPageObject.passwordInput)
				self.loginPageObject.passwordInput.focus()
		else:
			self.loginButton.flash()
			self.activePageObject.lift()												# otherwise, if entries are correct, execute & display the home page
	
	def verifyCreate(self):	
		def waitLabel():																# For removing the SUCCESSFUL message after 1 second
			self.loginPageObject.verifyCreateLabel.config(text="")			
		responses = ["USERNAME IS BLANK", "PASSWORD REQUIRED", "PLEASE RETYPE THE PASSWORD", "USERNAME IS ALREADY TAKEN", "RETYPE YOUR PASSWORD\nCORRECTLY", "PASSWORD MUST HAVE AT LEAST\n6 CHARACTERS"]
		self.createCC.set_name(self.loginPageObject.newUsernameVariable.get())
		self.createCC.set_password(self.loginPageObject.newPasswordVariable.get())
		self.answer = self.cre.guic(self.createCC.get_name(), self.createCC.get_password(), self.loginPageObject.newPasswordVerifyVariable.get())		# Assign the return value of this very long function into variable answer! (actually, self.answer)
		if self.answer in responses:																									# If the answer is included in the list above,
			self.loginPageObject.verifyCreateLabel.config(text=self.answer, fg="red", font=("Tahoma", 9, "bold"))
			if self.answer == responses[0] or self.answer == responses[3]:											# Display that message from the list, then format some widgets
				self.eraseContents(self.loginPageObject.newUsernameInput, self.loginPageObject.newPasswordInput, self.loginPageObject.newPasswordVerifyInput)
				self.loginPageObject.newUsernameInput.focus()
			elif self.answer == responses[1]:
				self.eraseContents(self.loginPageObject.newPasswordVerifyInput)
				self.loginPageObject.newPasswordInput.focus()
			elif self.answer == responses[2]:
				self.loginPageObject.newPasswordVerifyInput.focus()
			elif self.answer == responses[5]:
				self.eraseContents(self.loginPageObject.newPasswordInput, self.loginPageObject.newPasswordVerifyInput)
				self.loginPageObject.newPasswordInput.focus()
			else:
				self.eraseContents(self.loginPageObject.newPasswordVerifyInput)
		else:																																# Otherwise, if create entries are valid, proceed to some formatting, then create the database! YAY!
			self.createButton.flash()
			self.cre.create()
			self.eraseContents(self.loginPageObject.newUsernameInput, self.loginPageObject.newPasswordInput, self.loginPageObject.newPasswordVerifyInput, self.loginPageObject.usernameInput)
			self.loginPageObject.usernameInput.focus()
			self.loginPageObject.verifyLoginLabel.config(text="")
			self.loginPageObject.verifyCreateLabel.config(text="SUCCESSFUL! YOU CAN NOW\nLOG-IN!", fg="#52A41D", font=("Tahoma", 9, "bold"))
			self.loginPageObject.verifyCreateLabel.after(1000, waitLabel)					# An event delayer for changing the label of SUCCESSFUL CREATIONS
			
Window = Tk()        		 													# Creates an empty window
Main = navClass()
Window.geometry('1000x600+170+80')												# Set dimensions to 1000x600 pos @ screen center
Window.resizable(0,0)			 												# Does not resize the window, ever 	
Window.wm_iconbitmap('GUIE\\CoffeeCup.ico')										# Adds a little mug icon over the top left corner
Window.mainloop()																# Executes code above in a loop

os.remove('CC.pyc')																# Removes the temporary files inside the (" ")
#os.remove('Main.pyc')															# (For Git uploading purposes only)