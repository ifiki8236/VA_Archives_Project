let currentPage = 1;
let allImagesLoaded = false;
let totalCount = 0;
const pageSize = 12; // Assuming 10 images per page
let isLoading = false; // New flag to track loading state


const loadImages = (boxID,currentPage) => {
    if (allImagesLoaded || isLoading) return;

    isLoading = true
    const loadedImages = [];
    const globalLoadingScreen = document.getElementById('globalLoadingScreen');
    const footerText = document.getElementById('footerText');
    let loadedCount = 0; // Counter for loaded images

    fetch(`http://127.0.0.1:5000/retrieve_images/${boxID}?page=${currentPage}&size=${pageSize}`)
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        console.log('Data pulled from DB');
        return response.json();
    })
    .then(data => {
        if (data.length === 0) {
            allImagesLoaded = true;
            return;
        }
        const pulledCount = data.length; // Total number of images to load
        // console.log(pulledCount)
        totalCount += pulledCount
        console.log('Current Page :',currentPage)
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
                // footerText.textContent = `Loading images... ${loadedCount}/${totalCount}`;
                if (totalCount === totalCount) {
                    globalLoadingScreen.style.display = 'none'; // Hide loading screen after all images are loaded
                    // footerText.textContent = `Images loaded - ${totalCount}/${totalCount}`;
                }
            };
            imgElement.onerror = () => {
                footerText.textContent = 'Error loading some images';
            };
            imageDiv.appendChild(imgElement);
            document.querySelector('.photo-gallery').appendChild(imageDiv);
        });
        if (data.length < pageSize) {
            allImagesLoaded = true;  // No more images to load
            console.log(`Total of Images loaded : ${totalCount}`)
        }
        isLoading = false
    })
    .catch(error => {
        console.error('Fetch error:', error);
        globalLoadingScreen.style.display = 'none';  // Hide the loading screen after fetching
        footerText.textContent = "Error loading content, refresh required...";
        isLoading = false
    });
};
document.addEventListener('DOMContentLoaded', () => {
    console.log('DOMContentLoaded event fired');

    const urlParams = new URLSearchParams(window.location.search);
    const boxID = urlParams.get('boxId');
  
    if (boxID) {
        console.log('boxID found:', boxID);
        loadImages(boxID,currentPage); // Initial load
        currentPage++;

    } else {
        console.error('No boxID provided in URL.');
    }
    window.addEventListener('scroll', () => {
        if ((window.innerHeight + window.scrollY) >= document.body.offsetHeight - 100 && !allImagesLoaded && !isLoading) {
            globalLoadingScreen.style.display = 'flex';
            loadImages(boxID, currentPage);
            currentPage++;
        }
    });
})





