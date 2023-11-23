const addBox = document.getElementById('add-a-box')
const uploadImg = document.getElementById('upload-imgs')
const back = document.getElementById('back-bttn')
const bgPage = document.querySelector('.bg-page')
const uploadImgPage = document.getElementById('uploadImgPage')
const boxCreationPage = document.getElementById('boxCreationPage')
// const select_create_box = document.getElementById('box-select')
// const select_upload_images = document.getElementById('shelf_select')


function switchPage() {
    back.style.visibility = 'visible'
    addBox.style.display = 'none'
    uploadImg.style.display = 'none'
}

function goBack() {
    back.style.visibility = 'hidden'
    boxCreationPage.style.display = 'none'
    uploadImgPage.style.display = 'none'
    addBox.style.display = 'flex'
    uploadImg.style.display = 'flex'
}

function createAddBoxForm() {
    boxCreationPage.style.display = 'flex'
}

function createUploadImagesForm() {
    uploadImgPage.style.display = 'block'
}

addBox.addEventListener('click', function() {
    switchPage()
    createAddBoxForm()
})

uploadImg.addEventListener('click', function() {
    switchPage()
    createUploadImagesForm()
})

back.addEventListener('click', goBack)

const buttons = document.getElementsByTagName('button');
for (let i = 0; i < buttons.length; i++) {
    buttons[i].addEventListener('click', function() {
        // console.log(`Button ${buttons[i]} clicked`);
        buttons[i].style.backgroundColor = 'lightgray'
        setTimeout(() => {
            this.style.backgroundColor = ''; // Resets to original or you can set a specific color
        }, 125);
    });
}

