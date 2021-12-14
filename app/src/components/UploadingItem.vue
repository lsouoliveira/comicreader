<template>
	<div class="uploading-item py-2">
		<div class="uploading-item__header pb-1">
			<div class="uploading-item__filename">
				<span class="text-body-1">{{ filename }}</span>
			</div>
			<div>
				<span class="uploading-item__size text-body-2 alt--text">1.2 KB / 12 KB</span>
			</div>
		</div>
		<div class="uploading-item__progress-bar"></div>
	</div>
</template>

<script>
export default {
	name: "UploadingItem",
	props: {
		filename: {
			default: ""
		},
		filesize: {
			default: 0
		},
		uploadedSize: {
			default: 0
		}
	}
}
</script>

<style scoped>
.uploading-item {
}

.uploading-item__header {
	display: flex;
	justify-content: space-between;
}

.uploading-item__filename span {
}

.uploading-item__size {
	font-weight: 500;
}

.uploading-item__progress-bar {
	position: relative;
	min-height: 4px;
	background-color: var(--v-background-base);
	border-radius: 2px;
}

.uploading-item__progress-bar:after {
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
