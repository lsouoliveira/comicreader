<template>
	<div class="d-flex flex-column" v-ripple>
		<img src="onepiece_vol1_cover.jpg" class="elevation-2 thumbnail">
		<div class="subtitle-2 text-center pa-2 text-truncate">Vol 1 - One piece</div>
	</div>
</template>

<script>
	export default {
		name: 'LibraryItem'
	};
</script>

<style scoped>
	.thumbnail {
		position: relative;
		border: 10px solid black !important;
	}

	.thumbnail::after {
		position: absolute;	
		top: 0px;
		left: 0px;
		width: 100%;
		height: 100%;
		background-color: red; 
	}
</style>
