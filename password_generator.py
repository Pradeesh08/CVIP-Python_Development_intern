from  tkinter import *
import  random
import string
root=Tk()
root.title('Password Generator')
root.geometry('600x400')

def pass_word():
    password_entry.delete(0,END)
    length=int(entry.get())
    upper_caseletters=string.ascii_uppercase
    lower_caseletters=string.ascii_lowercase
    digits=string.digits
    symbols=string.punctuation

    capital=upperletter.get()
    lower=lowerletter.get()
    numbers=digit.get()
    special=symbol.get()
    
    if capital=='on':
        upper_caseletter=True
    else:
        upper_caseletter=False
    if lower=='on':
        lower_caseletter=True
    else:
        lower_caseletter=False
    if numbers=='on':
        digit_=True
    else:
        digit_=False
    if special=='on':
        symbol_=True
    else:
        symbol_=False
    word=''
    if upper_caseletter:
        word+=upper_caseletters
    if lower_caseletter:
        word+=lower_caseletters
    if digit_:
        word+=digits
    if symbol_:
        word+=symbols
    
    password=''.join(random.sample(word,length))
    
    password_entry.insert(0,password)

title_label=Label(root,text='Password Generator')
title_label.pack()

frame=LabelFrame(root,bd=5,width=420,height=250)
frame.pack()

upperletter=StringVar()
lowerletter=StringVar()
digit=StringVar()
symbol=StringVar()
upperletter.set('on')
lowerletter.set('on')
digit.set('on')
symbol.set('on')

label=Label(frame,text='Password Length')
label.grid(row=0,column=0)
entry=Entry(frame)
entry.grid(row=0,column=1,columnspan=2)

uppercase_letters=Checkbutton(frame,text='Upper Case',variable=upperletter,onvalue='on',offvalue='off')
uppercase_letters.grid(row=2,column=0,columnspan=3,)

lowercase_letters=Checkbutton(frame,text='Lower Case',variable=lowerletter,onvalue='on',offvalue='off')
lowercase_letters.grid(row=3,column=0,columnspan=3)

digits=Checkbutton(frame,text='Digits',variable=digit,onvalue='on',offvalue='off')
digits.grid(row=4,column=0,columnspan=3)

symbols=Checkbutton(frame,text='Symbols',variable=symbol,onvalue='on',offvalue='off')
symbols.grid(row=5,column=0,columnspan=3)

pass_gen=Button(root,text='Generate Password',padx=15,pady=10,font=('Arial', 10),command=pass_word)
pass_gen.pack(anchor=CENTER)

password_entry=Entry(root,font=('Arial', 15),bd=0,bg="grey")
password_entry.pack(pady=5)

root.mainloop()