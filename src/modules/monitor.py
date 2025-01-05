import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as anim 
import rd6006 as rd 
import time

def monitor_voltage(psu, event):
	while(True):
		if not event.isSet():
			v = psu.voltage
			print(f"Voltage read is: {v}")
		else:
			print("Thread terminated by event")
			break
		time.sleep(0.5)
