function startRecording() {
    navigator.mediaDevices.getUserMedia({ audio: true })
        .then(stream => {
            const mediaRecorder = new MediaRecorder(stream);
            mediaRecorder.start();
            mediaRecorder.ondataavailable = function(event) {
                const formData = new FormData();
                formData.append('audio', event.data);
                formData.append('target_language', document.getElementById('target_language').value);
                
                fetch('/process_audio', {
                    method: 'POST',
                    body: formData
                })
                .then(response => response.json())
                .then(data => {
                    document.getElementById('recognized_text').textContent = data.recognized_text || 'Error in recognition';
                    document.getElementById('translated_text').textContent = data.translated_text || 'Error in translation';
                })
                .catch(error => console.error('Error:', error));
            };
        })
        .catch(error => console.error('Error accessing media devices.', error));
}
