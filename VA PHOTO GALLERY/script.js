const loadImages = (boxID) => {
    const loadedImages = [];
    const globalLoadingScreen = document.getElementById('globalLoadingScreen');
    const footerText = document.getElementById('footerText');
    let loadedCount = 0; // Counter for loaded images

    fetch(`http://127.0.0.1:5000/retrieve_images/${boxID}`)
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        console.log('Data pulled from DB');
        return response.json();
    })
    .then(data => {
        const totalCount = data.length; // Total number of images to load
        console.log(totalCount)
        // footerText.textContent = `Loading images... 0/${totalCount}`;

        data.forEach(image => {
            loadedImages.push(image);
            loadedCount++;
            console.log(image.id, loadedCount)
            const imageDiv = document.createElement('div');
            imageDiv.classList.add('image-item');
            const imgElement = document.createElement('img');
            imgElement.src = 'data:image/jpeg;base64,' + image.photo_data;
            imgElement.alt = 'Image ' + image.id;
            imgElement.onload = () => {
                footerText.textContent = `Loading images... ${loadedCount}/${totalCount}`;
                if (loadedCount === totalCount) {
                    globalLoadingScreen.style.display = 'none'; // Hide loading screen after all images are loaded
                    footerText.textContent = `Images loaded - ${loadedCount}/${totalCount}`;
                }
            };
            imgElement.onerror = () => {
                footerText.textContent = 'Error loading some images';
            };
            imageDiv.appendChild(imgElement);
            document.querySelector('.photo-gallery').appendChild(imageDiv);
        });
    })
    .catch(error => {
        console.error('Fetch error:', error);
        globalLoadingScreen.style.display = 'none';  // Hide the loading screen after fetching
        footerText.textContent = "Error loading content, refresh required...";
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


