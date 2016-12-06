#!/usr/bin/python
# encoding: utf-8

import sys
import argparse
from workflow import Workflow
from DictionaryServices import *

import urllib2
import urllib
import json
import re

def main(wf):
    parser = argparse.ArgumentParser()
    parser.add_argument('--query', dest='query', default='')
    args = parser.parse_args(wf.args)
    token=args.query.strip()#.replace(' ','%20').replace('?','%3F').replace('/','%2F')
    searchword=token#.decode('utf-8')
    
    wordrange = (0, len(searchword))
    dictresult = DCSCopyTextDefinition(None, searchword, wordrange)
    
    
    
    if not dictresult:
        wf.add_item('No results')
        wf.send_feedback()
    else:
        result=dictresult.encode('utf-8').split('\n')
        for i in range(min(10,len(result))):
            wf.add_item(result[i].decode('utf-8'))
        wf.send_feedback()

    return 0
    
if __name__==u"__main__":
    wf=Workflow()
    sys.exit(wf.run(main))
    