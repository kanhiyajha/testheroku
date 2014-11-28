
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.template import RequestContext
from django.template import loader

import re
import subprocess
@csrf_exempt
def method(request):
    return render(request,'data.html')

@csrf_exempt
def setdata(request):
    list1=[]
    name=request.POST['name1']
    no=request.POST['no']
    list1.append(str(name))
    list1.append(str(no))
    list2=[]
    list2.append(list1)
	
    device_re = re.compile("Bus\s+(?P<bus>\d+)\s+Device\s+(?P<device>\d+).+ID\s(?P<id>\w+:\w+)\s(?P<tag>.+)$", re.I)
    df = subprocess.check_output("lsusb", shell=True)
    devices = []
    for i in df.split('\n'):
        if i:
            info = device_re.match(i)
            if info:
                dinfo = info.groupdict()
                dinfo['device'] = '/dev/bus/usb/%s/%s' % (dinfo.pop('bus'), dinfo.pop('device'))
                devices.append(dinfo)
    print devices
    get_drives()
    print list2
  
    return render(request,"data.html",{'list1':list2})

@csrf_exempt
def display(request,list1):
    print "data",list1
  
    
    return render(request,'data.html')


import string  
from ctypes import windll  
import time  
import os  
def get_drives():  
    drives = []  
    bitmask = windll.kernel32.GetLogicalDrives()  
    for letter in string.uppercase:  
        if bitmask & 1:  
            drives.append(letter)  
        bitmask >>= 1  
    return drives  
if __name__ == '__main__':  
    before = set(get_drives())  
    pause = raw_input("Please insert the USB device, then press ENTER")  
    print ('Please wait...')  
    time.sleep(5)  
    after = set(get_drives())  
    drives = after - before  
    delta = len(drives)  
    if (delta):  
        for drive in drives:  
            if os.system("cd " + drive + ":") == 0:  
                newly_mounted = drive  
                print "There were %d drives added: %s. Newly mounted drive letter is   %s" %   (delta, drives, newly_mounted)  
    else:  
        print "Sorry, I couldn't find any newly mounted drives."  
