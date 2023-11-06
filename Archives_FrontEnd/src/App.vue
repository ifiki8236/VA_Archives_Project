<template>
  <div>
    <header>
      <Main_Header/>
    </header>

    <main class="photo-gallery">
      <ImageItem 
        v-for="item in loadedImages"
        :photo_data="item.photo_data"
        :id="item.id"
        :key="item.id"
      />
      <!-- <PhotoGallery/> -->
    </main>
  </div>
</template>

<script setup>
import Main_Header from "./myComponents/Main_Header.vue";
import { ref } from "vue";
// import PhotoGallery from "./myComponents/PhotoGallery.vue";
import ImageItem from "./myComponents/ImageItem.vue";

const loadedImages = ref([]);  // to store loaded images

fetch('http://127.0.0.1:5000/')
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return response.json();
  })
  .then(data => {
    const images = data.slice(0, -1).map(item => item[0]);
    images.forEach(image => {
      loadedImages.value.push(image);  // push each image to the reactive list
      console.log('Image ', image, 'has been loaded')
    });
  })
  .catch(error => {
    console.error('Fetch error:', error);
  });
</script>


<style scoped>
    .photo-gallery {
        display: grid;
        grid-template-columns: repeat(1, 1fr);
        gap: 10px;
    }
    
    @media screen and (min-width: 600px) {
        .photo-gallery {
            grid-template-columns: repeat(2,1fr);
        }
    }
    @media screen and (min-width: 1000px) {
        .photo-gallery {
            grid-template-columns: repeat(3,1fr);
        }
    }
</style>
