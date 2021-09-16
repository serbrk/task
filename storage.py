#!usr/bin/env python3
import json
from os import name
import argparse
parser = argparse.ArgumentParser ()
parser.add_argument('--key',type=str)
parser.add_argument('--val',type=str)
args = parser.parse_args()
key = args.key
val = args.val
data=[]
data=str(data)
with open('storage.data', 'r') as f: 
   data = json.load(f)
if args.val is not None:
        data.append({
        'key':key,
        'val':val
    })
        with open('storage.data', 'w', encoding='utf-8')  as storage:
           a=json.dump(data, storage,indent=3,separators=(',',': '))
else:    
        with open('storage.data', 'r') as f:
            array = json.load(f)
        for i in array:
            if i["key"] == key:
                print(i["val"], end=',')