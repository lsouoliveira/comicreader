<template>
	<div class="books-table">
		<default-table 
			:headers="enabledHeaders"
			:data="books"
		>
			<template v-slot:title="slotProps">
				<div class="books-table__title body-1">
					<img src="../../public/onepiece_vol1_cover.jpg" style="width: 4rem; 4rem;" class="rounded-sm"/>

					<div class="books-table__title-text ml-6">
						{{ getTitle(slotProps.item) }}
						<div v-if="isMobileTableLayoutEnabled">
							<v-chip
								color="warning"
								x-small
								class="mt-2"
							>
								processing
							</v-chip>
						</div>
					</div>
				</div>
			</template>

			<template v-slot:status>
				<v-chip
					color="warning"
				>
					processing
				</v-chip>
			</template>

			<template v-slot:added_at>
				<div style="display: flex; align-items: center; justify-content: space-between;" class="mr-5">
					<span class="body-1 alt--text">20/01/2020</span>
					<v-btn icon>
						<v-icon>mdi-dots-horizontal</v-icon>
					</v-btn>
				</div>
			</template>

			<template v-slot:actions>
				<div style="display: flex; align-items: center; justify-content: flex-end;" class="mr-5">
					<v-btn icon>
						<v-icon>mdi-dots-horizontal</v-icon>
					</v-btn>
				</div>
			</template>
		</default-table>
	</div>
</template>

<script>
import DefaultTable from './../components/DefaultTable.vue'

export default {
	name: "BooksTable",
	props: {
		headers: {
			default: []
		},
		books: {
			default() {
				return []
			}
		}
	},
	components: {
		DefaultTable
	},
	methods: {
		getTitle(item) {
			const foundItem = item.meta.find(m => m.key === "title")

			if(foundItem) {
				return foundItem.value
			}

			return ""
		}
	},
	computed: {
		isMobileTableLayoutEnabled() { 
			switch (this.$vuetify.breakpoint.name) {
				case 'xs':
				case 'sm':
					return true
			}

			return false
		},
		enabledHeaders() {
			if(!this.isMobileTableLayoutEnabled) {
				return this.headers.filter(header => !header.hide)
			}

			return this.headers.filter(header => header.mobile)
		}
	}
}
</script>

<style scoped>
.books-table {
}

.books-table__title {
	max-width: 32rem;
	display: flex;
	align-items: center;
}

.books-table__title-text {
	text-overflow: ellipsis;
  white-space: nowrap;
  overflow: hidden;
}
</style>
