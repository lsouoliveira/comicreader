<template>
	<v-app>
		<v-app-bar app dark color="primary" >
			<v-toolbar-title class="title">Vol 1 - Romance Dawn</v-toolbar-title>
			<v-spacer/>
				<v-menu offset-y>
					<template v-slot:activator="{ on, attrs }">
						<v-btn 
										icon
										v-bind="attrs"
										v-on="on"
										>
										<v-icon>mdi-cog</v-icon>
						</v-btn>
					</template>
					<v-list>
						<v-list-item link>
							Adjust to height
						</v-list-item>
						<v-list-item link>
							Adjust to width
						</v-list-item>
						<v-list-item>
							<div class="config__item">
								<span>Zoom</span>
								<zoom-control/>
							</div>
						</v-list-item>
					</v-list>
				</v-menu>
		</v-app-bar>
		<v-main>
			<v-toolbar
				absolute
				color="primary"
				dark
				bottom
				dense
				width="100%"
				>
				<div class="options">
					<page-counter />
				</div>
			</v-toolbar>
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
					ZoomControl
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
