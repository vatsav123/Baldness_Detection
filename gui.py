# Importing Necessary Libraries
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import Image,ImageTk
import numpy
import numpy as np

# Loading the Model
from keras.models import load_model
import tensorflow as tf
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)
model=load_model('model.h5')

# Initializing the GUI
top=tk.Tk()
top.geometry('800x600')
top.title('Bald Detector')
top.configure(background='#CDCDCD')

# Initializing the Labels 

label2=Label(top,background="#CDCDCD",font=('arial',15,'bold'))
sign_image=Label(top)

# Definig Detect fuction which detects the baldness of the person in image using the model
def Detect(file_path):
    global label_packed
    image=Image.open(file_path)
    image=image.resize((48,48))
    image=numpy.expand_dims(image,axis=0)
    image=np.array(image)
    image=np.delete(image,0,1)
    image=np.resize(image,(48,48,3))
    print (image.shape)
    bald_f=["Bald","NotBald"]
    image=np.array([image])/255
    pred=model.predict(image)
    
    bald=int(np.round(pred[0][0]))
    
    print("Predicted Hair is "+bald_f[bald])
    
    label2.configure(foreground="#011638",text=bald_f[bald])

# Defining Show_detect button function
def show_Detect_button(file_path):
    Detect_b=Button(top,text="Detect Image",command=lambda: Detect(file_path),padx=10,pady=5)
    Detect_b.configure(background="#364156",foreground='white',font=('arial',10,'bold'))
    Detect_b.place(relx=0.79,rely=0.46) 

# Definig Upload Image Function
def upload_image():
    try:
        file_path=filedialog.askopenfilename()
        uploaded=Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width()/2.25),(top.winfo_height()/2.25)))
        im=ImageTk.PhotoImage(uploaded)

        sign_image.configure(image=im)
        sign_image.image=im
       
        label2.configure(text='')
        show_Detect_button(file_path)
    except:
        pass

upload=Button(top,text="Upload an Image",command=upload_image,padx=10,pady=5)
upload.configure(background="#364156",foreground='white',font=('arial',10,'bold'))
upload.pack(side='bottom',pady=50)
sign_image.pack(side='bottom',expand=True)

label2.pack(side="bottom",expand=True)
heading=Label(top,text="Bald Detector",pady=20,font=('arial',20,"bold"))
heading.configure(background="#CDCDCD",foreground="#364156")
heading.pack()
top.mainloop()