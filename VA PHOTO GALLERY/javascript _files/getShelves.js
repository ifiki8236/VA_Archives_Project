const shelf_select = document.getElementById('shelf_select')
const box_num = document.getElementById('box-number')
document.addEventListener('DOMContentLoaded', function() {
    // Select the input element
    fetchShelves();


    function fetchShelves() {
        // Get the current value of the input

        // Make the fetch request to the server
        fetch('http://127.0.0.1:5000/retrieve_shelves', {
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
            setOptions(data)
            
            
        })
        .catch(error => {
            // Handle any errors
            console.error('Fetch error:', error);
        });
    }
    
    function setOptions(names) {
        names.forEach(dataValue => {
            // Create a new option element
            const option = document.createElement('option')
            // Set the value and text of the option
            option.value = dataValue[0];
            // console.log(dataValue[0])
            option.textContent = dataValue[1];  // You can modify this if you need a different display text

            // Append the option to the select element
            shelf_select.appendChild(option);
        })
    }
    document.getElementById('make-box').addEventListener('click', () => {
        const theShelf = shelf_select.value;
        const box = box_num.value
        const newBox = 'Box ' + box
        console.log('Selected Shelf:', theShelf);
        console.log(newBox)
    })
});
