<template>
	<div class="comic" :style="bottomMargin">
			<comic-page
				:src="page.url"
				:display-mode="displayMode"
				:zoom-scale="zoomScale"
				v-for="page in pages"
				:index="page.index"
				:key="page.index"
				@load="handleImageLoaded"
				:show="page.isVisible"
			/>
	</div>
</template>

<script>
	import ComicPage from './../components/ComicPage.vue'
	import MouseScrollDrag from './../utils/MouseScrollDrag.js'
	import MouseEvents from './../utils/MouseEvents.js'

	export default {
			name: 'ComicReader',
			props: {
				pages: [],
				page: {
					type: Number,
					default: 0
				},
				numPages: {
					type: Number,
					default: 0
				},
				remainImagesTrigger: {
					type: Number,
					default: 0
				},
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
			methods: {
				handleImageLoaded(pageIndex) {
					this.$emit('page-load', pageIndex);
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
