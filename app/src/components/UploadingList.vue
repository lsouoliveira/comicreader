<template>
	<div class="uploading-list pa-4">
		<uploading-item filename="one piece - vol 1.cbz" progress="0.5" v-for="item in Array(5)" :key="item" />
	</div>
</template>

<script>
import UploadingItem from "./UploadingItem.vue"

export default {
	name: "UploadingList",
	components: {
		UploadingItem
	}
}
</script>

<style scoped>
.uploading-list {
	background-color: var(--v-background-lighten-1);
}
</style>
