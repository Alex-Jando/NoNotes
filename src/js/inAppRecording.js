

navigator.mediaDevices.getUserMedia({audio:true})
      .then(stream => {handlerFunction(stream)})


function handlerFunction(stream){
    rec = new MediaRecorder(stream);
    rec.ondataavailable = e => {
        audioChunks.push(e.data);
        if (rec.state == "inactive"){
            let blob = new Blob(audioChunks,{type:'audio/mpeg-3'});
            recordAudio.src= Url.createObjectURL(blob);
            recordAudio.controls=true;
            recordAudio.autoplay=true;
            sendData(blob) 
        }
    }
}     

sendData(data){
    
}

record.onclick = e => {
    record.disabled = true;
    record.style.backgroundColor = "blue";
    stopRecord.disabled = false; 
    audioChunks =[];
    rec.start();
}
stopRecord.onclick = e => {
    record.disabled = false;
    record.style.backgroundColor = "red";
    stopRecord.disabled = true; 
    audioChunks =[];
    rec.stop();
}

