from tkinter import *
root=Tk()
root.title('Simple Calculator')
root.geometry("264x230")
#displaying numbers
def click(num):
    temp=display.get()
    display.delete(0,END)
    display.insert(0,str(temp)+str(num))
#addition
def add():
    global first_num,math
    first_num=display.get()
    math='+'
    display.delete(0,END)
#subtraction
def sub():
    global first_num,math
    first_num=display.get()
    math='-'
    display.delete(0,END)
#multiplication
def mul():
    global first_num,math
    first_num=display.get()
    math='*'
    display.delete(0,END)
#division
def div():
    global first_num,math
    first_num=display.get()
    math='/'
    display.delete(0,END)
#calculation
def equal():
    second_num=display.get()
    display.delete(0,END)
    if math=='+':
        display.insert(0,int(first_num)+int(second_num))
    elif math=='-':
        display.insert(0,int(first_num)-int(second_num))
    elif math=='*':
        display.insert(0,int(first_num)*int(second_num))
    elif math=='/':
        display.insert(0,int(first_num)/int(second_num))
#clearing values
def clear():
    display.delete(0,END)
#creating display
display=Entry(root,bd=10,bg='black',fg='white',width=40)
display.grid(row=0,column=0,columnspan=4,ipady=8)
#creating button
button_1=Button(root,text='1',padx=25,pady=10,bg='grey65',fg='black',command=lambda:click('1'))
button_2=Button(root,text='2',padx=25,pady=10,bg='grey65',fg='black',command=lambda:click('2'))
button_3=Button(root,text='3',padx=25,pady=10,bg='grey65',fg='black',command=lambda:click('3'))
button_add=Button(root,text='+',padx=25,pady=10,bg='gainsboro',fg='black',command=add)
button_4=Button(root,text='4',padx=25,pady=10,bg='grey65',fg='black',command=lambda:click('4'))
button_5=Button(root,text='5',padx=25,pady=10,bg='grey65',fg='black',command=lambda:click('5'))
button_6=Button(root,text='6',padx=25,pady=10,bg='grey65',fg='black',command=lambda:click('6'))
button_sub=Button(root,text='-',padx=27,pady=10,bg='gainsboro',fg='black',command=sub)
button_7=Button(root,text='7',padx=25,pady=10,bg='grey65',fg='black',command=lambda:click('7'))
button_8=Button(root,text='8',padx=25,pady=10,bg='grey65',fg='black',command=lambda:click('8'))
button_9=Button(root,text='9',padx=25,pady=10,bg='grey65',fg='black',command=lambda:click('9'))
button_mul=Button(root,text='*',padx=27,pady=10,bg='gainsboro',fg='black',command=mul)
button_clear=Button(root,text='C',padx=24,pady=10,bg='gainsboro',fg='black',command=clear)
button_0=Button(root,text='0',padx=25,pady=10,bg='grey65',fg='black',command=lambda:click('0'))
button_equal=Button(root,text='=',padx=24,pady=10,bg='gainsboro',fg='black',command=equal)
button_div=Button(root,text='/',padx=27,pady=10,bg='gainsboro',fg='black',command=div)
#inserting buttons
button_1.grid(row=1,column=0)
button_2.grid(row=1,column=1)
button_3.grid(row=1,column=2)
button_add.grid(row=1,column=3)
button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_sub.grid(row=2,column=3)
button_7.grid(row=3,column=0)
button_8.grid(row=3,column=1)
button_9.grid(row=3,column=2)
button_mul.grid(row=3,column=3)
button_clear.grid(row=4,column=0)
button_0.grid(row=4,column=1)
button_equal.grid(row=4,column=2)
button_div.grid(row=4,column=3)

root.mainloop()