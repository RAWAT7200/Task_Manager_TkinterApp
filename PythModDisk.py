import platform
import datetime
import os
from time import sleep
class DISK():
 def __init__(self):
   self.prev_read=0
   self.prev_write=0
   self.disk_curr_sum=0
   self.block_curr_sum=0
   self.disk_prev_sum=0
   self.block_prev_sum=0
   self.bprev_read=0
   self.bprev_write=0
   self.nreads=0
   self.nwrite=0
   self.nread=0
   self.bnwrite=0
   self.curr_write=0
   self.curr_read=0
   self.bcurr_read=0
   self.bcurr_write=0
 def getDiskInfo(self):
    self.getDiskData()
    st=str(self.nread)+'                '+str(self.nwrite)+'                '+str(self.bnread)+'                '+str(self.bnwrite)+'               '+str(self.disk_curr_sum)+'               '+str(self.block_curr_sum)
    return st  

 def getDiskData(self):
    with open('/proc/diskstats') as fs:
     data=fs.readlines()
     for line in data:
       fields=line.split()   
       if(fields[2]=="sda"):
          self.curr_read=float(fields[3])
          self.curr_write=float(fields[7])  
          self.bcurr_read=float(fields[5])
          self.bcurr_write=float(fields[9])
          self.nread=self.curr_read-self.prev_read
          self.nwrite=self.curr_write-self.prev_write
          self.bnread=self.bcurr_read-self.bprev_read  
          self.bnwrite=self.bcurr_write-self.bprev_write
        
          self.disk_curr_sum=(self.curr_read + self.curr_write - self.prev_read + self.prev_write)* 512 / 10**6
          self.block_curr_sum=(self.bcurr_read + self.bcurr_write - self.bprev_read + self.bprev_write)* 512/ 10**6
          self.disk_prev_sum=self.disk_curr_sum
          self.block_prev_sum=self.block_curr_sum
 
          self.prev_read=self.curr_read
          self.prev_write=self.curr_write
          self.bprev_read=self.bcurr_read
          self.bprev_write=self.bcurr_write
          break
      
      
    
