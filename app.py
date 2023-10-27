#programa de la hora
from tkinter import Label, Tk
import time

windows = Tk ()
windows.config(bg='gray')
windows.geometry('500x200')
windows.wm_attributes('-transparentcolor' , 'gray')
windows.overrideredirect(1)

#que pedo
def quit(*args):
    windows.destroy()
    windows.quit()
def obtaintime():
    hour = time.strftime('%H:%M:%S')

    texthour['text'] = hour
    texthour.after(1000, obtaintime)

def star(event):
    global x, y
    x = event.x
    y = event.y
def stop(event):
    global x, y
    x = None
    y = None
def move(event):
    global x, y
    deltax = event.x - x
    deltay = event.y - y
    windows.geometry("+%s+%s" %(windows.winfo_x() + deltax, windows.winfo_y() + deltay))
    windows.update()

windows.bind("<ButtonPress-1>", star)
windows.bind("<ButtonRelease-1>", stop)
windows.bind("<B1-Motion>", move)
windows.bind("<KeyPress-Escape>", quit)

texthour = Label (windows, fg='white', bg='gray', font= ('Star Jedi Holow', 50, 'bold'), width=10)
texthour.grid(column=0, row=0, ipadx=1, ipady=1)

obtaintime()
windows.mainloop()