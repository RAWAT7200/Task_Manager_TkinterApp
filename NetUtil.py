import os
import time
import subprocess

class NET():
  def __init__(self):
  	self.bandwidth=1000*(10 **6)
  	self.curr_data_trans=0
	self.prev_data_trans_receive=0
	self.curr_data_trans_receive=0
	self.prev_data_trans_sent=0
	self.curr_data_trans_sent=0
	self.x = 0
	self.net_util=0
	self.net_text=''
  def getNetStat(self):
  	self.net_text=''
  	with open("/proc/net/dev") as f:
		device = []
		one_pass = 1
		
		for lines in f.readlines():
			if one_pass > 2:
				# print(lines)
				
				data= lines.split()

				if "lo" in data[0]:
					pass
				else:
					device.append(data[0].split(":")[0])
					self.curr_data_trans_receive=float(data[1])
					self.curr_data_trans_sent=float(data[9])
					self.curr_data_trans=(self.curr_data_trans_receive-self.prev_data_trans_receive) + (self.curr_data_trans_sent-self.prev_data_trans_sent)
					
					
			else:
				one_pass += 1
		self.prev_data_trans_receive=self.curr_data_trans_receive
		self.prev_data_trans_sent=self.curr_data_trans_sent
		
		



		

	 
