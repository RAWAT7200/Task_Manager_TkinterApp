import platform
import datetime
import os
from time import sleep
import pickle

       
class CPU:
    def __init__(self):  
      self.time_int=5
      self.utilisation_intr=0
      self.utilisation_ctxt=0
      self.utilisation=0
      self.memory_utilisation=0
      self.total_memory=0
      self.available_memory=0
      self.curr_intr=self.prev_intr=self.curr_ctxt=self.prev_ctxt=0
      self.curr_user=self.curr_sys=self.prev_user=self.prev_sys=self.curr_ideal=self.prev_ideal=0
      self.curr_free_memory=self.prev_free_memory=0;
      

    def getInfoCpu(self):
      self.getCpuInfo()
      sts=str(self.utilisation_ctxt)+'        '+str(self.utilisation)+'       '+str(self.utilisation_intr)+'           '+str(self.available_memory)+'               '+str(self.total_memory)+'                       '+str(self.memory_utilisation)       
      return sts

    def getCpuInfo(self):
  
        with open('/proc/meminfo') as fs:
          fields=[float(column) for column in fs.readline().strip().split()[1:2]]
          self.total_memory=fields[0]/1000
          fields=[float(column) for column in fs.readline().strip().split()[1:2]] 
          self.curr_free_memory= fields[0]

          self.available_memory = ((self.curr_free_memory + self.prev_free_memory) / 2)/1000
       
          self.memory_utilisation= self.available_memory /self.total_memory

          self.prev_free_memory=self.curr_free_memory
          

        with open('/proc/stat') as f:
         fields = [float(column) for column in f.readline().strip().split()[1:]]
         self.curr_user,self.curr_sys,self.curr_ideal = fields[0], fields[2],fields[3]
         delta_usage=self.curr_user - self.prev_user + self.curr_sys - self.prev_sys
         delta_total=self.curr_user - self.prev_user + self.curr_sys - self.prev_sys + self.curr_ideal - self.prev_ideal 
         self.prev_user, self.prev_sys,self.prev_ideal = self.curr_user,self.curr_sys,self.curr_ideal 
        
         x=1       
         data=f.readlines()
         self.cur_intr=self.curr_ctxt=0
         for line in data:
          field_intr = line.strip().split()
          if(field_intr[0]=="intr"):  
           self.curr_intr=float(field_intr[1])
          if(field_intr[0]=="ctxt"):
           self.curr_ctxt=float(field_intr[1])


        
        self.utilisation_intr=(100.0 * (self.curr_intr-self.prev_intr)/100 ) 
 
        self.prev_intr=self.curr_intr  
        
        self.utilisation_ctxt= 100.0 * (self.curr_ctxt-self.prev_ctxt)/100   
         
        self.prev_ctxt=self.curr_ctxt
        if(delta_total>0):
         self.utilisation = 100.0 * (delta_usage /delta_total)
        """         
        print('\n Context Switch',self.utilisation_ctxt)
        print('\n cpu utilisation is ', self.utilisation)
        print('\n no of interrupts is ',self.utilisation_intr)
        print('\n\n\n ----MEMORY DATA------- ')
        print('\nAvailable_Memory',self.available_memory)
        print('\nTotal Memory',self.total_memory)
        print('\n Memory Utilisation(%)',self.memory_utilisation*100)
        print('\n')
        """
          
        
         
        
        
       



    







