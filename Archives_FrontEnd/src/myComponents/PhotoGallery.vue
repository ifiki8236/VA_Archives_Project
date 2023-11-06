<template>
    <div class="photo-gallery">
        <ImageItem 
            v-for="image in images"
            :key="image.id"
            :photo_data="image.data"
            :id="image.id"
        />
    </div>
</template>

<script>
import ImageItem from './ImageItem.vue';

export default {
  components: {
    ImageItem
  },
  props: {
    images: {
      type: Array,
      required: true
    }
  }
}
</script>

<style scoped>
    .photo-gallery {
      display: grid;
      grid-template-columns: repeat(1, 1fr);
      gap: 10px;
    }
    
    /* .gallery-item {
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
    } */
    
    @media screen and (min-width: 900px) {
        .photo-gallery {
            grid-template-columns: repeat(2,1fr);
        }
    }
</style>
