from tkinter import * #imports the window
from tkinter.ttk import * #imports the combo box class
from tkinter import Menu #imports the menu class
from tkinter import messagebox #imports the message box class

#from temperature_converter import Converter

window = Tk()
window.title("Temperature Converter")
window.geometry("675x200")

def clickedexit():
    exit()
"""Menu is used to create the menu tabs"""
menu = Menu(window)
new_item = Menu(menu,tearoff = 0)
new_item.add_command(label='Exit', command = clickedexit)
#new_item.add_separator()
menu.add_cascade(label = 'File', menu = new_item)
window.config(menu = menu)

def clickedabout():
    messagebox.showinfo("about temperature converter", "check out more of my apps at: \
https://github.com/davidgbarron")
    
menu2 = Menu(window)
new_item = Menu(menu,tearoff = 0)
new_item.add_command(label='About',command = clickedabout)
#new_item.add_separator()
#new_item.add_command(label='Edit')
menu.add_cascade(label = 'Help', menu = new_item)
window.config(menu = menu)
#combo = Combobox(window)
#combo['values'] = (1,2,3,4,5)
#combo.current(0)
#combo.grid(column = 0, row=0)
"""Label is used to create Labels in text"""
lbl = Label(window, text="                  Temperature Converter",font = ("Arial Bold", 20))
lbl.grid(column = 0, row =0)

cellbl = Label(window, text='celsius to fahrenheit',font = ("Arial", 16))
cellbl.grid(column =0, row = 2)

cresultlbl = Label(window, text = "", font = ("Arial", 16))
cresultlbl.grid(column = 0, row = 4)

spacelbl = Label(window, text = "")
spacelbl.grid(column = 0, row = 8)

farlbl = Label(window, text = 'fahrenheit to celsius', font = ("Arial",16))
farlbl.grid(column = 0, row = 10)

fresultlbl = Label(window, text = "", font = ("Arial", 16))
fresultlbl.grid(column = 0, row = 12)

def clickedc():
    
    resc = celtxt.get() 
    resc = int(resc)
    resc = resc * 9 / 5 + 32
    resc = str(resc)
    cdegrees = " degrees fahrenheit"
    cresultlbl.configure(text = resc + cdegrees)
    
def clickedf():

    resf = fartxt.get()
    resf = int(resf)
    resf = (resf - 32) * 5 / 9
    resf = str(resf)
    fdegrees = " degrees celsius"
    fresultlbl.configure(text = resf + fdegrees)
         
"""Entry is used to get user input"""
celtxt = Entry(window, width = 5)
celtxt.focus()
celtxt.grid(column = 1, row = 2)

fartxt = Entry(window, width = 5)
fartxt.focus()
fartxt.grid(column = 1, row = 10)
"""Button in used to create buttons"""
celbtn = Button(window, text = "Convert", command = clickedc)
celbtn.grid(column = 2, row = 2)

farbtn = Button(window, text = "Convert", command = clickedf)
farbtn.grid(column = 2, row = 10)

window.mainloop()


#selected = IntVar()

#rad1 = Radiobutton(window, text = 'First', value = 1, variable = selected)
#rad2 = Radiobutton(window, text = 'Second', value = 2, variable = selected)
#def clicked():
#    print(selected.get())

#chk = Checkbutton(window, text = 'choose')
#chk.grid(column = 0, row = 1)
#rad1.grid(column = 0, row = 0)
#rad2.grid(column = 1, row = 0)


#txt = Entry(window, width = 10)
#txt.focus()
#txt.grid(column = 2, row = 0)


#def clicked():
#    res = "Welcome to " + txt.get()
#    lbl.configure(text = res)

#adding a widget to the window
