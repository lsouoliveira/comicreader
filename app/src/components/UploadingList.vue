<template>
	<div class="uploading-list pa-4">
		<uploading-item 
      v-for="item in uploadedFiles"
      :key="item.id"
      :filename="item.name"
      :uploaded-size="item.uploaded_size"
      :file-size="item.size"
      :status="item.status"
    />
	</div>
</template>

<script lang="ts">
import { Vue, Component, Watch } from 'vue-property-decorator'
import UploadingItem from "./UploadingItem.vue"
import { UploadedFile } from "../types/uploaded_file"

const UploadingListProps = Vue.extend({
  props: {
    uploadedFiles: {
      type: Array as () => Array<UploadedFile>,
      default: () => []
    }
  }
})

@Component({
  components: {
    UploadingItem
  }
})
export default class UploadingList extends UploadingListProps {
}
</script>

<style scoped>
.uploading-list {
	background-color: var(--v-background-lighten-1);
}
</style>
