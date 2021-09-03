<template>
	<v-app>
		<custom-header>
			<v-flex pl-4>
				<v-text-field
					hide-details
					single-line
					placeholder="Search for comics"/>
			</v-flex>
			<v-spacer/>
				<v-btn 
					icon
					href="comics/add"
				>
					<v-icon>mdi-plus</v-icon>
				</v-btn>
		</custom-header>
		<v-main>
			<v-container>
				<library/>
			</v-container>
			<Loading />
		</v-main>
	</v-app>
</template>

<script>
	import CustomHeader from '../components/CustomHeader.vue'
	import Library from './../components/Library.vue'
	import Loading from './../components/Loading.vue'

	export default {

			name: 'Home',
			components: {
					CustomHeader,
					Library,
					Loading
				}
		}
</script>
