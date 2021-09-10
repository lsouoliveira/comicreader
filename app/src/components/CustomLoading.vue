<template>
	<div class="d-flex justify-center pa-5" v-if="show">
		<v-progress-circular
			indeterminate
			:color="color"/>
	</div>
</template>


<script>
export default {
	name: 'CustomLoading',
	props: {
		show: {
			type: Boolean,
			default: false
		},
		color: {
			type: String,
			default: "primary"
		},
		center: {
			type: Boolean
		}
	}
}
</script>
