import RPi.GPIO as GPIO
import time
​
GPIO.setmode(GPIO.BCM)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup( 4,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
​
def move(pin1,pin2,sec):
	GPIO.output(pin1,GPIO.HIGH)
	GPIO.output(pin2,GPIO.HIGH)
	time.sleep(sec)
	GPIO.output(pin1,GPIO.LOW)
	GPIO.output(pin2,GPIO.LOW)
​
def left():
	print("left")
	move(17,4,0.1)
	
def right():
	print("right")
	move(27,18,0.1)
​
def front():
	print("front")
	move(27,4,0.2)
	
def back():
	print("back")
	move(17,18,0.2)
​
import tkinter as tk
​
#main window
root = tk.Tk()
​
#window's title
root.title("Remote Man")
​
#main window's sise
root.geometry("600x600")
​
#button LRFB
L =tk.Button(root, text='L',command=left)
L.grid(row=2,column=1,ipadx=80,ipady=80)
R =tk.Button(root, text='R',command=right)
R.grid(row=2,column=3,ipadx=80,ipady=80)
F =tk.Button(root, text='F',command=front)
F.grid(row=1,column=2,ipadx=80,ipady=80)
B =tk.Button(root, text='B',command=back)
B.grid(row=3,column=2,ipadx=80,ipady=80)
​
root.mainloop()