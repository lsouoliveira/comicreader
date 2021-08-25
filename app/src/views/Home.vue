<template>
	<v-app>
		<v-app-bar app dark color="primary">
			<v-toolbar-title class="title">Comic Reader</v-toolbar-title>
		</v-app-bar>
		<v-main>
			<v-container grid-list-lg>
				<library/>
			</v-container>
		</v-main>
	</v-app>
</template>

<script>
	import Library from './../components/Library.vue'

	export default {

		name: 'Home',
		components: {
			Library
		}
	}
</script>
