from collections import deque
import time
import commands


    

def parseString(serialString, stack):
    
    if(len(serialString)>0):
        byte=serialString[0]
        if byte==0x8e or byte==0x86 or byte==0x91:
            arr=[byte,]
            stack.append(arr)
        else:
            ln=len(stack)-1
            stack[ln].append(byte)
        serialString=serialString[1:]
        return parseString(serialString, stack)
    return stack
        
    


def parseBoardUpdate(data, passStack): 
        print("parseBoardUpdate")
        passStack.append({commands.SQUARES[data[3]]:commands.PIECES[data[4]], "time":time.time()})
    
def parseBoardState(data, msgStack, passStack):
    items = deque(data)
    items.popleft()
    items.popleft()
    items.popleft()
    
    print("parseBoardState")
    event={"time":time.time(), "board":[], "vectors":passStack.copy()}
    i=0
    for item in items:
        event["board"].append({commands.SQUARES[i]:commands.PIECES[item]})
        i=i+1
    #msgStack.append({"field":buf, time:time.time()})
    msgStack.append(event)
    
    
def parseSn(data):
    return ''.join(str(x)+"_" for x in data[3:11])
    
  
