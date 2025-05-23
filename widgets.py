from tkinter import *
window=Tk()
window.title("My window")
window.geometry('400x200')

lbl=Label(text='Hey there',fg='blue',bg='green',height=1,width='300')
lbl_name=Label(text='Full nmae',bg='yellow')
name_entry=Entry()

def display():
    name=name_entry.get()
    global Message
    Message="Hello welcome to the application! \n Today's date is:"
    Greet='Welcome'+name+"\n"

    text_box.inseet(END,Message)
    text_box.insert(END,Greet)
    text_box.insert(END,date.today())

text_box=Text(height=3)

btn=Button(text='Begin',fg='Indigo',bg='Aquamarine',command=display)

lbl.pack()
lbl_name.pack()
name_entry.pack()
btn.pack()
text_box.pack()