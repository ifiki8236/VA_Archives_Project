const bttn = document.getElementById('make-box')

bttn.addEventListener('click', function() {
    // Get the current value of the input
    const boxNum = document.getElementById('box-number').value
    const shelfData = document.getElementById('shelf_select').value
    // Prepare the data to be sent in the request
    if (boxNum != '' && shelfData != '') {
        const data = {
            boxNum: boxNum,
            shelfData: shelfData,
        }
    
        // Make the fetch request to the server
        fetch('http://127.0.0.1:5000/store_box_data', {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data)
        })
        .then(response => {
            // Check if the response is successful
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            console.log('Success:', data);
            alert(`Archival Box ${boxNum} created!`)
            clearInput()
        })
        .catch(error => {
            console.error('Fetch error:', error);
        });
    }
    else {
        alert('Null values detected!')
        // bttn.classList.add('error');
    }
    
})

function clearInput() {
    const boxInput = document.getElementById('box-number')
    const shelfInput = document.getElementById('shelf_select')

    boxInput.value = ''
    shelfInput.value = ''
}