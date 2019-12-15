import platform
import datetime
import os
import pwd
import ipaddress
# import pandas as pd
from time import sleep
final_list=[]

def compare_inode(self,inode,local_address,remote_address,uid, c_type):
		for file in os.listdir("/proc"):
			if file.isdigit():
		 		# print("in compare loop")
				try:
					path = "/proc/" + str(file) +"/fd"
					# print("in try")
					for fd_files in os.listdir(path):
					    socket = os.stat(path + "/" + fd_files).st_ino
						# print(socket, inode)
					    if(socket==inode):
						    print("inode:  ",inode, "socket from code :", socket)
						    print("match")
						    loc_list = []
                               
						    with open("/proc/" + str(file) +"/comm") as file_uname:
							   process_name = file_uname.readlines()

						    uname=pwd.getpwuid(uid).pw_name
						    tcp_udp_line=str(c_type)
						    tcp_udp_line=tcp_udp_line+'		 '+str(local_address)
						    tcp_udp_line=tcp_udp_line+' 	      '+str(remote_address)
						    tcp_udp_line=tcp_udp_line+' 	      '+str(inode)+'		    '+str(process_name[0].split("\n")[0])+'		    '+str(uname) 
                            
						    print(tcp_udp_line+'\n')
						    self.getTCP_UDP=self.getTCP_UDP+tcp_udp_line+'\n'
						      
				except Exception as e:
					print(e)
def getIp(s):
    bytes_b=["".join(x) for x in zip(*[iter(s)]*2)]
    bytes_b=[int(x,16) for x in bytes_b]
    return ".".join(str(x) for x in reversed(bytes_b))   
                    
class TCP():
  def __init__(self):
   self.getTCP_UDP=''	
  def getTCPUDP(self):
    try:
    	self.getTCP_UDP=''
        with open("/proc/net/tcp","r") as f:
            start_read = False
            for line in f.readlines():
		        if start_read == False:
			       start_read = True
		        else:
			        field =  line.split()
			        print(field)
			        local_address=(field[1]).split(':')[0]
			        remote_address=(field[2]).split(':')[0]
			        inode = int(field[9])
			        uid = int(field[7])
			        compare_inode(self,inode,getIp(local_address),getIp(remote_address), uid, c_type = "tcp")
    except  :
        pass
    try:
        with open("/proc/net/udp","r") as f:
            start_read = False
            for line in f.readlines():
                if start_read == False:
                   start_read = True
                else:
                    field =  line.split()
                    print(field)
                    local_address=field[1]
                    remote_address=field[2]
                    inode = int(field[9])
                    uid = int(field[7])
                    compare_inode(self,inode,getIp(local_address),getIp(remote_address),uid, c_type = "udp")
    except  :
        pass 

   
       
