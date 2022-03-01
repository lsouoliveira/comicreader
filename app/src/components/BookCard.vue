<template>
	<div class="book-card">
    <a :href="readerUrl">
      <div class='cover'>
        <img :src='thumbnailUrl'/>
      </div>
    </a>
		<div class="mt-1 book-card__info-header">
				<a class="font-weight-bold text-body-1 primary--text book-card__title me-1">{{title}}</a>
			<div>
				<v-btn small icon class="primary--text">
					<v-icon style="font-size: 1.42rem;">mdi-dots-vertical</v-icon>
				</v-btn>
			</div>
		</div>
		<div class="mt-1">
			<v-chip color="green" small v-if="read">read</v-chip>
		</div>
	</div>
</template>

<script>
export default {
	name: 'BookCard',
	props: {
		read: {
			type: Boolean,
			default: false
		},
    title: {
      type: String,
      default: ""
    },
    thumbnailUrl: {
      type: String,
      default: ""
    },
    readerUrl: {
      type: String,
      default: ""
    }
	}
}
</script>

<style scoped>
.book-card {
	background: none;
}

.book-card__title {
	white-space: nowrap;
	text-overflow: ellipsis;
	overflow: hidden;
}

.book-card__info-header {
	display: flex;
	justify-content: space-between;
	align-items: center;
}

.cover {
	display: flex;
	flex-direction: column;
}

.cover:hover {
	cursor: pointer;
}
</style>
