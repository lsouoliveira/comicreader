<template>
	<div class="d-flex align-center zoom-control">
		<v-btn
			icon
		>
			-
		</v-btn>
		<div>
			<v-text-field
				hide-details
				single-line
				solo-inverted
				class="zoom-control__level"
				value="100%" />
		</div>
		<v-btn
			icon
		>
			+
		</v-btn>
	</div>
</template>

<script>
	export default {
			name: 'ZoomControl',
			props: {
			}
		};
</script>

<style>
	.zoom-control div + div {
		margin-left: 8px;
	}

	.zoom-control__level {
		flex: 0;
	}

	.zoom-control__level .v-input__control {
		min-height: 0 !important;
	}

	.zoom-control__level input {
		max-width: 42px;
		text-align: center;
	}
</style>
