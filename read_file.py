#!/usr/bin/python

file_name = raw_input("File name to open = ")
file_open = open(str(file_name),"r")

for files in file_open.readlines():
	print(files)

file_open.close()

