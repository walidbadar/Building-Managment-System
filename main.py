#Tkinter and GPIO together
#----------------------------------------------------------------------------
import time
import os
import serial
from tkinter import *

#----------------------------------------------------------------------------
ser = serial.Serial('COM4', 57600, timeout = 1)
#----------------------------------------------------------------------------

def main():

    root=Tk()
    root.title("BMS")
    logo=PhotoImage(file="building_img.gif")
    w1=Label(root,image=logo).place(x=400,y=40)
    root.wm_geometry("800x600+0+0")# x,y+origin x+ origin y
    root.configure(background="white")
    lblheading=Label(root,text="BUILDING MANAGMENT SYSTEM",bg="white",fg="black",font=("Verdana",15,"italic","bold"))
    lblheading.pack()

    #--------------------------------------------------------------
    #Access Control
    #--------------------------------------------------------------
    lblAccessControl=Label(root,text="Access Control",bg="white",fg="black",font=("Verdana",10,"bold","underline"))
    lblAccessControl.place(x=20,y=30)
    txt1AccessControl=Text(root,width=20,height=1,relief='ridge')
    txt1AccessControl.place(x=20,y=50)
    txt2AccessControl=Text(root,width=20,height=1,relief='ridge')
    txt2AccessControl.place(x=20,y=70)
    txt3AccessControl=Text(root,width=20,height=1,relief='ridge')
    txt3AccessControl.place(x=20,y=90)
    txt4AccessControl=Text(root,width=20,height=1,relief='ridge')
    txt4AccessControl.place(x=20,y=110)

    #--------------------------------------------------------------
    #Fire Emergency
    #--------------------------------------------------------------
    lblFireEmergency=Label(root,text="Fire Emergency",bg="white",fg="black",font=("Verdana",10,"bold","underline"))
    lblFireEmergency.place(x=20,y=150)
    txt5FireEmergency=Text(root,width=20,height=1,relief='ridge',fg='white',bg='red')
    txt5FireEmergency.place(x=20,y=170)

    #--------------------------------------------------------------
    #Intrusion
    #--------------------------------------------------------------
    lblIntrusionDetection=Label(root,text="Intrusion Detection",bg="white",fg="black",font=("Verdana",10,"bold","underline"))
    lblIntrusionDetection.place(x=20,y=210)
    txt6IntrusionDetection=Text(root,width=20,height=1,relief='ridge')
    txt6IntrusionDetection.place(x=20,y=230)
    txt7IntrusionDetection=Text(root,width=20,height=1,relief='ridge')
    txt7IntrusionDetection.place(x=20,y=250)
    txt8IntrusionDetection=Text(root,width=20,height=1,relief='ridge')
    txt8IntrusionDetection.place(x=20,y=270)
    
    #--------------------------------------------------------------
    #Parking
    #--------------------------------------------------------------
    lblParking=Label(root,text="Parking System",bg="white",fg="black",font=("Verdana",10,"bold","underline"))
    lblParking.place(x=20,y=310)
    txt9Parking=Text(root,width=20,height=1,relief='ridge')
    txt9Parking.place(x=20,y=330)
    txt10Parking=Text(root,width=20,height=1,relief='ridge')
    txt10Parking.place(x=20,y=350)

    #--------------------------------------------------------------
    #Lighting
    #--------------------------------------------------------------
    varLight = IntVar()

    def setLight():
       ser.write(str(varLight.get()))
       ser.write(b'\n')

    def setShade(tog=[0]):

        tog[0] = not tog[0] 
        
        if tog[0]:
            button3Lighting.config(text='Close Shade')
            ser.write(b'A')
            ser.write(b'\n')

        else:
            button3Lighting.config(text='Open Shade ')
            ser.write(b'B')
            ser.write(b'\n')
       

    lblLighting=Label(root,text="Lighting System",bg="white",fg="black",font=("Verdana",10,"bold","underline"))
    lblLighting.place(x=20,y=390)
    button2Lighting = Button(root, text=" Set Intesity ", command=setLight)
    button2Lighting.place(x=20,y=410)
    scale1Lighting = Scale( root, variable = varLight, from_=0, to=3, orient=HORIZONTAL)
    scale1Lighting.place(x=20,y=440)
    button3Lighting = Button(root, text="Open Shade ", command=setShade)
    button3Lighting.place(x=20,y=490)

    #--------------------------------------------------------------
    #HVAC
    #--------------------------------------------------------------
    varTemp = IntVar()
    
    def setTemp():
       ser.write(b'Y')
       ser.write(str(varTemp.get()).encode())
       ser.write(b'\n')

    lblHVAC=Label(root,text="HVAC",bg="white",fg="black",font=("Verdana",10,"bold","underline"))
    lblHVAC.place(x=220,y=30)   
    button1HVAC = Button(root, text=" Set Tempreature ", command=setTemp)
    button1HVAC.place(x=220,y=60) 
    scale1HVAC = Scale( root, variable = varTemp, from_=-9, to=50, orient=HORIZONTAL)
    scale1HVAC.place(x=220,y=90) 

    #--------------------------------------------------------------
    #Water Managment
    #--------------------------------------------------------------
    lblwaterManagment=Label(root,text="Water Managment",bg="white",fg="black",font=("Verdana",10,"bold","underline"))
    lblwaterManagment.place(x=220,y=150)
    txt12waterManagment=Text(root,width=20,height=1,relief='ridge')
    txt12waterManagment.place(x=220,y=170)
    
    #--------------------------------------------------------------
    #Lobby
    #--------------------------------------------------------------
    varLobby = IntVar()

    def setLight():
       ser.write(str(varLight.get()))
       ser.write(b'\n')

    lblLobby=Label(root,text="Lobby",bg="white",fg="black",font=("Verdana",10,"bold","underline"))
    lblLobby.place(x=220,y=210)   
    button2Lobby = Button(root, text=" Set Intesity ", command=setLight)
    button2Lobby.place(x=220,y=230)
    scale1Lobby = Scale( root, variable = varLight, from_=5, to=9, orient=HORIZONTAL)
    scale1Lobby.place(x=220,y=250)
   
    def process():
        x1 = 0
        x2 = 0
        x3 = 0
        x4 = 0
        x5 = 0
        incomingByte = ser.read(1)
        print(incomingByte)
        if (incomingByte == b"A"):
            txt1AccessControl.delete(1.0,END)
            txt1AccessControl.insert(20.0,"Person 'A' swaped")
            txt2AccessControl.delete(1.0,END)
            txt2AccessControl.insert(20.0,"Card Accepted")
            txt3AccessControl.delete(1.0,END)
            txt3AccessControl.insert(20.0,"Door Unlocked")

        elif (incomingByte == b"B"):
            txt1AccessControl.delete(1.0,END)
            txt1AccessControl.insert(20.0,"Person 'B' swaped")
            txt2AccessControl.delete(1.0,END)
            txt2AccessControl.insert(20.0,"Card Accepted")
            txt3AccessControl.delete(1.0,END)
            txt3AccessControl.insert(20.0,"Door Unlocked")

        elif (incomingByte == b"C"):
            txt1AccessControl.delete(1.0,END)
            txt2AccessControl.delete(1.0,END)
            txt3AccessControl.delete(1.0,END)
            txt3AccessControl.insert(20.0,"Door  Locked") 

        elif (incomingByte == b"D"):
            txt5FireEmergency.delete(1.0,END)
            txt5FireEmergency.insert(20.0,"Fire Detected")
            x1=x1+1
            if(x1==10):
                txt5FireEmergency.config(bg='red',fg='white')
                                     
            elif(x1==20):
                txt5FireEmergency.config(fg='red',bg='white')
                                     
            elif(x1>20):
                x1=0
            
        elif (incomingByte == b"E"):
            txt5FireEmergency.delete(1.0,END)
            txt5FireEmergency.insert(20.0,"Fire Extinguished")
            txt5FireEmergency.config(bg="white",fg="green")

        elif (incomingByte == b"F"):
            txt4AccessControl.delete(1.0,END)
            txt4AccessControl.insert(20.0,"Motion Detected")
            x2=x2+1
            if(x2==40):
                txt4AccessControl.config(bg='red',fg='white')

            elif(x2==80):
                txt4AccessControl.config(fg='red',bg='white')

            elif(x2>80):
                x2=0

        elif (incomingByte == b"G"):
            txt4AccessControl.delete(1.0,END)
            txt4AccessControl.insert(20.0,"No Motion Detected")
            txt4AccessControl.config(bg="white",fg="green")

        elif (incomingByte == b"H"):
            txt8IntrusionDetection.delete(1.0,END)
            txt8IntrusionDetection.insert(20.0,"Motion Detected")
            x3=x3+1
            if(x3==40):
                txt8IntrusionDetection.config(bg='red',fg='white')

            elif(x3==80):
                txt8IntrusionDetection.config(fg='red',bg='white')

            elif(x3>80):
                x3=0

        elif (incomingByte == b"I"):
            txt8IntrusionDetection.delete(1.0,END)
            txt8IntrusionDetection.insert(20.0,"No Motion Detected")
            txt8IntrusionDetection.config(bg="white",fg="green")

        elif (incomingByte == b"J"):
            txt7IntrusionDetection.delete(1.0,END)
            txt7IntrusionDetection.insert(20.0,"Window Break-in")
            x4=x4+1
            if(x4==40):
                txt7IntrusionDetection.config(bg='red',fg='white')

            elif(x4==80):
                txt7IntrusionDetection.config(fg='red',bg='white')

            elif(x4>80):
                x4=0

        elif (incomingByte == b"K"):
            txt7IntrusionDetection.delete(1.0,END)
            txt7IntrusionDetection.insert(20.0,"Window Closed")
            txt7IntrusionDetection.config(bg="white",fg="green")
            
        elif (incomingByte == b"L"):
            txt6IntrusionDetection.delete(1.0,END)
            txt6IntrusionDetection.insert(20.0,"Door Break-in")
            x5=x5+1
            if(x5==40):
                txt6IntrusionDetection.config(bg='red',fg='white')

            elif(x5==80):
                txt6IntrusionDetection.config(fg='red',bg='white')

            elif(x5>80):
                x5=0

        elif (incomingByte == b"M"):
            txt6IntrusionDetection.delete(1.0,END)
            txt6IntrusionDetection.insert(20.0,"Door Locked")
            txt6IntrusionDetection.config(bg="white",fg="green")

        elif (incomingByte == b"N"):
            txt9Parking.delete(1.0,END)
            txt9Parking.insert(20.0,"No of Empty Slot: 0")
            txt10Parking.delete(1.0,END)
            txt10Parking.insert(20.0,"Parking Full")
            txt10Parking.config(bg="white",fg="red")

        elif (incomingByte == b"O"):
            txt9Parking.delete(1.0,END)
            txt9Parking.insert(20.0,"No of Empty Slot: 1")
            txt10Parking.delete(1.0,END)
            txt10Parking.insert(20.0,"Parking Available")
            txt10Parking.config(bg="white",fg="green")

        elif (incomingByte == b"P"):
            txt9Parking.delete(1.0,END)
            txt9Parking.insert(20.0,"No of Empty Slots: 2")
            txt10Parking.config(bg="white",fg="green")
            txt10Parking.delete(1.0,END)
            txt10Parking.insert(20.0,"Parking Available")

        elif (incomingByte == b"Q"):
            txt9Parking.delete(1.0,END)
            txt9Parking.insert(20.0,"No of Empty Slots: 3")
            txt10Parking.delete(1.0,END)
            txt10Parking.insert(20.0,"Parking Available")
            txt10Parking.config(bg="white",fg="green")

        elif (incomingByte == b"R"):
            txt9Parking.delete(1.0,END)
            txt9Parking.insert(20.0,"No of Empty Slots: 4")
            txt10Parking.config(bg="white",fg="green")
            txt10Parking.delete(1.0,END)
            txt10Parking.insert(20.0,"Parking Available")
            txt10Parking.config(bg="white",fg="green")

        elif (incomingByte == b"S"):
            txt9Parking.delete(1.0,END)
            txt9Parking.insert(20.0,"No of Empty Slots: 5")
            txt10Parking.delete(1.0,END)
            txt10Parking.insert(20.0,"Parking Available")
            txt10Parking.config(bg="white",fg="green")

        elif (incomingByte == b"T"):
            txt9Parking.delete(1.0,END)
            txt9Parking.insert(20.0,"No of Empty Slots: 6")
            txt10Parking.delete(1.0,END)
            txt10Parking.insert(20.0,"Parking Available")
            txt10Parking.config(bg="white",fg="green")

        elif (incomingByte == b"U"):
            txt12waterManagment.delete(1.0,END)
            txt12waterManagment.insert(20.0,"Water Level 0%")

        elif (incomingByte == b"V"):
            txt12waterManagment.delete(1.0,END)
            txt12waterManagment.insert(20.0,"Water Level 25%")

        elif (incomingByte == b"W"):
            txt12waterManagment.delete(1.0,END)
            txt12waterManagment.insert(20.0,"Water Level 75%")

        elif (incomingByte == b"X"):
            txt12waterManagment.delete(1.0,END)
            txt12waterManagment.insert(20.0,"Water Level 100%")

        root.update()
        root.after(10, process)

    root.after(10, process)
    root.update()
    root.mainloop()

if __name__ == '__main__':
    main()

