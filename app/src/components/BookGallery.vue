<template>
  <div>
    <transition-group name="remove-item" tag="div" class="book-gallery" v-if="!loading">
      <div class="book-gallery__item" v-for="item in data" :key="item.id">
          <book-card 
            :id="item.id"
            :title="item.title"
            :thumbnailUrl="item.thumbnailUrl"
            :readerUrl="item.readerUrl"
            :read="item.read"
            :status="item.status"
            @remove="handleBookRemove"
            @mark-as-read="handleMarkAsRead"
            @book-unavailable="handleBookUnavailable"
            :key="item.id"
          />
      </div>
    </transition-group>

    <div v-if="loading">
      <div class="book-gallery">
        <div v-for="item in Array(16)" :key="item">
          <v-skeleton-loader type="image" />
          <v-skeleton-loader type="text" class="mt-2" max-width="50%"/>
        </div>
      </div>
      <div class="text-center mt-5">
        <v-progress-circular
          indeterminate
          color="primary"/>
      </div>
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
    },
    loading: {
      type: Boolean,
      default: false
    }
  },
  methods: {
    handleBookRemove(bookId) {
      this.$emit("remove", bookId)
    },
    handleMarkAsRead(bookId) {
      this.$emit("mark-as-read", bookId)
    },
    handleBookUnavailable(bookId) {
      this.$emit("book-unavailable", bookId)
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
  transition: all 0.5s;
}

.remove-item-move,
.remove-item-enter-active,
.remove-item-leave-active {
  transition: all 0.5s ease;
}

.remove-item-enter-from,
.remove-item-leave-to {
  opacity: 0;
}

.remove-item-leave-active {
  display: none;
}
</style>
