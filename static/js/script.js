// Audio recording and transcription function
async function recordAndTranscribe() {
    const recordBtn = document.getElementById('recordBtn');
    const status = document.getElementById('recordingStatus');
    const transcribedTextDiv = document.getElementById('transcribedText');
    
    try {
        // Update UI to show recording state
        recordBtn.disabled = true;
        recordBtn.innerHTML = '⏹️';
        status.textContent = 'Recording...';
        status.style.color = '#dc3545';
        
        // Call the audio_to_text endpoint
        const response = await fetch('/audio_to_text', {
            method: 'GET'
        });
        
        const result = await response.json();
        
        if (result.success) {
            // Show transcribed text
            transcribedTextDiv.textContent = result.transcribed_text;
            transcribedTextDiv.style.display = 'block';
            status.textContent = 'Recording complete';
            status.style.color = '#28a745';
        } else {
            throw new Error(result.error || 'Failed to record audio');
        }
        
    } catch (error) {
        console.error('Error recording audio:', error);
        status.textContent = 'Error occurred';
        status.style.color = '#dc3545';
        transcribedTextDiv.textContent = 'Error: ' + error.message;
        transcribedTextDiv.style.display = 'block';
    } finally {
        // Reset button state
        recordBtn.disabled = false;
        recordBtn.innerHTML = '🎤';
        setTimeout(() => {
            status.textContent = 'Not recording';
            status.style.color = '#666';
        }, 2000);
    }
}

// Image upload and analysis function
async function uploadAndAnalyzeImage() {
    const fileInput = document.getElementById('imageUpload');
    const imagePreview = document.getElementById('imagePreview');
    const imageTextDiv = document.getElementById('imageText');
    
    if (!fileInput.files[0]) {
        alert('Please select an image first');
        return;
    }
    
    try {
        // Show loading state
        imagePreview.innerHTML = '<div class="text-center"><div class="spinner-border" role="status"><span class="visually-hidden">Loading...</span></div><p>Analyzing image...</p></div>';
        
        // Create form data
        const formData = new FormData();
        formData.append('image', fileInput.files[0]);
        
        // Call the image_to_text endpoint
        const response = await fetch('/image_to_text', {
            method: 'POST',
            body: formData
        });
        
        const result = await response.json();
        
        if (result.success) {
            // Show analysis result
            if (imageTextDiv) {
                imageTextDiv.textContent = result.image_text;
                imageTextDiv.style.display = 'block';
            }
            // Update preview to show success
            const file = fileInput.files[0];
            const reader = new FileReader();
            reader.onload = function(e) {
                imagePreview.innerHTML = `
                    <div class="text-center">
                        <img src="${e.target.result}" style="max-width: 100%; max-height: 200px; border-radius: 10px; box-shadow: 0 5px 15px rgba(0,0,0,0.2);">
                        <p style="margin: 10px 0 0 0; font-size: 0.8rem; opacity: 0.8;">${file.name}</p>
                        <p class="text-success mt-2">✓ Analysis complete</p>
                    </div>
                `;
            };
            reader.readAsDataURL(file);
        } else {
            throw new Error(result.error || 'Failed to analyze image');
        }
        
    } catch (error) {
        console.error('Error analyzing image:', error);
        imagePreview.innerHTML = '<div class="text-danger">Error analyzing image: ' + error.message + '</div>';
        if (imageTextDiv) {
            imageTextDiv.textContent = 'Error: ' + error.message;
            imageTextDiv.style.display = 'block';
        }
    }
}

// Image preview function
function previewImage() {
    const fileInput = document.getElementById('imageUpload');
    const imagePreview = document.getElementById('imagePreview');
    const file = fileInput.files[0];
    
    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            imagePreview.innerHTML = `
                <div class="text-center">
                    <img src="${e.target.result}" style="max-width: 100%; max-height: 200px; border-radius: 10px; box-shadow: 0 5px 15px rgba(0,0,0,0.2);">
                    <p style="margin: 10px 0 0 0; font-size: 0.8rem; opacity: 0.8;">${file.name}</p>
                    <button onclick="uploadAndAnalyzeImage()" class="btn btn-success mt-2">Analyze Image</button>
                </div>
            `;
        };
        reader.readAsDataURL(file);
    } else {
        imagePreview.innerHTML = 'No image selected';
    }
}

// Initialize event listeners when the page loads
document.addEventListener('DOMContentLoaded', function() {
    // Record button event listener
    const recordBtn = document.getElementById('recordBtn');
    if (recordBtn) {
        recordBtn.addEventListener('click', recordAndTranscribe);
    }
    
    // Image upload event listener
    const imageUpload = document.getElementById('imageUpload');
    if (imageUpload) {
        imageUpload.addEventListener('change', previewImage);
    }
});
