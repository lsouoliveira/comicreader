<template>
	<v-app>
		<v-app-bar app dark color="primary" class="app-bar" :class="appBarClassObject">
			<v-toolbar-title class="logo title">Comic Reader</v-toolbar-title>
			<v-spacer class="app-bar__spacer"/>
				<v-flex class="app-bar__search-input">
					<v-text-field
						hide-details
						single-line
						placeholder="Search for comics"/>
				</v-flex>
				<v-spacer class="app-bar__second-spacer"/>
					<v-btn 
									icon
									class="app-bar__btn-search"
									@click="handleSearchBtnClick"
									>
									<v-icon>mdi-magnify</v-icon>
					</v-btn>
					<v-btn 
									icon
									href="comics/add"
									>
									<v-icon>mdi-plus</v-icon>
					</v-btn>
		</v-app-bar>
		<v-main>
			<v-container>
				<library/>
			</v-container>
			<Loading />
		</v-main>
	</v-app>
</template>

<script>
	import Library from './../components/Library.vue'
	import Loading from './../components/Loading.vue'

	export default {
			name: 'Home',
			components: {
					Library,
					Loading
				},
			data() {
					return {
							showSearchInput: false
						}
				},
			methods: {
					handleSearchBtnClick() {
							this.showSearchInput = true;
						}
				},
			computed: {
					appBarClassObject() {
						return {
							'app-bar--search-enabled': this.showSearchInput
						}
					}
				}
		}
</script>
<style lang="scss">
	@import '~vuetify/src/components/VStepper/_variables.scss';

	.app-bar__search-input, .app-bar__spacer {
		display: none;
	}

	.app-bar.app-bar--search-enabled .logo,
	.app-bar.app-bar--search-enabled .app-bar__btn-search,
	.app-bar.app-bar--search-enabled .app-bar__second-spacer {
		display: none;
	}

	.app-bar--search-enabled .app-bar__search-input {
		display: block;
	}

	@media #{map-get($display-breakpoints, 'sm-and-up')} {
		.app-bar.app-bar--search-enabled .logo,
		.app-bar.app-bar--search-enabled .app-bar__btn-search,
		.app-bar.app-bar--search-enabled .app-bar__second-spacer {
			display: block;
		}

		.app-bar.app-bar--search-enabled .app-bar__btn-search,
		.app-bar__btn-search {
			display: none;
		}

		.app-bar__search-input, .app-bar__spacer {
			display: block;
		}
	}
</style>
