<template>
	<div class="text-center">
		<v-dialog
			v-model="isDialogOpen"
			width="640"
		>
			<v-card>
				<v-card-title>
					Upload files
				</v-card-title>

				<v-divider />
				<div class="pt-4">
					<div class="px-4">
						<drag-and-drop-area @change="handleFileDropped"/>
					</div>
					<uploading-list :uploaded-files="uploadedFiles"/>
				</div>
			</v-card>
		</v-dialog>
	</div>
</template>

<script lang="ts">
import { Vue, Component, Watch } from 'vue-property-decorator'
import DragAndDropArea from "./DragAndDropArea.vue"
import UploadingList from "./UploadingList.vue"
import { UploadedFile } from "../types/uploaded_file"

const FileUploadDialogProps = Vue.extend({
  props: {
    show: {
      type: Boolean,
      default: false
    },
    uploadedFiles: {
      type: Array as () => Array<UploadedFile>,
      default: () => []
    }
  }
})

@Component({
  components: {
		DragAndDropArea,
		UploadingList
  }
})
export default class FileUploadDialog extends FileUploadDialogProps {
  isDialogOpen = false 

  handleCloseDialog(): void {
    this.$emit("close")
  }

  handleFileDropped(e: Event): void {
    this.$emit('fileDropped', e)
  }

  @Watch("show")
  watchShow(newValue: boolean): void {
    this.isDialogOpen = newValue
  }

  @Watch("isDialogOpen")
  watchIsDialogOpen(newValue: boolean): void {
    if(!newValue) {
      this.$emit("close")
    }
  }
}
</script>
