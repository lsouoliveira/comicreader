<template>
	<v-app-bar app dark color="primary">
		<v-toolbar-title class="title">Comic Reader</v-toolbar-title>
		<slot />
	</v-app-bar>
</template>

<script>
	export default {
			name: 'CustomHeader',
			components: {
			}
		};
</script>
