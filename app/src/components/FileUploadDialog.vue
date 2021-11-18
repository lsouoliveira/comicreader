<template>
	<div class="text-center">
		<v-dialog
			:value="dialog"
			@click:outside="handleCloseDialog"
			width="640"
		>
			<v-card>
				<v-card-title>
					Upload files
				</v-card-title>

				<v-divider />
				<div class="py-4 px-6">
					<drag-and-drop-area />
				</div>
			</v-card>
		</v-dialog>
	</div>
</template>

<script>
import DragAndDropArea from "./DragAndDropArea.vue"

export default {
	name: "FileUploadDialog",
	components: {
		DragAndDropArea
	},
	props: {
		dialog: {
			default: false
		}
	},
	methods: {
		handleCloseDialog() {
			this.$emit("close")
		}
	}
}
</script>
