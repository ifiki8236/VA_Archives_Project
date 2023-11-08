const loadImages = (boxID) => {
    const loadedImages = [];
    const globalLoadingScreen = document.getElementById('globalLoadingScreen');
    // const footerText = document.getElementById('footerText');
    // Fetch all images from the server
    fetch(`http://127.0.0.1:5000/retrieve_images/${boxID}`, {
        // credentials: 'include'  // Include credentials with the request
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        console.log('Data pulled from DB');
        return response.json();
    })
    .then(data => {
        data.forEach(image => {
            loadedImages.push(image);
            const imageDiv = document.createElement('div');
            imageDiv.classList.add('image-item');
            const imgElement = document.createElement('img');
            imgElement.src = 'data:image/jpeg;base64,' + image.photo_data;
            imgElement.alt = 'Image ' + image.id;
            imageDiv.appendChild(imgElement);
            document.querySelector('.photo-gallery').appendChild(imageDiv);
        });
        globalLoadingScreen.style.display = 'none';  // Hide the loading screen after fetching
        // footerText.textContent = "";
    })
    .catch(error => {
        console.error('Fetch error:', error);
        globalLoadingScreen.style.display = 'none';  // Hide the loading screen after fetching
        // footerText.textContent = "Error loading content, refresh required...";
    });
};
document.addEventListener('DOMContentLoaded', () => {
    console.log('DOMContentLoaded event fired');

    const urlParams = new URLSearchParams(window.location.search);
    const boxID = urlParams.get('boxId');
  
    if (boxID) {
        console.log('boxID found:', boxID);
        loadImages(boxID); // This should only log once unless the page is reloaded
    } else {
        console.error('No boxID provided in URL.');
    }
});

