import tkinter as tk
import tkinter.font as tkfont
from tkinter import *
from tkinter.ttk import *

root = tk.Tk()

root.title("Text Encryptor-Decryptor")

root.geometry("570x500")
root.resizable(width=FALSE, height=FALSE)
# added
menu= StringVar()
menu.set("Select Any Language")
options = [
    "Caesar Cipher",
    "Rail Fence",
]
drop= OptionMenu(root, menu, *options )
drop.pack()
canvas = tk.Canvas(root,height = 800, width=800, bg="MediumPurple1")
canvas.pack()
bold_font = tkfont.Font(family="Helvetica",size=12,weight="bold")
label1 = tk.Label(root,text= "Enter the Text",width=20,bg="MediumPurple1")
label1.config(font=bold_font)
canvas.create_window(200,100,window=label1)
user_text = tk.Entry(root)
labelk = tk.Label(root,text= "Enter the Keys",width=20,bg="MediumPurple1")
labelk.config(font=bold_font)
canvas.create_window(400,100,window=labelk)
user_text = tk.Entry(root)
canvas.create_window(200,150,window=user_text)
keys = tk.Entry(root)
canvas.create_window(400,150,window=keys)
label2=tk.Label(root,text="Choose an Operation",width=25,bg="MediumPurple1")
label2.config(font=bold_font)
canvas.create_window(300,200,window=label2)
v = tk.IntVar()
def choice():
    x = v.get()
    if(x==1):
        encryption()
    elif(x==2):
        decryption()
label3=tk.Radiobutton(root, text="Encryption",padx = 20, variable=v, value=1,command=choice,bg="black")
label3.config(font=bold_font)
canvas.create_window(150,250,window=label3)
label4=tk.Radiobutton(root, text="Decryption",padx = 20, variable=v, value=2,command=choice,bg="black")
label4.config(font=bold_font)
canvas.create_window(430,250,window=label4)
def encryptRailFence(text, key):
	rail = [['\n' for i in range(len(text))]
				for j in range(key)]
	
	dir_down = False
	row, col = 0, 0
	for i in range(len(text)):

		if (row == 0) or (row == key - 1):
			dir_down = not dir_down

		rail[row][col] = text[i]
		col += 1

		if dir_down:
			row += 1
		else:
			row -= 1

	result = []
	for i in range(key):
		for j in range(len(text)):
			if rail[i][j] != '\n':
				result.append(rail[i][j])
	return("" . join(result))

def decryptRailFence(cipher, key):


	rail = [['\n' for i in range(len(cipher))]
				for j in range(key)]
	

	dir_down = None
	row, col = 0, 0

	for i in range(len(cipher)):
		if row == 0:
			dir_down = True
		if row == key - 1:
			dir_down = False

		rail[row][col] = '*'
		col += 1

		if dir_down:
			row += 1
		else:
			row -= 1

	index = 0
	for i in range(key):
		for j in range(len(cipher)):
			if ((rail[i][j] == '*') and
			(index < len(cipher))):
				rail[i][j] = cipher[index]
				index += 1
		
	result = []
	row, col = 0, 0
	for i in range(len(cipher)):

		if row == 0:
			dir_down = True
		if row == key-1:
			dir_down = False
			

		if (rail[row][col] != '*'):
			result.append(rail[row][col])
			col += 1
		if dir_down:
			row += 1
		else:
			row -= 1
	return("".join(result))
def encryption():
    d = menu.get()
    if(d==options[0]) :
        plain_text = user_text.get()
        key = int(keys.get())
        cipher_text = ""
        for i in range(len(plain_text)):
            letter = plain_text[i]
            if(letter.isupper()):
                cipher_text+=chr((ord(letter)+key-65)%26+65)
            else:
                cipher_text+=chr((ord(letter)+key-97)%26+97)
    else :
        plain_text = user_text.get()
        key = int(keys.get())
        cipher_text = encryptRailFence(plain_text, key)
    label6 =tk.Label(root,text=cipher_text,width=20,bg="black")
    label6.config(font=bold_font)
    canvas.create_window(300,350,window=label6)
def decryption():
    d = menu.get()
    if(d==options[0]) :
        cipher_text = user_text.get()
        key =int(keys.get())
        plain_text = ""
        for i in range(len(cipher_text)):
            letter = cipher_text[i]
            if(letter.isupper()):
                plain_text+=chr((ord(letter)-key-65)%26+65)
            else:
                plain_text+=chr((ord(letter)-key-97)%26+97)
    else :
        cipher_text = user_text.get()
        key = int(keys.get())
        plain_text = decryptRailFence(cipher_text, key)
    label6 =tk.Label(root,text=plain_text,width=20,bg="black")
    label6.config(font=bold_font)
    canvas.create_window(300,350,window=label6)
label7 =tk.Label(root,text="Converted Text ",width=20,bg="MediumPurple1")
label7.config(font=bold_font)
canvas.create_window(300,300,window=label7)
root.mainloop()