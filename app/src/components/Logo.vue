<template>
	<v-toolbar-title class="logo primary--text"><a href="/">Comic Reader</a></v-toolbar-title>
</template>

<script lang="ts">
import Vue from 'vue'
import Component from 'vue-class-component'

@Component
export default class Logo extends Vue {
}
</script>

<style scoped>
.logo {
	font-weight: bold;
}

.logo a {
	text-decoration: none;
}
</style>
