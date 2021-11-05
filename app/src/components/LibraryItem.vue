<template>
	<div class="library-item d-flex flex-column" @click="handleClick">
			<div class="thumbnail" :class="classObject">
				<router-link to="comics/1/pages/1">
					<img src="onepiece_vol1_cover.jpg" class="thumbnail__image elevation-2"/>
				</router-link>
			</div>
			<div class="library-item__title">
				<span>One Piece - vol 1</span>
			</div>
	</div>
</template>

<script>
	export default {
		name: 'LibraryItem',
		props: {
			isAvailable: {
				type: Boolean,
				default: false
			},
			read: {
				type: Boolean,
				default: false
			}
		},
		methods: {
			handleClick() {
				this.$emit('click');
			}
		},
		computed: {
			classObject() {
				return {
					'thumbnail--processing': !this.isAvailable
				}
			}
		}
	};
</script>

<style scoped>
	.library-item {
		position: relative;
	}

	.library-item__title {
		text-align: center;
	}

	.library-item__title span {
		text-align: center;
	}

	.thumbnail {
		display: flex;
		justify-content: center;
		position: relative;
	}

	.thumbnail--processing.thumbnail:after {
		content: '';
		position: absolute;
		top: 0;
		height: 0;
		width: 100%;
		height: 100%;
		background-color: #e0e0e0;
		opacity: 0.6;
	}

	.thumbnail__image {
		position: relative;
		max-width: 100%;
	}

</style>
