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
				<div class="pt-4">
					<div class="px-4">
						<drag-and-drop-area />
					</div>
					<uploading-list />
				</div>
			</v-card>
		</v-dialog>
	</div>
</template>

<script>
import DragAndDropArea from "./DragAndDropArea.vue"
import UploadingList from "./UploadingList.vue"

export default {
	name: "FileUploadDialog",
	components: {
		DragAndDropArea,
		UploadingList
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
