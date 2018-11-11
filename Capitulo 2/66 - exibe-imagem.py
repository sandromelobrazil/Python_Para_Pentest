from PIL import ImageTk, Image
import Tkinter

root = Tkinter.Tk() #1
root.geometry('0x0+0+0') #2
root.attributes('-alpha', 0) #3
root.overrideredirect(1) #4

img = ImageTk.PhotoImage(Image.open("imagem.jpg")) #5

top = Tkinter.Toplevel() #6
top.transient(root) #7
top.overrideredirect(1) #8

screen_width = top.winfo_screenwidth() #9
screen_height = top.winfo_screenheight()
x = (screen_width/2) - (img.width()/2)
y = (screen_height/2) - (img.height()/2) #10
top.geometry('%dx%d+%d+%d' % (img.width(), img.height(), x, y)) #11

top.resizable('False', 'False') #12
Tkinter.Label(top, image=img).pack() #13

root.mainloop() #14