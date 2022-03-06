<template>
	<div class="drag-and-drop-area">
		<label>
			<div>
				<div class="text-center">
					<v-icon class="upload-icon alt--text">mdi-cloud-upload</v-icon>
				</div>
				<div class="text-h6">
					<span>Drag and drop, or <span class="font-weight-bold">browse</span> your files</span>
				</div>
			</div>
			<input type="file" hidden multiple @change="handleFileBrowserChange" accept=".cbz"/>
		</label>
	</div>
</template>

<script>
export default {
	name: "DragAndDropArea",
	methods: {
		handleFileBrowserChange(e) {
			this.$emit("change", e)
		}
	}
}
</script>

<style scoped>
.drag-and-drop-area {
	background-color: var(--v-background-base);
}

.drag-and-drop-area label {
	padding: 4rem 0;
	display: flex;
	align-items: center;
	justify-content: center;
	cursor: pointer;
	flex: 1;
}

.upload-icon {
	font-size: 4rem;
}
</style>
