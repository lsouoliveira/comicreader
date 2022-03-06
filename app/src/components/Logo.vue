<template>
	<v-toolbar-title class="logo"><router-link to="/" class="white--text">Comic Reader</router-link></v-toolbar-title>
</template>

<script lang="ts">
import Vue from 'vue'
import Component from 'vue-class-component'

@Component
export default class Logo extends Vue {
}
</script>

<style scoped>
.logo a {
	text-decoration: none;
}
</style>
