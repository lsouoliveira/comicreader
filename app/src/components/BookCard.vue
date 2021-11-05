<template>
	<v-card flat>
		<v-card-text class="pa-8">
			<div class='cover'>
				<img src='../../public/onepiece_vol1_cover.jpg'/>
			</div>
			<div class='font-weight-bold mt-5'>
				One piece - vol 1 
			</div>
		</v-card-text>
	</v-card>
</template>

<script>
export default {
	name: 'BookCard'
}
</script>

<style scoped>
.cover {
	display: flex;
	flex-direction: column;
}
</style>
