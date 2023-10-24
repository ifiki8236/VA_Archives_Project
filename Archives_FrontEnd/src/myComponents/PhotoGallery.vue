<template>
    <div class="photo-gallery">
      <div class="gallery-item">
        <h2>Image ID: {{ id }}</h2>
        <img :src="'data:image/jpeg;base64,' + photo_data" alt="Image" class="gallery-image"/>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      photo_data: String,
      id: Number
    },
    setup(props) {
      console.log(props.photo_data);
      return {};
    }
  }
  </script>
  
  
  <style scoped>
    .photo-gallery {
      display: grid;
      grid-template-columns: repeat(1, 1fr);
      gap: 10px;
    }
    
    .gallery-item {
      border: red 2px solid;
      padding: 10px;
      margin: auto;
      margin-top: 15px;
      width: 100%;
      height: fit-content;
      text-align: center;
    }
    
    .gallery-image {
      width: 100%;
      height: 200px;
      border: solid 3px rgb(74, 74, 145);
    }
  </style>
  