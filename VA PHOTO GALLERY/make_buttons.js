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
                //   loadImages(box[0])
              };
              buttonsContainer.appendChild(button);
          });
      })
      .catch(error => {
          console.error('Error fetching boxes:', error);
      });
}

// function redirectPage(boxId) {
//     // Data to be sent in the PUT request
//     let dataToSend = boxId
  
//     // Make a PUT request to the Flask server
//     fetch('http://127.0.0.1:5000/store_box_data', {
//       method: 'PUT',
//       headers: {
//         'Content-Type': 'application/json'
//       },
//       body: JSON.stringify(dataToSend),
//       // credentials: 'include'
//     })
//     .then(response => {
//         if (!response.ok) {
//             throw new Error('Network response was not ok');
//         }
//         return response.json();
//     })
//     .then(data => {
//         if (data.success) {
//         // Redirect to the desired page after successful PUT request
//         // For example, redirect to a new page that uses the box data
//         const queryParams = new URLSearchParams({ boxId }).toString()
//         const redirectUrl = `http://127.0.0.1:5500/VA%20PHOTO%20GALLERY/index.html?${queryParams}`
//         window.location.href = redirectUrl
//         //   window.location.href = `http://127.0.0.1:5500/VA%20PHOTO%20GALLERY/index.html`;
//         }
//     })
//     .catch(error => {
//         console.error('Error during PUT request:', error);
//     });
//   }
  
function redirectPage(boxId) {
  if (true) {
    // Redirect to the desired page after successful PUT request
    // For example, redirect to a new page that uses the box data
    const queryParams = new URLSearchParams({ boxId }).toString()
    const redirectUrl = `http://127.0.0.1:5500/VA%20PHOTO%20GALLERY/index.html?${queryParams}`
    window.location.href = redirectUrl
    //   window.location.href = `http://127.0.0.1:5500/VA%20PHOTO%20GALLERY/index.html`;
    }
}

document.addEventListener('DOMContentLoaded', () => {
  loadBoxes();
});
