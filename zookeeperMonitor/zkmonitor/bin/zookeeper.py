# -*- coding: utf-8 -*-
"""
Created on Mon May 28 15:27:00 2018

@author: Administrator
"""
import yaml
import commands
import os
import time
import requests
import json
#os.system("echo stat | nc 10.211.30.83 2181")
#info = commands.getoutput('echo mntr | nc 10.211.30.83 2181')
#print info
falcon_client = "http://127.0.0.1:1988/v1/push"
ts = int(time.time())
f=open("../conf/zookeeper.conf")
y = yaml.load(f)
f.close()
#print y
zk_items = y["items"]
for zk_ins in zk_items:
	zookeeper_update_list=[]
	ip = zk_ins["addr"]
	port = zk_ins["port"]
	info = commands.getoutput('echo mntr | nc '+ ip + ' ' + port)
	#print info
	zk_list= info.split('\n')
	#print zk_list[0]
	tag = zk_list[0].replace("\t","=")
	for x in range(1,len(zk_list)):
		#print zk_list[x]
		#key_item_dict={"endpoiin"}
		tmp = zk_list[x].split("\t")
		if tmp[0] == "zk_server_state":
			value = 0 if (tmp[1]=="follower") else 1
			#print value
    			key_item_dict =  {"endpoint": ip + " Zookeeper", "metric": tmp[0], "tags":tag , "timestamp":ts, "value": value, "step": 60, "counterType": "GAUGE"}
		else:
    			key_item_dict =  {"endpoint": ip + " Zookeeper", "metric": tmp[0], "tags":tag , "timestamp":ts, "value":  tmp[1], "step": 60, "counterType": "GAUGE"}
		zookeeper_update_list.append(key_item_dict)
	info = commands.getoutput('echo conf | nc '+ ip + ' ' + port)
	#print info
	zk_list= info.split('\n')
	for x in range(0,len(zk_list)):
		tmp = zk_list[x].split("=")
		if tmp[1].isdigit():
			key_item_dict =  {"endpoint": ip + " Zookeeper", "metric": tmp[0], "tags":tag , "timestamp":ts, "value":  tmp[1], "step": 60, "counterType": "GAUGE"}
		zookeeper_update_list.append(key_item_dict)

	#info = commands.getoutput('echo cons | nc '+ ip + ' ' + port)
	#zk_list= info.split('\n')

	r = requests.post(falcon_client,data=json.dumps(zookeeper_update_list))		

	
#print zk_items

