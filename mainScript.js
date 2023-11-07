// Function to load images for a specific box
const loadImages = () => {
    const loadedImages = [];
    const globalLoadingScreen = document.getElementById('globalLoadingScreen');
    const footerText = document.getElementById('footerText');

    // Fetch all images from the server
    fetch('http://127.0.0.1:5000/retrieve_images', {
        credentials: 'include'  // Include credentials with the request
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
            document.querySelector('.gallery-image').appendChild(imageDiv);
        });
        globalLoadingScreen.style.display = 'none';  // Hide the loading screen after fetching
        footerText.textContent = "";
    })
    .catch(error => {
        console.error('Fetch error:', error);
        globalLoadingScreen.style.display = 'none';  // Hide the loading screen after fetching
        footerText.textContent = "Error loading content, refresh required...";
    });
};

// Function to load all boxes and create buttons for them
function loadBoxes() {
    fetch('http://127.0.0.1:5000/retrieve_boxes')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(boxes => {
            console.log('Boxes fetched:', boxes);
            const buttonsContainer = document.getElementById('auto-gen-bttns');
            buttonsContainer.innerHTML = ''; // Clear existing buttons if any

            boxes.forEach(box => {
                const button = document.createElement('button');
                button.textContent = box[1];
                button.classList.add('photo_categories'); // Add your specific class here
                button.onclick = function() {
                    redirectPage(box[0]);
                };
                buttonsContainer.appendChild(button);
            });
        })
        .catch(error => {
            console.error('Error fetching boxes:', error);
        });
}

// Function to redirect the page after storing box data
function redirectPage(boxId) {
    // Data to be sent in the PUT request
    let dataToSend = boxId;

    // Make a PUT request to the Flask server
    fetch('http://127.0.0.1:5000/store_box_data', {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(dataToSend),
        credentials: 'include'
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        if (data.success) {
            // Redirect to the desired page after successful PUT request
            // For example, redirect to a new page that uses the box data
            const queryParams = new URLSearchParams({ boxId }).toString();
            const redirectUrl = `http://127.0.0.1:5500/VA%20PHOTO%20GALLERY/index.html?${queryParams}`;
            window.location.href = redirectUrl;
        }
    })
    .catch(error => {
        console.error('Error during PUT request:', error);
    });
}

// Main function to setup the page
const main = () => {
    console.log('DOMContentLoaded event fired');

    const urlParams = new URLSearchParams(window.location.search);
    const boxID = urlParams.get('boxId');

    if (boxID) {
        console.log('boxID found:', boxID);
        loadImages();  // This should only log once unless the page is reloaded
    } else {
        console.error('No boxID provided in URL.');
        // You can handle the case where no boxID is provided here
    }

    loadBoxes();
};

// Set up event listeners when the document is fully loaded
document.addEventListener('DOMContentLoaded', main);
