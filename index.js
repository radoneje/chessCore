const {SerialPort} = require('serialport')
const config=require("./config.json")
const path=require("path")




const initBoard=async()=>{
    let portDescription=null;
    let port=null;
    let awlPorts=await SerialPort.list()
    awlPorts.forEach(awlPort=>{
        if(!portDescription){
            if(awlPort.vendorId=='0403' && awlPort.productId=='6001')
            portDescription=awlPort
            serialOpen(portDescription)
        }
    })
    if(!portDescription)
        setTimeout(initBoard, 1000)
}
const serialOpen=(descr)=>{

   // var serialPort =
   const port = new SerialPort({path:"COM3",baudRate: 9600},false);
   port.on('error', function(err) { console.log('Error: ', err.message); })
   port.open(err=>{
    if(err)
        setTimeout(initBoard,1000)
   })
    
   // new SerialPort('\\\\.\\COM1', {baudrate: 9600}, true);
    /*const port = new SerialPort({
        path: '\\\\.\\COM3',//+descr.path,
        baudRate: 9600,
        //databits: 8,
        //parity: 'none'
      })
       port.open(err=>{
        if(err)
            setTimeout(initBoard,1000)
       })*/
}


initBoard();


