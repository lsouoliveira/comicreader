<template>
	<div class="comic">
		<div>
			<comic-page src="http://localhost:8080/onepiece_vol1_cover.jpg" />
			<comic-page src="http://localhost:8080/onepiece_vol1_cover.jpg" />
			<comic-page src="http://localhost:8080/onepiece_vol1_cover.jpg" />
			<comic-page src="http://localhost:8080/onepiece_vol1_cover.jpg" />
			<comic-page src="http://localhost:8080/onepiece_vol1_cover.jpg" />
		</div>
	</div>
</template>

<script>
	import ComicPage from './../components/ComicPage.vue'

	export default {
			name: 'ComicReader',
			props: {
				},
			data() {
					return {
							isDragging: false,
							lastMousePosition: {
									x: 0,
									y: 0
							}
						}
				},
			mounted() {
					const rootElement = this.$el;

					rootElement.addEventListener("mousedown", (e) => {
							this.isDragging = true;

							this.lastMousePosition = {
									x: e.clientX,
									y: e.clientY
								};
						}, false);

					rootElement.addEventListener("mousemove", (e) => {
							if(this.isDragging) {
									const currentMousePosition = {
											x: e.clientX,
											y: e.clientY
									};
									window.scrollBy(
										this.lastMousePosition.x - currentMousePosition.x,
										this.lastMousePosition.y - currentMousePosition.y 
									);

									this.lastMousePosition = currentMousePosition;
							}
						}, false);

					rootElement.addEventListener("mouseup", () => {
							this.isDragging = false;
					}, false);

					rootElement.addEventListener("mouseleave", () => {
							this.isDragging = false;
					}, false);
				},

			components: {
					ComicPage
				}
		};
</script>

<style scoped>

.comic {
	position: relative;
	min-height: 100vh;
	background-color: #212121;
	padding: 8px 0 56px 0;
}

.comic {
	width: 100%;
	position: absolute;
	top: 0;
	overflow: auto;
	-webkit-touch-callout: none;
	-webkit-user-select: none;
	-khtml-user-select: none;
	-moz-user-select: none;
	-ms-user-select: none;
	user-select: none;
	text-align: center;
}

.comic:active {
	cursor: grabbing;
}

.comic .page + .page {
	margin-top: 8px;
}

</style>
