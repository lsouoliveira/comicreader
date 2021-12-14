<template>
	<div class="book-gallery">
		<div class="book-gallery__item" v-for="item in Array(20)" :key="item">
			<book-card />
		</div>
	</div>
</template>

<script>
import BookCard from './BookCard.vue'

export default {
	name: "BookGallery",
	components: {
		BookCard
	}
}
</script>

<style scoped>
.book-gallery {
	display: grid;
	grid-template-columns: repeat(auto-fit, minmax(9.14rem, auto));
	grid-gap: 1.14rem;
}

.book-gallery__item {
	max-width: 9.14rem;
}
</style>
