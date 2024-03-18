

import serial
import time, threading
import serial.tools.list_ports
import requests


import commands
import rawParser
from collections import deque

msgStack= deque([]) 
passStack= []
serialNo=0

def upload(sn):
    url="http://localhost:3301/api/chess"
    while True:
        time.sleep(.5)
        print 
        if len(msgStack)>0:
            try:
                x = requests.post(url, json = msgStack[len(msgStack)-1])
                if x.json()>0:
                    msgStack.pop();
            except:
                print("ERROR on upload")
    
def initSendQuery(sn):
    serialNo=sn
    print(serialNo)
    threadUpload = threading.Thread(target=upload, args=(sn,))
    threadUpload.start()
    
    
def receiveMessage(ser):
    
    #try:
        while True:
            
            time.sleep(.2)
            #bytesToRead = ser.inWaiting()
            #bytesToRead=100
            #if bytesToRead>0:
            serialString = ser.readline()
            
            if len(serialString)>0:
                print("receiveMessage", len(serialString))
                
                buf=rawParser.parseString(serialString, [] )
                
                for item in buf:
                    arr=bytearray(item)
                    if arr[0]==0x8e:
                        rawParser.parseBoardUpdate(arr, passStack)
                        ser.write(bytearray([commands.DGT_SEND_BRD]))
                    else:
                        if arr[0]==0x86 and arr[0]==0x86 and len(arr)==67:
                            rawParser.parseBoardState(arr, msgStack)
                            
                        else:
                            if arr[0]==0x91 and arr[2]==0x08:
                                serialNo=rawParser.parseSn(arr)
                                initSendQuery(serialNo)
                            else:
                                print(arr.hex(" "))
        
    #except:
        #print("receive thread Err")
        #receiveMessage(ser)
   
def findDevice():
    print("find")
    find=False
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        if p.description=="US232R" :
            initDevice(p)
            find=True
    if find==False:
        print(find)
        time.sleep(5)
        findDevice()
        
def initDevice(dev):
    try:
        print (dev.device)
        ser = serial.Serial( port=dev.device, baudrate=9600, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
        
        time.sleep(1)
        flags={"stop":False}
        threadReceive = threading.Thread(target=receiveMessage, args=(ser,))
        threadReceive.start()
        
        ser.write(bytearray([commands.DGT_RETURN_SERIALNR]))
        ser.write(bytearray([commands.DGT_SEND_UPDATE_BRD]))
        #ser.write(bytearray([commands.DGT_SEND_BRD]))
        time.sleep(1)
       
        while True:
            time.sleep(10)
            ser.write(bytearray([commands.DGT_SEND_BRD]))
    except:
        print("error")
        flags["stop"]=True

        time.sleep(5)
        findDevice()
    
findDevice()
        
        
    



