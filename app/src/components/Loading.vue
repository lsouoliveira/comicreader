<template>
	<div class="d-flex justify-center align-center" style="height: 100%;" v-if="show">
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
