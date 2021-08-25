<template>
		<v-layout class="row wrap">
			<v-flex v-for="n in 9" :key="n" xs4 sm3 md2 lg2 xl1>
				<library-item />
			</v-flex>
		</v-layout>
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
