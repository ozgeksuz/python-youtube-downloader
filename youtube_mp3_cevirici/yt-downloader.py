import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
#install through ->>  pip install pytube3
import pytube
import time

#===================================== pencere =============================================
root = tk.Tk()
#pencere title
root.title("Youtube Downloader")
#pencere logo
root.iconbitmap("Youtube.ico")
#pencere size
root.geometry("700x300")
#pencere max-size
root.maxsize(700,500)
#pencere min-size
root.minsize(700,500)
# ================================ pencere =============================================================================

#=================================== fonk ======================================================
def download():
        link = text.get("1.0","end-1c")

        if link == '':
                messagebox.showerror("YouTube Downloader", "Linki giriniz:") 
        else:
                yt = pytube.YouTube(link)
                stream = yt.streams.first()
                time.sleep(2)
                text.delete(1.0,'end') 
                text.insert('end','İndirme Bekleniyor ......')
                time.sleep(5)
                stream.download()
                messagebox.showinfo("YouTube Downloader",'Mp4 olarak indirildi.')

# ================================================= End =========================================================
        
# ================================================ main design code ================================================= 
# header label
header = Label(root,bg="black",width="300",height="2")
header.place(x=0,y=0)

#youtube logo image
yt_logo = ImageTk.PhotoImage(Image.open('youtube.png'))
logo = Label(root, image = yt_logo,borderwidth=0)
logo.place(x=10,y=10)

#caption label
caption = Label(root,text="YouTube Downloader",font=('verdana',10,'bold'))
caption.place(x=50,y=10)

#youtube logo image
yt1_logo = ImageTk.PhotoImage(Image.open('yt.png'))
logo1 = Label(root, image = yt1_logo,borderwidth=0)
logo1.place(x=300,y=60)

#text widgets to get the url
text = Text(root,width=60,height=2,font=('verdana',10,'bold'))
text.place(x=90,y=180) 
text.insert('end','Linki giriniz:')

#Download Buttons
button = Button(root,text="İndir",relief=RIDGE,font=('verdana',10,'bold'),bg="red",fg="white",command=download)
button.place(x=330,y=220)

#load the window 
root.mainloop()

#======================================================== End ========================================================