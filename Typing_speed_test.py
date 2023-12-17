from tkinter import *
from tkinter import messagebox
import random
import time


class Speed_calculator:
    def __init__(self):
        self.sentence=["Tomorrow early morning first I go to morning walk",
                       "We would help in any way we could",
                       "This health service cannot take any more people",
                       "You got any big celebrations coming up?",
                       "None of the parties would make any comment"]
        self.root=Tk()
        self.root.title("Typing_speed_test")
        self.root.geometry("700x400")
        self.title=Label(self.root,text="Typing speed test",font=("times new roman",35))
        self.title.grid(row=0,column=0,columnspan=3,padx=80)
        self.frame=LabelFrame(self.root,width=30)
        self.frame.grid(row=1,column=0,columnspan=3,pady=10)

        self.sample_label=Label(self.frame,text=random.choice(self.sentence),font=("areial",15))
        self.sample_label.grid(row=0,column=0,columnspan=3,pady=5)

        

        self.entry=Entry(self.frame,width=80)
        self.entry.grid(row=2,column=0,pady=10)
    
        
        self.start_button=Button(self.root,text="Start",command=self.start)
        self.start_button.grid(row=2,column=0,padx=5,pady=5)
        self.reset_button=Button(self.root,text='Reset',command=self.reset)
        self.reset_button.grid(row=2,column=1,pady=5)

        self.result=Label(self.root,text="Speed\n0.00WPM",font=('arial batlic','20'))
        self.result.grid(column=1,row=3,columnspan=1,pady=5)

        self.root.mainloop()

        

    def start(self):
        self.start_time=time.time()
        self.start_button.config(state=DISABLED)
        self.entry.bind("<KeyPress>",self.calculation)

    def calculation(self,event):
        if self.sample_label.cget('text').startswith(self.entry.get()):
            self.entry.config(fg='green')
        else:
            self.entry.config(fg='red')
        if self.entry.get()==self.sample_label.cget('text')[:-1]:
            self.entry.config(fg='green')
            self.end_time=time.time()
            self.entry.unbind("<KeyPress>")
            self.counter=self.end_time-self.start_time
            self.wps=len(self.entry.get().split())/self.counter
            self.wpm=self.wps*60
            self.result.config(text=f'Speed\n{self.wpm:.2f}WPM',font=('arial batlic','20'))
            self.popup()
    def reset(self):
        self.sample_label.config(text=random.choice(self.sentence),font=("areial",15))
        self.entry.delete(0,END)
        self.start_button.config(state=ACTIVE)
        self.result.config(text="Speed\n0.00WPM",font=('arial batlic','20'))

    def popup(self):
        messagebox.showinfo('Typing Speed Test',f'Speed:\nWords Per Minute={self.wpm:.2f}')
    
Speed_calculator()