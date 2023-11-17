const addBox = document.getElementById('add-a-box')
const uploadImg = document.getElementById('upload-imgs')
const back = document.getElementById('back-bttn')
const bgPage = document.querySelector('.bg-page')
const uploadImgPage = document.getElementById('uploadImgPage')
const boxCreationPage = document.getElementById('boxCreationPage')
const put_images_bttn = document.getElementById('put-images')
const make_box_bttn = document.getElementById('make-box')
const select = document.getElementById('box-select')
const fileInput = document.getElementById('img-upload')


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
make_box_bttn.addEventListener('click', () => {
    
})
put_images_bttn.addEventListener('click', () => {
    const selectedBox = select.value;
    console.log('Selected Box:', selectedBox);

    const files = fileInput.files;
        console.log('Uploaded files:');
        for (let i = 0; i < files.length; i++) {
            console.log(files[i].name);
    }
})