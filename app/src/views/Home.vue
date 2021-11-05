<template>
	<default-layout>
		<template v-slot:header>
			<logo />
			<v-spacer />
			<v-btn 
				icon
			>
				<v-icon>mdi-plus</v-icon>
			</v-btn>
		</template>
		<template v-slot:main>
			<v-container>
				<div class="search-container my-12">
					<v-row no-gutters justify="center">
						<v-col md="5">
							<v-text-field solo flat placeholder="Type a comic name" append-icon="mdi-magnify" />	
						</v-col>
					</v-row>
				</div>
				<library/>
			</v-container>
		</template>
	</default-layout>
</template>

<script>
import DefaultLayout from './../layout/DefaultLayout.vue'
import Logo from './../components/Logo.vue'

export default {
	name: 'Home',
	components: {
		DefaultLayout,
		Logo
	},
	computed:{
		theme(){
			return (this.$vuetify.theme.dark) ? 'dark' : 'light'
		}
	}
}
</script>

<style lang="scss" scoped>
</style>
