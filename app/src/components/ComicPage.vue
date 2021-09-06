<template>
	<div class="page">
		<img
			class="page__image"
			:src="src"
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
</style>

