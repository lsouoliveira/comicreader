<template>
	<v-app-bar app dark color="primary">
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
