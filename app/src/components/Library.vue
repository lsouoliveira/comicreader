<template>
	<div class="library">
		<div v-for="n in 12" :key="n">
			<library-item :isAvailable="true" @click="() => handleLibraryItemClick(n)" />
		</div>
	</div>
</template>

<script>
	import LibraryItem from './LibraryItem.vue';

	export default {
		name: 'Library',
		components: {
			LibraryItem
		}
	};
</script>

<style>
	.library {
		display: grid;
		grid-template-columns: repeat(auto-fill, minmax(158px, 1fr));
		gap: 16px;
	}
</style>
