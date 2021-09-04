<template>
	<v-app>
		<v-app-bar app dark color="primary" >
			<v-toolbar-title class="title">Vol 1 - Romance Dawn</v-toolbar-title>
			<template v-slot:extension>
				<div class="options">
						<page-counter />
						<zoom-control />
				</div>
			</template>
		</v-app-bar>
		<v-main>
		</v-main>
	</v-app>
</template>

<script>
	import PageCounter from './../components/PageCounter.vue'
	import ZoomControl from './../components/ZoomControl.vue'
	// import Loading from './../components/Loading.vue'

	export default {

			name: 'ReadComic',
			components: {
					PageCounter,
					ZoomControl,
					// Loading
				}
		}
</script>

<style>
	.options {
		position: absolute;
		top: 0;
		left: 0;
		width: 100%;
		height: 100%;
		display: flex;
		align-items: center;
		justify-content: center;
		pointer-events: none;
	}

	.options * {
		pointer-events: auto;
	}
</style>
