
import os
import pandas as pd
import pwd
from time import sleep
tot_cpu=cpu_prev=0
total_memory=0
df={}
uname=pname=0
##### Store Total_memory
with open('/proc/meminfo') as cf:
			data_cpu=cf.readlines()
			for line in data_cpu:
				total_memory=float(line.strip().split()[1:2][0])*1000
				break

def get_names(pid):
	
   	try:
		with open("/proc/" + str(pid) + "/comm","r") as file_pname:
			pname = file_pname.readlines()[0].split("\n")[0]
			#print(pname)
		with open("/proc/" + str(pid) + "/status", "r") as file_uid:
			data=file_uid.readlines()
			for line in data:
				columns = line.split("\t")
				if columns[0] == "Uid:":
					uid=columns[1]
                          
					uname=pwd.getpwuid(int(uid)).pw_name
					return uname,pname
					break
		return uname,pname
		 
	except Exception as e:
		print(e)

def get_vmsize():
	vm_siz=0
	with open('/proc/meminfo') as cf:
			data_cpu=cf.readlines()
			for line in data_cpu:
				if line.strip().split()[0]=='MemTotal:':
					vm_siz=float(line.strip().split()[1:2][0])*1000
				if line.strip().split()[0]=='SwapTotal:':
					vm_siz=vm_siz+float(line.strip().split()[1:2][0])*1000
					break
	return vm_siz



class Process():
 def __init__(self):
    self.proc_text=''
 def getProcess(self):
    self.proc_text='' 
    for_one_pass = True
    need_vm = True
    close = 0
    cpu_prev=0	
    while True:
	    with open('/proc/stat', "r") as cf:
			data_cpu=cf.readlines()
			field=[]
			for line in data_cpu:
				  field=line.split()[1:]
				  break
			tot_cpu=float(field[0])+float(field[2])+float(field[3])
			diff=tot_cpu-cpu_prev
			cpu_prev = tot_cpu
			

	    if not for_one_pass:
		    for p_id in os.listdir("/proc"):
			  if p_id.isdigit():
				try:
					path_stat = "/proc/" + str(p_id) + "/stat"

					if need_vm == True:
						vmsize = get_vmsize()
						need_vm = False

					with open(path_stat) as f:
						data = f.readlines()[0].split()
						p_cpu = float(data[13]) + float(data[14]) #jiffy
						p_vm = float(data[22]) #bytes
						p_mem = float(data[23]) * 2048  #converting pages to bytes

						

						p_uname, p_pname = get_names(p_id)
						
						if not p_uname:
							break

						p_cpu_util = (p_cpu / tot_cpu) * 100 #percentage
						p_vm_util = (p_vm / get_vmsize()) * 100 #percentage
						p_mem_util = (p_mem /  total_memory) * 100 #percentage
						
		
						st=str(p_uname)+' 		'+str(p_pname)+' 		'+str(p_cpu_util)+' 			'+str(p_vm_util)+' 				'+str(p_mem_util)
						self.proc_text=self.proc_text+st+'\n'	
								 
					
				except Exception as e:
				   print(e)
	    for_one_pass = False
	    if close >=5:
	    	break
	    close+=1

	    
	




