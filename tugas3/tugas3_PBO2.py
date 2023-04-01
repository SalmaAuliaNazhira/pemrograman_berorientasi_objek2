# Nama    : Salma Aulia Nazhira
# NIM     : 210511132
# Kelas   : R3/TI21C

from tkinter import *
import pygame

pygame.mixer.init()

def Dog():   
    pygame.mixer.music.load("C:/Users/SALMA AULIA NAZHIRA/Documents/Tugas/SEMESTER 4/PBO2/tugas/voice/suara_anjing.mp3")
    pygame.mixer.music.play()

def Bebek():   
    pygame.mixer.music.load("C:/Users/SALMA AULIA NAZHIRA/Documents/Tugas/SEMESTER 4/PBO2/tugas/voice/suara_bebek.mp3")
    pygame.mixer.music.play()

def Burung():   
    pygame.mixer.music.load("C:/Users/SALMA AULIA NAZHIRA/Documents/Tugas/SEMESTER 4/PBO2/tugas/voice/suara_burung.mp3")
    pygame.mixer.music.play()

def Elang():   
    pygame.mixer.music.load("C:/Users/SALMA AULIA NAZHIRA/Documents/Tugas/SEMESTER 4/PBO2/tugas/voice/suara_elang.mp3")
    pygame.mixer.music.play()

def Gajah():   
    pygame.mixer.music.load("C:/Users/SALMA AULIA NAZHIRA/Documents/Tugas/SEMESTER 4/PBO2/tugas/voice/suara_gajah.mp3")
    pygame.mixer.music.play()

def Kambing():   
    pygame.mixer.music.load("C:/Users/SALMA AULIA NAZHIRA/Documents/Tugas/SEMESTER 4/PBO2/tugas/voice/suara_kambing.mp3")
    pygame.mixer.music.play()

def Kucing():   
    pygame.mixer.music.load("C:/Users/SALMA AULIA NAZHIRA/Documents/Tugas/SEMESTER 4/PBO2/tugas/voice/suara_kucing.mp3")
    pygame.mixer.music.play()

def Kuda():   
    pygame.mixer.music.load("C:/Users/SALMA AULIA NAZHIRA/Documents/Tugas/SEMESTER 4/PBO2/tugas/voice/suara_kuda.mp3")
    pygame.mixer.music.play()

def Sapi():   
    pygame.mixer.music.load("C:/Users/SALMA AULIA NAZHIRA/Documents/Tugas/SEMESTER 4/PBO2/tugas/voice/suara_sapi.mp3")
    pygame.mixer.music.play()

def Serigala():   
    pygame.mixer.music.load("C:/Users/SALMA AULIA NAZHIRA/Documents/Tugas/SEMESTER 4/PBO2/tugas/voice/suara_serigala.mp3")
    pygame.mixer.music.play()

def close():    
    guiWindow.destroy()  

if __name__ == "__main__":   
    guiWindow = Tk()  
    guiWindow.title("Animal Voice Application")  
    guiWindow.geometry("665x430+550+250")  
    guiWindow.resizable(0, 0)  
    guiWindow.configure(bg = "#B5E5CF")  

    functions_frame = Frame(guiWindow, bg = "black") 
    functions_frame.pack(side = "top", expand = True, fill = "both")  

    Label( functions_frame,text = "ANIMAL VOICE APPLICATION", font = ("arial", "17", "bold"), background = "black", 
    foreground="white").place(x = 200, y = 30)  

    Label( functions_frame,text = "By Salma Aulia Nazhira (210511132)", font = ("verdana", "12", "bold"), background = "black", 
    foreground="white").place(x = 20, y = 400)  

    Button(functions_frame, text = "Suara Anjing", width = 20,  bg='#D4AC0D',font=("arial", "14", "bold"), command=Dog
    ).place(x = 70, y = 80,)

    Button(functions_frame, text = "Suara Bebek", width = 20, bg='#D4AC0D', font=("arial", "14", "bold"), command=Bebek
    ).place(x = 350, y = 80) 

    Button(functions_frame, text = "Suara Burung", width = 20, font=("arial", "14", "bold"), bg='#D4AC0D', command=Burung
    ).place(x = 70, y = 130)

    Button(functions_frame, text = "Suara Elang", width = 20, font=("arial", "14", "bold"), bg='#D4AC0D', command=Elang
    ).place(x = 350, y = 130)

    Button(functions_frame, text = "Suara Gajah", width = 20, font=("arial", "14", "bold"), bg='#D4AC0D', command=Gajah
    ).place(x = 70, y = 180)

    Button(functions_frame, text = "Suara Kambing", width = 20, font=("arial", "14", "bold"), bg='#D4AC0D', command=Kambing
    ).place(x = 350, y = 180)

    Button(functions_frame, text = "Suara Kucing", width = 20, font=("arial", "14", "bold"), bg='#D4AC0D', command=Kucing
    ).place(x = 70, y = 230)

    Button(functions_frame, text = "Suara Kuda", width = 20, font=("arial", "14", "bold"), bg='#D4AC0D', command=Kuda
    ).place(x = 350, y = 230)

    Button(functions_frame, text = "Suara Sapi", width = 20, font=("arial", "14", "bold"), bg='#D4AC0D', command=Sapi
    ).place(x = 70, y = 280)

    Button(functions_frame, text = "Suara Serigala", width = 20, font=("arial", "14", "bold"), bg='#D4AC0D', command=Serigala
    ).place(x = 350, y = 280)

    Button(functions_frame, text = "Exit", width = 52, bg='#D4AC0D',  font=("arial", "14", "bold"), command = close  
    ).place(x = 17, y = 340) 

    guiWindow.mainloop()  
    pygame.quit()
