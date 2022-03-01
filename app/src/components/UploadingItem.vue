<template>
	<div class="uploading-item py-2">
		<div class="uploading-item__header pb-1">
			<div class="uploading-item__filename text-truncate overflow-hidden">
				<span class="text-body-1">{{ filename }}</span>
			</div>
			<div v-if="isUploading" class="text-no-wrap">
				<span class="uploading-item__size text-body-2 alt--text">{{ progressInfo }}</span>
			</div>
			<div v-if="isSuccess">
        <v-icon right small color="success">
          mdi-checkbox-marked-circle
        </v-icon>
			</div>
			<div v-if="isError">
        <v-icon right small color="error">
          mdi-alert-circle
        </v-icon>
			</div>
		</div>
		<div class="progress-bar" v-if="isUploading">
      <div class="progress-bar__progress" :style="progressBarStyleObject">
      </div>
    </div>
	</div>
</template>

<script>
export default {
	name: "UploadingItem",
	props: {
		filename: {
			default: ""
		},
		fileSize: {
			default: 0
		},
		uploadedSize: {
			default: 0
		},
    status: {
      default: 0
    }
	},
  computed: {
    progressInfo() {
      return `${this.uploadedSize / 1000} KB / ${this.fileSize / 1000} KB`
    },
    progressBarStyleObject() {
      return {
        width: `${this.uploadedSize / this.fileSize * 100}%`
      }
    },
    isUploading() {
      return this.status == 0 
    },
    isError() {
      return this.status == 1 
    },
    isSuccess() {
      return this.status == 2 
    },
  }
}
</script>

<style scoped>
.uploading-item__header {
	display: flex;
	justify-content: space-between;
}

.uploading-item__size {
	font-weight: 500;
}

.progress-bar {
	position: relative;
	min-height: 4px;
	background-color: var(--v-background-base);
	border-radius: 2px;
}

.progress-bar__progress {
	content: "";
	position: absolute;
	top: 0;
	left: 0;
	width: 50%;
	height: 100%;
	min-height: 4px;
	background-color: var(--v-success-lighten2);
	border-radius: 2px;
}
</style>
