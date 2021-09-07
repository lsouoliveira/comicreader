<template>
	<div class="comic" :style="bottomMargin">
			<comic-page src="http://localhost:8080/onepiece_vol1_cover.jpg" :display-mode="displayMode" :zoom-scale="zoomScale"/>
			<comic-page src="http://localhost:8080/onepiece_vol1_cover.jpg" :display-mode="displayMode" :zoom-scale="zoomScale"/>
			<comic-page src="http://localhost:8080/onepiece_vol1_cover.jpg" :display-mode="displayMode" :zoom-scale="zoomScale"/>
			<comic-page src="http://localhost:8080/onepiece_vol1_cover.jpg" :display-mode="displayMode" :zoom-scale="zoomScale"/>
			<comic-page src="http://localhost:8080/onepiece_vol1_cover.jpg" :display-mode="displayMode" :zoom-scale="zoomScale"/>
	</div>
</template>

<script>
	import ComicPage from './../components/ComicPage.vue'
	import MouseScrollDrag from './../utils/MouseScrollDrag.js'
	import MouseEvents from './../utils/MouseEvents.js'

	export default {
			name: 'ComicReader',
			props: {
				displayMode: {
					type: String
				},
				zoomScale: {
					type: Number,
					default: 1
				},
				bottomSpacing: {
					type: Boolean,
					default: true
				}
			},
			data() {
					return {
							mouseScrollDrag: null,
							mouseEvents: null
						}
				},
			computed: {
				bottomMargin() {
					return {
						paddingBottom: (8 + (this.bottomSpacing ? 48 : 0)) + 'px' 
					}
				}
			},
			mounted() {
					const rootElement = this.$el;

					this.mouseScrollDrag = new MouseScrollDrag(rootElement);
					this.mouseEvents = new MouseEvents(rootElement);

					this.mouseEvents.onClick = () => {
						this.$emit('click');
					}

					this.mouseEvents.onDoubleClick = () => {
						this.$emit('dblclick');
					}
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
	padding-top: 8px;
	padding-left: 8px;
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
