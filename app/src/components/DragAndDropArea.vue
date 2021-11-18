<template>
	<div class="drag-and-drop-area">
		<div class="text-center">
			<v-icon class="upload-icon">mdi-cloud-upload</v-icon>
		</div>
		<div class="text-center text-h6">
			<span>Drag and drop, or <span class="font-weight-bold">browse</span> your files</span>
		</div>
	</div>
</template>

<script>
export default {
	name: "DragAndDropArea"
}
</script>

<style scoped>
.drag-and-drop-area {
	border: 0.125rem dashed var(--v-alt-base);
	padding: 5rem 0;
	cursor: pointer;
}

.upload-icon {
	font-size: 4rem;
}
</style>
