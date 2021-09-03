<template>
	<v-app>
		<custom-header>
		</custom-header>
		<v-main>
			<v-container>
				<v-row 
					no-gutters
					justify="center"
				>
					<v-col md="7" lg="4">
						<v-card>
							<v-card-title>Add Comics</v-card-title>
							<v-divider />
							<v-card-text>
								<div class="upload-area">
									<div>
										<p><v-icon x-large class="upload-area__icon rounded-circle">mdi-publish</v-icon></p>
										<p class="">Drag & Drop files here</p>
										<p>or</p>
										<v-btn
											color="primary"
										>
											Browse files
										</v-btn>
									</div>
								</div>
							</v-card-text>
						</v-card>
					</v-col>
				</v-row>
			</v-container>
		</v-main>
	</v-app>
</template>

<script>
	import CustomHeader from '../components/CustomHeader.vue'

	export default {

			name: 'AddComics',
			components: {
					CustomHeader
				}
		}
</script>

<style>
	.upload-area {
		display: flex;
		justify-content: center;
		align-items: center;
		min-height: 320px;
		text-align: center;
		border: 2px dashed var(--v-primary-base);
	}

</style>
