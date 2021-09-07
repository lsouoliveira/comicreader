<template>
	<div class="d-flex align-center zoom-control">
		<v-slider
			min="25"
			max="200"
			step="25"
			:value="zoomScale"
			@change="handleChange"
			thumb-label
			ticks
			></v-slider>
	</div>
</template>

<script>
	export default {
			name: 'ZoomControl',
			props: {
				zoomScale: {
					type: Number,
					default: 100
				}
			},
			methods: {
				handleChange(value) {
					this.$emit('change', value)
				}
			}
		};
</script>

<style>
.zoom-control {
	min-width: 200px;
}
</style>
