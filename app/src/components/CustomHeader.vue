<template>
	<v-app-bar app dense elevation="1" color="surface">
		<slot />
	</v-app-bar>
</template>

<script>
import Vue from 'vue'
import Component from 'vue-class-component'

@Component
export default class CustomHeader extends Vue {
}
</script>
