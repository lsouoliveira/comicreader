<template>
	<div class="loading d-flex justify-center align-center" style="height: 100%;" v-if="show">
		<v-progress-circular
			indeterminate
			color="primary"/>
	</div>
</template>


<script>
	export default {
		name: 'Loading',
		props: {
			show: {
				type: Boolean,
				default: false
			}
		}
	}
</script>

<style scoped>
.loading {
	position: fixed;
	top: 0;
	left: 0;
	width: 100%;
	background-color: white;
}
</style>
