const button = document.getElementById('put-images')

button.addEventListener('click', function() {
    const boxData = document.getElementById('box-select').value;
    const imageData = document.getElementById('img-upload').files;
    const imagePromises = [];

    // Convert each image file to Base64
    for (let i = 0; i < imageData.length; i++) {
        const reader = new FileReader();
        const imagePromise = new Promise((resolve, reject) => {
            reader.onload = function(event) {
                resolve(event.target.result);
            };
            reader.onerror = reject;
            reader.readAsDataURL(imageData[i]);
        });
        imagePromises.push(imagePromise);
    }

    // Once all images are converted
    Promise.all(imagePromises).then(base64Images => {
        console.log(imagePromises.length)
        const data = {
            boxData: boxData,
            imageData: base64Images
        };

        // Make the fetch request to the server
        fetch('http://127.0.0.1:5000/add_images', {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data)
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            console.log('Success:', data)
            alert('Images added')
            clearInput();
        })
        .catch(error => {
            console.error('Fetch error:', error);
        });
    });
});

function clearInput() {
    const boxInput = document.getElementById('box-number')
    const shelfInput = document.getElementById('shelf_select')

    boxInput.value = ''
    shelfInput.value = ''
}

// function extractImageData(imageData) {
//     const files = imageData;
//     let imageArray = []
//     console.log('Uploaded files:');
//     for (let i = 0; i < files.length; i++) {
//         console.log(files[i]);
//         imageArray.push(files[i])
//     }
//     return imageArray
// }