
from cgitb import text
from tkinter import *
import speedtest 
import socket

#speedtest work:
def speedcheck():
    sp = speedtest.Speedtest()
    #to get server from speed test module
    sp.get_servers()
    #to get download speed
    down=str(round(sp.download()/(10**6),3))+".mbps"
    #(down/up gives us speed in bits per second so to convert in into mb/sec do /10**6 )
    up=str(round(sp.upload()/(10**6),3))+".mbps"
    #round function is used to round of final value of mbps
    #To get IP Adress: 
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    #print("Your Computer Name is:" + hostname)
    print("Your Computer IP Address is:" + IPAddr)
    #now setting these function to parameter
    lab_down.config(text=down)
    lab_up.config(text=up)
    lab_ip.config(text=IPAddr)

#graphic work:
sp=Tk()
sp.title("Internet speed Test")
sp.geometry("500x700")
sp.config(bg="black")
lab=Label(sp,text="Internet Speed Test", font=("Time New Roman",18, "bold"))
lab.place(x=60,y=40, height=30,width=380)

lab=Label(sp,text="Download Speed ", font=("Time New Roman",18, "bold"))
lab.place(x=60,y=130,height=30,width=380)

lab_down=Label(sp,text="00", font=("Time New Roman",18, "bold"))
lab_down.place(x=60,y=180,height=30,width=380)

lab=Label(sp,text="Upload Speed ", font=("Time New Roman",18, "bold"))
lab.place(x=60,y=290,height=30,width=380)

lab_up=Label(sp,text="00", font=("Time New Roman",18, "bold"))
lab_up.place(x=60,y=340,height=30,width=380)

button=Button(sp,text="Check Speed",font=("Time New Roman",18, "bold"),relief=RAISED,bg="Red",command=speedcheck)
button.place(x=60,y=400,height=50,width=380)

lab=Label(sp,text="Your IP Address ", font=("Time New Roman",18, "bold"))
lab.place(x=60,y=500,height=30,width=380)

lab_ip=Label(sp,text="00", font=("Time New Roman",18, "bold"))
lab_ip.place(x=60,y=540,height=30,width=380)

lab=Label(sp,text="BY Omkar Khade ", font=("Time New Roman",16, "bold"))
lab.place(x=60,y=620, height=30,width=380)

sp.mainloop()