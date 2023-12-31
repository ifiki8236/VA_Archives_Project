const box_select = document.getElementById('box-select')
const put_images = document.getElementById('put-images')
const fileInput = document.getElementById('img-upload')

document.addEventListener('DOMContentLoaded', function() {
    // Select the input element
    fetchBoxes();


    function fetchBoxes() {
        // Get the current value of the input

        // Make the fetch request to the server
        fetch('http://127.0.0.1:5000/retrieve_boxes', {
            method: 'GET'
        })
        .then(response => {
            // Check if the response is successful
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            // Process the data
            setBoxes(data)
            // console.log(data)
            
        })
        .catch(error => {
            // Handle any errors
            console.error('Fetch error:', error);
        });
    }
});

function setBoxes(boxes) {
    // console.log(boxes)
    boxes.forEach(dataValue => {
        // Create a new option element
        const option = document.createElement('option')
        // Set the value and text of the option
        option.value = dataValue[0];
        // console.log(dataValue[1])
        option.textContent = dataValue[1];  // You can modify this if you need a different display text

        // Append the option to the select element
        box_select.appendChild(option);
    })
}
// document.getElementById('put-images').addEventListener('click', () => {
//     const theBox = box_select.value;
//     console.log('Selected Box:', theBox);

//     // const files = fileInput.files;
//     //     console.log('Uploaded files:');
//     //     for (let i = 0; i < files.length; i++) {
//     //         console.log(files[i]);
//     // }
// })