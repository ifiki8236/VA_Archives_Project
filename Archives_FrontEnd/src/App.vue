<template>
  <div>
    <header>
      <Main_Header/>
    </header>

    <main>
      <PhotoGallery 
        v-for="item in dataArray"
        :photo_data="item.photo_data"
        :id="item.id"
        :key="item.id"
        />

    </main>
  </div>
</template>

<script setup>
import Main_Header from "./myComponents/Main_Header.vue";
import { ref } from "vue";
import PhotoGallery from "./myComponents/PhotoGallery.vue";

const dataArray = ref([]);

fetch('http://127.0.0.1:5000/')
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return response.json();
  })
  .then(data => {
    // console.log(data); // Log the fetched data
    dataArray.value = data.map(item => item[0]);    console.log('dataArray after assignment:', dataArray.value);

  })
  .catch(error => {
    console.error('Fetch error:', error);
  });
</script>
<style scoped>
  #app {
    padding: 5px;
  }
</style>
