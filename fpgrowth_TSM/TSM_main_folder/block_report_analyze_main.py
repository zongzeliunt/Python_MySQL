#!/usr/bin/python
#coding:utf-8
import sys
sys.path.append("/home/ares/UNT_work/SLEBD/SLEBD_work/python_code_folder")
import os
import re 
import time 
import global_APIs
import sequence_pattern_mining

def main (cmd_1, cmd_2 = ""):
	#sequence_pattern_mining.node_common_block_summary(cmd_1)
	
	#sub_path_list = sequence_pattern_mining.block_sequence_detect(cmd_1)
	#sequence_pattern_mining.sequence_file_test (cmd_1)





cmd_1 = sys.argv[1]
print cmd_1
if not os.path.isfile(cmd_1):
	print "please enter sequence learning file folder"
main(cmd_1)
