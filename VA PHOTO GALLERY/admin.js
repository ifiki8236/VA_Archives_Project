const addBox = document.getElementById('add-a-box');
const uploadImg = document.getElementById('upload-imgs');
const back = document.getElementById('back-bttn');
const bgPage = document.querySelector('.bg-page');

function switchPage() {
    // Clear existing content
    while (bgPage.firstChild) {
        bgPage.removeChild(bgPage.firstChild);
    }
    back.style.visibility = 'visible';
}

function goBack() {
    // Clear existing content
    while (bgPage.firstChild) {
        bgPage.removeChild(bgPage.firstChild);
    }
    back.style.visibility = 'hidden';
    // Recreate and append the initial buttons
    bgPage.appendChild(addBox);
    bgPage.appendChild(uploadImg);
}

function createAddBoxForm() {
    const h2 = document.createElement('h2');
    h2.textContent = 'Create a Box';
    const boxFormDiv = document.createElement('div');
    boxFormDiv.classList.add('form-class');
    boxFormDiv.appendChild(h2);
    // Add form elements here (input, label, button, etc.)
    bgPage.appendChild(boxFormDiv);
}

function createUploadImagesForm() {
    const h2 = document.createElement('h2');
    h2.textContent = 'Upload Images';
    const uploadFormDiv = document.createElement('div');
    uploadFormDiv.classList.add('form-class');
    uploadFormDiv.appendChild(h2);
    // Add form elements here (input, label, button, etc.)
    bgPage.appendChild(uploadFormDiv);
}

addBox.addEventListener('click', function() {
    switchPage();
    createAddBoxForm();
});

uploadImg.addEventListener('click', function() {
    switchPage();
    createUploadImagesForm();
});

back.addEventListener('click', goBack);
