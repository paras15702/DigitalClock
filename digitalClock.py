from tkinter import *
from datetime import *
from tkinter.messagebox import *
from requests import *
import pytz
import time
import sys


root=Tk()
root.title("Digital Clock")
root.geometry("1000x700+250+80")
root.configure(bg="#856ff8")
p1 = PhotoImage(file = 'clock.png')
root.iconphoto(False, p1)

f=("Times New Roman",40,"bold","italic")



""" ----------------------------------------------------------------------------------------------------------- """


def showTime():
	hour=datetime.now().hour
	min=datetime.now().minute
	sec=datetime.now().second
	currtime=str(hour)+":"+str(min)+":"+str(sec)
	time_lab.configure(text=currtime)
	root.after(1000,showTime)



def world():
	world_clock.deiconify()
	root.withdraw()
	


def worldClock():
	
	area=pytz.timezone(selected.get())
	try:
		if (area=="") :
			raise Exception("enter valid area")
			ent_loc.delete(0,END)
			ent_loc.focus()
			return
		hour=datetime.now(area).hour
		min=datetime.now(area).minute
		sec=datetime.now(area).second
		currtime=str(hour)+":"+str(min)+":"+str(sec)
		lab_time.configure(text=currtime)
		world_clock.after(1000,worldClock)
	except Exception as e:
		showerror("Invalid", e)
		

def backWorld():
	selected.set("Asia/Kolkata")
	root.deiconify()
	world_clock.withdraw()
	
			

def showSw():
	stop_watch.deiconify()
	root.withdraw()

def start():
	global second
	second=0
	global minute
	minute =0
	global hour
	hour = 0
	global stop
	stop=0
	global reset
	reset=0
	stopWatchStart()

def stopWatchStart():
	global second,minute,hour,stop,reset
	second+=1
	
	if second==60:
		second=0
		minute+=1
	if minute==60:
		minute=0
		hour+=1
	if stop==0:
		time=str(hour)+":"+str(minute)+":"+str(second)
		time_elapsed.configure(text=time)
		world_clock.after(1000,stopWatchStart)
	
			

def stopWatchStop():
	global stop
	stop=1

def stopWatchReset():
	global reset ,stop
	reset=1
	stop=1
	if reset==1:
		time="00:00:00"
		time_elapsed.configure(text=time)

def backSw():
	root.deiconify()
	stop_watch.withdraw()

def showCountDown():
	countdown_timer.deiconify()
	root.withdraw()

def countDownBack():
	root.deiconify()
	countdown_timer.withdraw()

def startCd():
	global x
	x=int(ent_time.get())
	startCd2()

def startCd2():
	global x
	if x >-1 :
		seconds=x%60
		minutes=int(x/60)%60
		hours=int(x/3600)
		cd=str(hours)+":"+str(minutes)+":"+str(seconds)
		lab_showtime.configure(text=cd)
		if x==0:
			ent_time.delete(0,END)
			ent_time.focus()
			lab_showtime.configure(text="TIME UP !!!")
		x-=1
		countdown_timer.after(1000,startCd2)
		
	
	

""" ------------------------------------------------------------------------------------------------------------ """

time_lab=Label(root,font=f,bg="pink")
time_lab.pack(pady=30)
world_clock_btn=Button(root,text="World Clock",font=f,command=world,bg="pink")
world_clock_btn.pack(pady=30)
stopwatch_btn=Button(root,text="StopWatch",font=f,command=showSw,bg="pink")
stopwatch_btn.pack(pady=30)
countdown_btn=Button(root,text="CountDown",font=f,bg="pink",command=showCountDown)
countdown_btn.pack(pady=30)
showTime()


""" ------------------------------------------------------------------------------------------------------------- """
world_clock = Toplevel()
world_clock.title("World clock")
world_clock.geometry("1000x700+250+80")
world_clock.configure(bg="#856ff8")
world_clock.iconphoto(False, p1)
country_list=[]
for timeZone in pytz.all_timezones:
    country_list.append(timeZone)

selected=StringVar()
selected.set("Asia/Kolkata")
lab_loc=Label(world_clock,text="Enter the location",font=f,bg="pink")
ent_loc=OptionMenu(world_clock,selected,*country_list)
lab_time=Label(world_clock,font=f,bg="#856ff8")
serch_btn=Button(world_clock,text="Search",font=f,command=worldClock,bg="green")
lab_loc.pack(pady=30)
ent_loc.pack(pady=30)
lab_time.pack(pady=30)
serch_btn.pack(pady=30)
backworld_btn=Button(world_clock,text="Back",font=f,command=backWorld,bg="orange")
backworld_btn.place(x=830,y=590)
world_clock.withdraw()

""" ------------------------------------------------------------------------------------------------------------- """
stop_watch = Toplevel()
stop_watch.title("StopWatch")
stop_watch.geometry("1000x700+250+80")
stop_watch.configure(bg="#856ff8")
stop_watch.iconphoto(False, p1)
time_elapsed=Label(stop_watch,font=f,bg="#856ff8")
start_btn=Button(stop_watch,font=f,text="START",command=start,bg="green")
stop_btn=Button(stop_watch,font=f,text="STOP",command=stopWatchStop,bg="red")
reset_btn=Button(stop_watch,font=f,text="RESET",command=stopWatchReset,bg="yellow")
backsw_btn=Button(stop_watch,text="Back",font=f,command=backSw,bg="orange")

time_elapsed.pack(pady=30)
start_btn.pack(pady=40)
stop_btn.pack(pady=30)
reset_btn.pack(pady=30)
backsw_btn.place(x=830,y=590)
stop_watch.withdraw()




""" ------------------------------------------------------------------------------------------------------------- """

countdown_timer = Toplevel()
countdown_timer.title("StopWatch")
countdown_timer.geometry("1000x700+250+80")
countdown_timer.configure(bg="#856ff8")
backcd_btn=Button(countdown_timer,text="Back",font=f,command=countDownBack,bg="orange")
backcd_btn.place(x=830,y=590)
countdown_timer.iconphoto(False, p1)
countdown_timer.withdraw()

lab=Label(countdown_timer,font=f,bg="#856ff8",text="Enter time is seconds")
ent_time=Entry(countdown_timer,font=f,width=20)

lab_showtime=Label(countdown_timer,font=f,bg="#856ff8",width=100)
lab.pack(pady=30)
ent_time.pack(pady=30)

lab_showtime.pack(pady=30)

start_btn=Button(countdown_timer,font=f,text="Start",bg="green",command=startCd)
start_btn.pack(pady=100)



""" ------------------------------------------------------------------------------------------------------------- """


def on_closing():
	if askyesno("CLock will be closed", "Are you sure?"):
		
		world_clock.destroy()
		stop_watch.destroy()
		countdown_timer.destroy()
		root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)
world_clock.protocol("WM_DELETE_WINDOW", on_closing)
stop_watch.protocol("WM_DELETE_WINDOW", on_closing)
countdown_timer.protocol("WM_DELETE_WINDOW", on_closing)




root.mainloop() 