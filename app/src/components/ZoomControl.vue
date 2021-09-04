<template>
	<div class="d-flex align-center zoom-control">
		<v-slider
			min="25"
			max="200"
			step="25"
			thumb-label
			ticks
			></v-slider>
	</div>
</template>

<script>
	export default {
			name: 'ZoomControl',
			props: {
				}
		};
</script>

<style>
.zoom-control {
	min-width: 200px;
}
</style>
