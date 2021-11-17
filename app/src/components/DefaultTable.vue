<template>
	<table class="table">
		<tr>
			<th class="subtitle-1" v-for="item in headers" :key="item.key" @click="() => sort(item)">
				<div>
					{{ !item.hide && item.text || "" }}
					<v-icon small class="ml-3">{{ getSortIcon(item) }}</v-icon>
				</div>
			</th>
		</tr>
		<tr class="table__row" v-for="item in data" :key="item.id">
			<td v-for="header in headers" :key="header.key">
				{{ item[header.value] }}
				<slot
					:name="header.key"
					:item="item"
				>
				</slot>
			</td>
		</tr>
	</table>
</template>

<script>
export default {
	name: 'DefaultTable',
	props: {
		headers: {
			default: []
		},
		data: {
			default() {
				return []
			}
		}
	},
	data() {
		return {
			sortedField: null,
			sortType: undefined
		}
	},
	methods: {
		sort(header) {
			const foundHeader = this.headers.find(h => h.key === header.key)

			if(!foundHeader) return

			this.sortedField = foundHeader.key

			switch(this.sortType) {
				case undefined:
					this.sortType = "sort_asc"
				break
				case "sort_asc":
					this.sortType = "sort_desc"
				break
				default:
					this.sortType = undefined
			}
		},
		getSortIcon(header) {
			if(header.key !== this.sortedField) {
				return null
			}

			if(this.sortType === "sort_asc") {
				return "mdi-sort-ascending"
			} else if(this.sortType === "sort_desc") {
				return "mdi-sort-descending"
			}

			return "";
		}
	}
}
</script>

<style scoped>
.table {
	width: 100%;
	border-spacing: 0 0.75rem;
	table-layout: fixed;
}

.table td {
	background-color: var(--v-surface-base);
	line-height: 1;
}

.table td:first-child {
	border-radius: 0.5rem 0 0 0.5rem;
	padding: 0.5rem 0.75rem;
}

.table td:last-child {
	border-radius: 0 0.5rem 0.5rem 0;
}

.table th {
	padding: 0.75rem 0rem;
	text-align: left;
	user-select: none;
	color: var(--v-alt-base);
	font-weight: 600;
}

.table th div {
	display: flex;
}

.table th:hover {
	cursor: pointer;
}
</style>
