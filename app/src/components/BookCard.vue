<template>
	<v-card flat>
		<v-card-text class="pa-6">
			<div class='cover'>
				<img src='../../public/onepiece_vol1_cover.jpg' class="cover__img rounded-lg"/>
			</div>
			<div class='mt-4'>
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
