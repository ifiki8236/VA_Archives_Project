<template>
    <div class="gallery-item" ref="imageItemRef">
        <div>
            <h2>Image ID: {{ id }}</h2>
        </div>
        <div v-if="!imageLoaded">Loading...</div>
        <img v-else-if="imageLoaded" :src="'data:image/jpeg;base64,' + photo_data" @error="onImageError" alt="Image" class="gallery-image"/>
    </div>
</template>

<script>
export default {
    props: {
        photo_data: String,
        id: String
    },
    data() {
        return {
            imageLoaded: false
        };
    },
    methods: {
        loadImage() {
            this.imageLoaded = true;
        },
        onImageError() {
            console.error('Failed to load image with ID:', this.id);
        }
    },
    mounted() {
        const observer = new IntersectionObserver(entries => {
            if (entries[0].isIntersecting) {
                this.loadImage();
                observer.disconnect();
            }
        });
        observer.observe(this.$refs.imageItemRef);
    },
    beforeUnmount() {
        observer && observer.disconnect();
    }
};
</script>

<style scoped>
.gallery-item {
    border: red 2px solid;
    padding: 10px;
    margin: auto;
    margin-top: 10px;
    margin-bottom: 10px;
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