<template>
	<table class="table">
		<tr>
			<th class="body-1" v-for="item in tableHeaders" :key="item.text" @click="() => sort(item)">
				<div>
				{{ !item.hide && item.text || "" }}
				<v-icon small class="ml-3" v-if="!item.hide" >{{ getSortIcon(item.sort) }}</v-icon>
			</div>
			</th>
		</tr>
		<tr class="table__row" v-for="item in data" :key="item.id">
			<td v-for="header in tableHeaders" :key="header.text" class="pa-2">
				{{ item[header.value] }}
				<slot
					:name="header.text"
					:item="item"
				>
				</slot>
			</td>
			<!--
			<td>
				<div style="display: flex; justify-content: flex-end;" class="mr-5">
					<v-btn icon>
						<v-icon>mdi-plus</v-icon>
					</v-btn>
				</div>
			</td>
			-->
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
			default: []
		}
	},
	data() {
		return {
			tableHeaders: this.headers
		}
	},
	methods: {
		sort(item) {
			const itemFound = this.tableHeaders.find(header => header.text === item.text)
			if(!itemFound) return
			const updatedHeaders = this.tableHeaders.map(header => {
				if(header.text !== item.text) {
					header.sort = undefined
				} else {
					let sortType = header.sort

					switch(sortType) {
						case undefined:
							header.sort = "sort_asc"
							break
						case "sort_asc":
							header.sort = "sort_desc"
							break
						default:
							header.sort = undefined
					}
				}

				return header
			})
			this.tableHeaders = updatedHeaders
		},
		getSortIcon(sort) {
			if(sort === "sort_asc") {
				return "mdi-sort-ascending"
			} else if(sort === "sort_desc") {
				return "mdi-sort-descending"
			}
		
			return "";
		}
	},
	computed: {
	}
}
</script>

<style scoped>
.table {
	width: 100%;
	border-spacing: 0 0.75rem;
}

.table td {
	background-color: var(--v-surface-base);
	line-height: 1;
}

.table td:first-child {
	border-radius: 0.5rem 0 0 0.5rem;
}

.table td:last-child {
	border-radius: 0 0.5rem 0.5rem 0;
}

.table th {
	padding: 0.75rem 0rem;
	text-align: left;
	user-select: none;
}

.table th div {
	display: flex;
}

.table th:hover {
	cursor: pointer;
}
</style>
