async function send_audio(audioBlob) {
    const formData = new FormData();
    formData.append('audio', audioBlob, 'audio.mp3');
    const response = await fetch('/api/mp3tonotes', {
        method: 'POST',
        body: formData
    });
    const result = await response.json();
    console.log(result);
    console.log(result.transcription)
}

navigator.mediaDevices.getUserMedia({ audio: true })
  .then(stream => {
    const mediaRecorder = new MediaRecorder(stream);
    

    const audioChunks = [];
    mediaRecorder.addEventListener("dataavailable", event => {
      audioChunks.push(event.data);
    });

    record = document.getElementById('record')

    record.onclick = () => {
        mediaRecorder.start();
    }
    
    stopRecord = document.getElementById('stopRecord')

    stopRecord.onclick = () => {
        mediaRecorder.stop();
    }
    
    mediaRecorder.addEventListener("stop", async () => {
      const audioBlob = await getWaveBlob(audioChunks);
      send_audio(audioBlob)
    });
  }
);
