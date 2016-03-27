#!/usr/bin/env python
"""
Title:   Wordpress backup script
Author:  prolinuxhub.com
Date:	 Sun 27 2016
"""
import sys,os,statvfs

#Variables



# Check to make sure backup directory has enough space for backup job
def check_space_for_backup(backup_path):
	size = os.statvfs(backup_path)
	free_space=(size.f_bavail * size.f_frsize) / 1024
	return free_space





# Backup web root
#def backup_webroot():

# Backup sql database
#def backup_database():

def main():
	if check_space_for_backup('/home/boris/nas') < 100:
		print 'SMALLER THEN NUMBR';
	
	
	
if __name__ == '__main__':
	main()

