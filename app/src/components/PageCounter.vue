<template>
	<div class="page-counter d-flex align-center">
		<div>
		<v-text-field
			hide-details
			single-line
			solo-inverted
			:value="page"
			class="page-counter__page"
			@keydown="handleKeyDown"
			@input="handleInput"
			placeholder="0"/>
		</div>
		<div>
			<span>/</span>
		</div>
		<div>
			<span>{{ maxPages }}</span>
		</div>
	</div>
</template>

<script>
	export default {
			name: 'PageCounter',
			props: {
					page: {
							type: Number,
							default: 0
					},
					maxPages: {
							type: Number,
							default: 0
					}
			},
			data() {
				return {
					currentValue: {
						type: Number,
						default: this.page 
					}
				};
			},
			methods: {
				handleInput(val) {
					this.currentValue = val;
				},
				handleKeyDown(e) {
					if(e.keyCode === 13 && this.page !== this.currentValue) {
						this.onPageChange();
					}
				},
				onPageChange() {
					this.$emit('page-change', this.currentValue);
					this.currentValue = this.page;
				}
			}
		};
</script>

<style>
	.page-counter div + div {
		margin-left: 8px;
	}

	.page-counter__page {
		flex: 0;
	}

	.page-counter__page .v-input__control {
		min-height: 0 !important;
	}

	.page-counter__page input {
		max-width: 32px;
		text-align: center;
	}
</style>
