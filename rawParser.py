from collections import deque
import time
import commands


    

def parseString(serialString, stack):
    
    if(len(serialString)>0):
        byte=serialString[0]
        if byte>=0x80:
            arr=[byte,]
            stack.append(arr)
        else:
            stack[len(stack)-1].append(byte)
        serialString=serialString[1:]
        return parseString(serialString, stack)
    return stack
        
    


def parseBoardUpdate(data, passStack):
     buf.append({commands.SQUARES[data[4]]:commands.PIECES[data[3]]})
    
def parseBoardState(data, msgStack):
    items = deque(data)
    items.popleft()
    items.popleft()
    items.popleft()
    
    print("parseBoardState")
    event={"time":time.time(), "board":{}}
    i=0
    buf=[]
    for item in items:
        buf.append({commands.SQUARES[i]:commands.PIECES[item]})
        i=i+1
    msgStack.append(buf)
    msgStack.append(event)
    
def parseSn(data):
    return(data[3:11].hex(":"))
    
  
