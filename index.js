const {SerialPort} = require('serialport')

let port=null;

const initBoard=async()=>{
    let port=null;
    let awlPorts=await SerialPort.list()
    awlPorts.forEach(awlPort=>{
        console.log("Port: ", awlPort);
    })
    if(!port)
        setTimeout(initBoard, 1000)
}
initBoard();


