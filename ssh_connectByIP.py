#!/usr/bin/env python 
"""
Create iplist.csv file see example below

1,systemname1,loginuserroot,port,192.168.0.3
2,best,root,22,192.168.0.1
3. To have coloref dispaly instal 
pip and install termcoclor module 

sudo apt-get install python-pip
sudo pip install termcolor
"""


import sys, os
from termcolor import colored
# VARIABLES
file_name = 'iplist.csv'


# FUNCTIONS 
def read_file():
	file = open(file_name)
	for line in file:
		if line[:1] != "#":
			print colored(line, 'green')
			print colored('------------------------------------------', 'red')
def start_ssh_connection(my_choice):
	file = open(file_name)
	for line in file:
		columns = line.split(',')
		vm_number = columns[0].strip()
		vm_number = int(vm_number)
		
		if vm_number == my_choice:
			# columns[-1]  ip address 
			# columns[-2]  port number 
			# columns[-3]  username
		   
			#os.system("ssh " + columns[-1] + " -p " +columns[-2]  + " -l " + columns[-3])
			os.system("ssh "+columns[-3]+"@"+columns[-1]+ " -p " + columns[-2])
		
		

# ACTION
read_file()

my_choice = input('System number: ')
my_choice = int(my_choice)
start_ssh_connection(my_choice)
