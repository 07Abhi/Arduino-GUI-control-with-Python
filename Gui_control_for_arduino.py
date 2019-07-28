import serial
from time import sleep
from tkinter import*
arduinodata = serial.Serial('com10',9600)
def led1_on():
    arduinodata.write(b'1')
    print("LED1 is on")
def led2_on():
    arduinodata.write(b'2')
    print("LED2 is on")
def led3_on():
    arduinodata.write(b'3')
    print("LED3 is on")
def led1_off():
    arduinodata.write(b'a')
    print("LED1 is Off")
def led2_off():
    arduinodata.write(b'b')
    print("LED2 is Off")
def led3_off():
    arduinodata.write(b'c')
    print("LED3 is Off")
def all_off():
    arduinodata.write(b'4')
    print("ALL LED is Off")
def all_on():
    arduinodata.write(b'5')
    print("ALL led is ON")
box = Tk()
box.title("Arduino Control")
box.geometry("500x500")
Label(box, text="LED-1", font="Arial 10 bold italic",fg="red").grid(row=0, column=2)
Label(box, text=" ").grid(row=1, column=2)
Label(box, text="LED-2", font="Arial 10 bold italic",fg="red").grid(row=2, column=2)
Label(box, text=" ").grid(row=3, column=2)
Label(box, text="LED-3", font="Arial 10 bold italic",fg="red").grid(row=4, column=2)
Label(box, text=" ").grid(row=5, column=2)
Button(box, text="ON", command=led1_on).grid(row=0,column=8)
Button(box, text="OFF",command=led1_off).grid(row=0,column=10)
Button(box, text="ON", command=led2_on).grid(row=2,column=8)
Button(box, text="OFF",command=led2_off).grid(row=2,column=10)
Button(box, text="ON", command=led3_on).grid(row=4,column=8)
Button(box, text="OFF",command=led3_off).grid(row=4,column=10)
Button(box, text="MASTER OFF", command=all_off).grid(row=7, column=12)
Button(box, text="MASTER ON", command=all_on).grid(row=9, column=12)


