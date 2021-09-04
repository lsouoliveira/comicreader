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

<style lang="scss">
	@import '~vuetify/src/components/VStepper/_variables.scss';

	@media #{map-get($display-breakpoints, 'sm-and-down')} {
		.library {
			display: grid;
			grid-template-columns: repeat(auto-fill, minmax(128px, 1fr));
			gap: 16px;
		}
	}

	@media #{map-get($display-breakpoints, 'sm-and-up')} {
		.library {
			display: grid;
			grid-template-columns: repeat(auto-fill, minmax(164px, 1fr));
			gap: 16px;
		}
	}
</style>
