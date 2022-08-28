# Importing tkinter to make gui in python
from tkinter import*
from tkinter import filedialog
from tkPDFViewer import tkPDFViewer as pdf
import os

# Initializing tk
root = Tk()
# Set the width and height of our root window.
root.geometry("850x735")
#set title of windoe
root.title("PDF Viewer")
# set baground colour of window
root.configure(bg="lightcyan")
#creating frame for title
frame=Frame(root,width=500,height=400,bg="purple")
frame.pack()
#creating team and batch name inside window
name=Label(frame,text="N1 Batch AI&DS Team PDF reader", fg='white',bg='purple',font='Arial 28 bold')
name.pack() 

#creating function to browse file from local PC/computer
def browseFiles():
    filename=filedialog.askopenfilename(initialdir=os.getcwd(),
                                       title="select pdf file",
                                       filetype=(("PDF File",".pdf"),
                                                ("PDF File",".PDF"),
                                                ("All file",".txt")))
    #creating a variable to show pdf file on window
    v1 = pdf.ShowPdf() 
    #set configuration of inner pdf showing window
    v2 = v1.pdf_view(root,pdf_location=open(filename,"r"),width =77,height=100)
    v2.pack(pady=(0,0))  
    
#creating button to initialise browsefiles function and to open pdf file
Button(root,text="open",width=40,
      font="arial 20",bd=4).pack()   

root.mainloop()