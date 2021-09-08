<template>
	<div class="page" :class="pageClassObject">
		<img
			class="page__image"
			:src="src"
			@load="onImgLoad"
			:style="styleObject"
			/>
	</div>
</template>

<script>
	export default {
			name: 'ComicPage',
			props: {
					src: {
							type: String,
							default: ""
					},
					displayMode: {
						type: String,
						default: "fit-height"
					},
					zoomScale: {
						type: Number,
						default: 1
					},
					index: {
						type: Number,
						default: 1
					}
			},
			data() {
				return {
					width: 0,
					height: 0,
					isLoaded: false
				}
			},
			methods: {
				onImgLoad(e) {
					const target = e.target;

					this.width = target.width;
					this.height = target.height;

					this.isLoaded = true;

					this.$emit('load', this.index);
				}
			},
			computed: {
				pageClassObject() {
					return {
						'page--fit-height': this.displayMode === 'fit-height',
						'page--fit-width': this.displayMode === 'fit-width'
					}
				},
				styleObject() {
					if(!this.isLoaded) return;

					if(this.displayMode !== 'zoom') {
						return {
						}
					}

					return {
						width: `${this.width * this.zoomScale}px`,
						height: `${this.height * this.zoomScale}px`
					}
				}
			}
		};
</script>

<style scoped>
	.page__image {
		display: block;
		margin: 0 auto;
		cursor: grab;
		-webkit-user-drag: none;
		-khtml-user-drag: none;
		-moz-user-drag: none;
		-o-user-drag: none;
		user-drag: none;
	}

	.page__image:active {
		cursor: grabbing;
	}

	.page__image + .page__image {
		margin-bottom: 8px;
	}

	.page.page--fit-height .page__image {
		height: 100vh;
	}

	.page.page--fit-width .page__image {
		width: 100%;
	}
</style>

