#!/usr/bin/env python
import psutil
import csv
import matplotlib.pyplot as plt 
from datetime import datetime
f = open('sysinfo.csv', 'a')
f.truncate(0) # need '0' when using r+
f.close
with open('sysinfo.csv', 'a', encoding='UTF8', newline='') as f:
	#Clear file before writing
	writer = csv.writer(f, delimiter = ";")
	#Writing output of system information to file for 5 minutes every 3 seconds
	difference = 0
	time_start = datetime.now()
	while difference < 5:
		time_now = datetime.now()
		difference = abs((time_start.minute - time_now.minute))
		#Gives a single float values
		cpu = psutil.cpu_percent(3)
		#Calculates percentage of utilised memory
		ram = psutil.virtual_memory().used / pow(1024, 2)
		#Writes to file
		data = [ "%s:%s:%s" % (time_now.hour, time_now.minute, time_now.second), "%.2f" % ram, cpu]
		writer.writerow(data)

with open('sysinfo.csv','r') as csvfile:
	x = []
	y = []
	z = []
	lines = csv.reader(csvfile, delimiter = ";")
	for row in lines:
		x.append(row[0])
		y.append(float(row[1]))
		z.append(float(row[2]))
	fig, axs = plt.subplots(2)
	fig.suptitle('System Information')
	plt.tight_layout()
	axs[0].plot(x, y, color = 'g', linestyle = 'solid', marker = 'none',label = "RAM Data")
	axs[0].set_title('RAM Data')
	axs[0].set_xlabel('Time, HH:MM:SS')
	axs[0].set_ylabel('RAM Used, Mb')
	axs[0].tick_params(labelrotation=45)
	axs[1].plot(x, z, color = 'b', linestyle = 'solid', marker = 'none',label = "CPU Data")
	axs[1].set_title('CPU Data')
	axs[1].set_xlabel('Time, HH:MM:SS')
	axs[1].set_ylabel('CPU Load, %')
	axs[1].tick_params(labelrotation=45)

	plt.legend()
	plt.show()
	plt.savefig('graphs.jpg')