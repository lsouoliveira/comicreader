<template>
	<div class="library-item d-flex flex-column" @click="handleClick">
		<v-card>
			<div class="thumbnail" :class="classObject">
				<img src="onepiece_vol1_cover.jpg" class="thumbnail__image"/>
			</div>
			<v-card-text>
				<div class="d-flex align-center justify-space-between">
					<div class="text-truncate">Vol 1 - One piece</div>
					<v-btn icon>
						<v-icon>mdi-dots-vertical</v-icon>
					</v-btn>
				</div>
				<div>
					<v-chip color="green" text-color="white">Lido</v-chip>
				</div>
			</v-card-text>
		</v-card>
	</div>
</template>

<script>
	export default {
		name: 'LibraryItem',
		props: {
			isAvailable: {
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

<style>
	.library-item {
		position: relative;
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
