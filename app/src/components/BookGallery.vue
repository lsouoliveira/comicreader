<template>
	<div class="book-gallery">
		<div class="book-gallery__item" v-for="item in data" :key="item.id">
      <book-card 
        :title="item.title"
        :thumbnailUrl="item.thumbnailUrl"
        :readerUrl="item.reader_url"
      />
		</div>
	</div>
</template>

<script>
import BookCard from './BookCard.vue'

export default {
	name: "BookGallery",
	components: {
		BookCard
	},
  props: {
    data: {
      default: () => [] 
    }
  }
}
</script>

<style scoped>
.book-gallery {
	display: grid;
	grid-template-columns: repeat(auto-fit, minmax(9.14rem, auto));
	grid-gap: 1.14rem;
  justify-content: flex-start;
}

.book-gallery__item {
	max-width: 9.14rem;
}
</style>
