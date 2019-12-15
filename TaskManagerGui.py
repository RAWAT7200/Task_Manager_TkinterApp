from Tkinter import *
from ttk import *
from time import sleep
import threading
import PythModSysInfo
import PythModDisk
import PythTcp
import process
import NetUtil

tab1=tab2=tab3=tab4=tab5=0
tb1=tb2=tb3=tb4=tb5=cm=0
result_stat_cpu=''
result_stat_tcp=''
result_stat_disk=''
result_stat_process=''
result_stat_net=''
cpulist=[]
disklist=[]
proclist=[]
def callbck(event):
	
	timers=cm.current()+1
	
	tb1.delete('1.0',END)
	tb2.delete('1.0',END)
	tb3.delete('1.0',END)
	tb4.delete('1.0',END)
	tb5.delete('1.0',END)
	strs1='Context Switch   CPU Utilisation    Interrupts    Available_Memory     Total_Memory     Memory_utilisation\n'
	tb1.insert(END,strs1)
	strs2='Number_of_Reads   Number_of_writes    Bytes_Read    Bytes_Write     Disk_Current(MB)     Block_Size(MB)\n'
	tb2.insert(END,strs2)
	strs3='Connection_Type   Local_Address    Remote_Address    Inode     Process_Name     User_Name\n'
	tb3.insert(END,strs3)
	strs4='Process_UserName   Process_Name    			Process_Cpu_Util    			Process_Vm_Util     			Process_Mem_Util\n'
	tb4.insert(END,strs4)
	strs5='Network Utilisation  Bandwidth\n'
	tb5.insert(END,strs5)
	x=threading.Thread(target=thread1sleep,args=(obj1,timers))
	x.start()
	y=threading.Thread(target=thread2sleep,args=(obj2,timers))
	y.start()
	w=threading.Thread(target=thread3sleep,args=(obj3,timers))
	w.start()
	z=threading.Thread(target=thread4sleep,args=(obj4,timers))
	z.start()
	n=threading.Thread(target=thread5sleep,args=(obj5,timers))
	n.start()

    
def thread1sleep(obj1,timers):
	while(True):
	 result_stat_cpu=obj1.getInfoCpu()
	 cpulist.append(result_stat_cpu)
	 cpulist.sort(key=lambda x:float(x.split()[1])) 
	 sleep(timers)
	 tb1.delete('1.0',END)
	 strs1='Context Switch   CPU Utilisation    Interrupts    Available_Memory(MB)     Total_Memory(MB)     Memory_utilisation\n'
	 tb1.insert(END,strs1)
	 for line in cpulist:
	 	tb1.insert(END,line+'\n')

def thread2sleep(obj2,timers):
	while(True):
	 result_stat_disk=obj2.getDiskInfo()
	 disklist.append(result_stat_disk)
	 disklist.sort(key=lambda x:float(x.split()[5]))
	 sleep(timers)
	 tb2.delete('1.0',END)
	 strs2='Number_of_Reads   Number_of_writes    Bytes_Read    Bytes_Write     Disk_Current(MB)     Block_Size(MB)\n'
	 tb2.insert(END,strs2)
	 for line in disklist:
	 	tb2.insert(END,line+'\n')
	 

def thread5sleep(obj5,timers):
   strs5='Network_Util(data(bytes) per second) \n'
   tb5.insert(END,strs5)	
   while(True):	
	obj5.getNetStat()
	result_stat_net=obj5.curr_data_trans/timers
	tb5.insert(END,str(result_stat_net)+'\n')
	sleep(timers)

def thread3sleep(obj3,timers):
	while(True):
	 obj3.getTCPUDP()
	 result_stat_tcp=obj3.getTCP_UDP	
	 tb3.insert(END,result_stat_tcp+'\n')
	 sleep(timers)
	 tb3.delete('1.0',END)
	 strs3='Connection_Type   Local_Address    Remote_Address    Inode     Process_Name     User_Name\n'
	 tb3.insert(END,strs3)

def thread4sleep(obj4,timers):
   while(True):	
	obj4.getProcess()
	result_stat_process=obj4.proc_text
	tb4.insert(END,result_stat_process)
	sleep(20)
	tb4.delete('1.0',END)
	strs4='Process_UserName   Process_Name    			  Process_Cpu_Util    			  Process_Vm_Util     			  Process_Mem_Util\n'
	tb4.insert(END,strs4)
	


		

def handletab1(tb): 
    print('code for ndknkd')
def handletab2(tb): 
    print("work in progress\n")
def handletab3(tb):
    print("work in progress\n")
def handletab4(tb):      
    print("work in progress\n")
def handletab5(tb):
	print("work in progress\n")


def handlevent(event):
   selection=event.widget.select()
   tab=event.widget.tab(selection,'text')
   if tab=='CPU Utilisation':
      handletab1(tb1)
   elif tab=='Disk Utilisation':
      handletab2(tb2)
   elif tab=='TCP/UDP Connection':
      handletab3(tb3)
   elif tab=='Per Process':
      handletab4(tb4)
   elif tab=='Network Utilisation':
      handletab5(tb5)           

window=Tk()   
   


window.geometry("1000x900")
window.title('TASK MANAGER')
tab_parent=Notebook(window)
tab1=Frame(tab_parent)
tab2=Frame(tab_parent)
tab3=Frame(tab_parent)
tab4=Frame(tab_parent)
tab5=Frame(tab_parent)
tab6=Frame(tab_parent)

pro=StringVar()
cm=Combobox(tab6,textvariable=pro,values=('1','2','3','4','5','6','7','8','9','10'))
cm.current(1)
cm.pack()

tab_parent.add(tab1,text="CPU Utilisation")
tab_parent.add(tab2,text="Disk Utilisation")
tab_parent.add(tab3,text="TCP/UDP Connection")
tab_parent.add(tab4,text="Per Process")
tab_parent.add(tab5,text="Network Utilisation")
tab_parent.add(tab6,text="Timer")

tb1=Text(tab1,height=80,width=150)
scroll1=Scrollbar(window,command=tb1.yview)
tb1.configure(yscrollcommand=scroll1.set)
tb1.pack()


tb2=Text(tab2,height=80,width=200)
tb2.pack()

tb3=Text(tab3,height=80,width=200)
tb3.pack()

tb4=Text(tab4,height=80,width=200)
tb4.pack()

tb5=Text(tab5,height=80,width=200)
tb5.pack()


obj1=PythModSysInfo.CPU()
obj2=PythModDisk.DISK()
obj3=PythTcp.TCP()
obj4=process.Process()
obj5=NetUtil.NET()



cm.bind("<<ComboboxSelected>>",callbck)
tab_parent.bind('<<NotebookTabChanged>>',handlevent)
tab_parent.pack(expand=1,fill='both')
window.mainloop()


