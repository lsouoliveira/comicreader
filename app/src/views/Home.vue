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
							<v-text-field
								solo
								flat
								placeholder="Type a comic name"
								append-icon="mdi-magnify"
								hide-details/>
						</v-col>
					</v-row>
				</div>
				<div class="tabs-container">
					<div class="tabs">
						<div class="tabs__names">
							<div><span class="body-1 font-weight-bold">Recently added</span></div>
						</div>
					</div>
					<div class="tabs__content py-5">
						<div class="gallery">
							<div class="gallery__item mr-6">
								<book-card />
							</div>
							<div class="gallery__item mr-6">
								<book-card />
							</div>
						</div>
					</div>
				</div>
				<div class="book-table mt-12">
					<v-row>
						<v-col>
							Title
						</v-col>
					</v-row>
					<div>
						<v-card>
							<v-card-text>
								a
							</v-card-text>
						</v-card>
					</div>
				</div>
			</v-container>
		</template>
	</default-layout>
</template>

<script>
import DefaultLayout from './../layout/DefaultLayout.vue'
import Logo from './../components/Logo.vue'
import BookCard from './../components/BookCard.vue'

export default {
	name: 'Home',
	components: {
		DefaultLayout,
		Logo,
		BookCard
	},
	computed:{
		theme(){
			return (this.$vuetify.theme.dark) ? 'dark' : 'light'
		}
	}
}
</script>

<style lang="scss" scoped>
.gallery {
	display: flex;
	overflow: hidden;
}

.gallery > div { 
	margin: 0;
}

.gallery__item {
	max-width: 12.25rem;
}
</style>
