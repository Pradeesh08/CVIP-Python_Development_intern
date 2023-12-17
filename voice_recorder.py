from tkinter import *
import time
import wave
import pyaudio
import threading
import os

class recorder:
    def __init__(self):
        self.root=Tk()
        self.root.title("Voice Recorder")
        self.root.geometry("400x200")
        self.root.resizable(False,False)
        self.recording=False
        self.label=Label(self.root,text="Voice Recorder",font=("arial",30))
        self.label.pack()
        self.rec_button=Button(self.root,text="🎙️",command=self.starter,font=("arial",25,"bold"),bd=3)
        self.rec_button.pack()
        self.timer=Label(self.root,text="00:00:00",font=("arial",15))
        self.timer.pack()

        self.root.mainloop()
    def starter(self):
        if self.recording:
            self.rec_button.config(fg="black")
            self.recording=False
        else:
            self.rec_button.config(fg="red")   
            self.recording=True
            t1=threading.Thread(target=self.rec)
            t1.start()
    def rec(self):
        p=pyaudio.PyAudio()
        stream=p.open(format=pyaudio.paInt16,channels=1,rate=44100,input=True,frames_per_buffer=1024)
        start_time=time.time()
        frame=[]
        while self.recording:
            data=stream.read(1024)
            frame.append(data)

            time_passed=time.time() - start_time
            sec=time_passed%60
            mins=time_passed//60
            hrs=mins//60
            self.timer.config(text=f"{int(hrs):02d}:{int(mins):02d}:{int(sec):02d}",font=("arial",15))
        stream.start_stream()
        stream.close()
        p.terminate()
        exists=True
        i=1
        while exists:
            if  os.path.exists(f"voice_record_{i}"):
                i+=1
            else:
                exists=False
        wf=wave.open(f"voice_record_{i}","wb")
        wf.setnchannels(1)
        wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
        wf.setframerate(44100)
        wf.writeframes(b"".join(frame))
        wf.close()        


recorder()