<template>

	<default-layout>
		<template v-slot:header>
			<logo />
			<v-spacer />
			<v-btn icon @click="handleOpenFileDialog">
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
							<div>
								<span class="body-2 font-weight-bold">Recently added</span>
							</div>
						</div>
					</div>
					<div class="tabs__content py-5">
						<div class="gallery pb-5">
							<div class="gallery__item mr-6" v-for="item in Array(20)" :key="item">
								<book-card />
							</div>
						</div>
					</div>
				</div>

				<div class="books-table-container mt-12">
					<books-table
						:headers="headers"
						:books="books"
					/>
				</div>
			</v-container>
			<file-upload-dialog :dialog="isFileDialogOpened" @close="isFileDialogOpened = false" />
		</template>
	</default-layout>
</template>

<script>
import DefaultLayout from './../layout/DefaultLayout.vue'
import Logo from './../components/Logo.vue'
import BookCard from './../components/BookCard.vue'
import BooksTable from './../components/BooksTable.vue'
import FileUploadDialog from './../components/FileUploadDialog.vue'

export default {
	name: 'Home',
	components: {
		DefaultLayout,
		Logo,
		BookCard,
		BooksTable,
		FileUploadDialog
	},
	data() {
		return {
			isFileDialogOpened: false,
			headers: [
				{
					key: "title",
					text: "Title",
					value: "",
					mobile: true
				},
				{
					key: "status",
					text: "Status",
					value: ""
				},
				{
					key: "added_at",
					text: "Added at",
					value: ""
				},
				{
					key: "actions",
					text: "",
					value: "",
					mobile: true,
					hide: true
				}
			],
			books: 
				[
				{ "created_at": "2021-11-03", "book_process": { "error_code": 0, "file_id": "6b99219f-c595-4bf0-8fd7-bb9d84b2d1e1.cbz", "status": "running" }, "cover_image": "bb851e7c-58ad-4596-8fd5-eb3210347a81.jpg", "id": 1, "meta": [ { "data_type": "string", "key": "title", "value": "sample" } ], "num_pages": 3, "reading_progress": { "page": 1, "read": false, "updated_at": "2021-11-03" } }, { "book_process": { "error_code": 0, "file_id": "62b37a01-7d0c-4282-a154-d68d3447f65b.cbz", "status": "running" }, "cover_image": "a99f40fe-6a6b-4254-83a4-8c0509e2b111.jpg", "id": 2, "meta": [ { "data_type": "string", "key": "title", "value": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus eu vehicula mi, et dictum velit. Maecenas aliquet ut leo id interdum. Proin rhoncus metus nec mi egestas dictum. Nunc fermentum at lectus id suscipit. Nam imperdiet dolor semper libero tincidunt pulvinar. Mauris et libero risus. Morbi aliquet magna et eros sagittis vulputate" } ], "num_pages": 3, "reading_progress": { "page": 1,
					"read": false,
					"updated_at": "2021-11-03"
				}
				},
				{
					"book_process": {
						"error_code": 0,
						"file_id": "654d3277-e119-4eda-b4e3-c8535823bc00.cbz",
						"status": "running"
					},
					"cover_image": "32ae3a4e-c345-4b75-b5b9-7036b3948e95.jpg",
					"id": 3,
					"meta": [
						{
							"data_type": "string",
							"key": "title",
							"value": "One piece vol 1"
						}
					],
					"num_pages": 3,
					"reading_progress": {
						"page": 1,
						"read": false,
						"updated_at": "2021-11-03"
					}
				},
				{
					"book_process": {
						"error_code": 0,
						"file_id": "cebb8296-d7c6-4e2a-b061-08f4370b8cde.cbz",
						"status": "running"
					},
					"cover_image": "5576bdd2-7038-4b18-a97d-54ec7da5a1ef.jpg",
					"id": 4,
					"meta": [
						{
							"data_type": "string",
							"key": "title",
							"value": "sample2"
						}
					],
					"num_pages": 3,
					"reading_progress": {
						"page": 1,
						"read": false,
						"updated_at": "2021-11-03"
					}
				},
				{
					"book_process": {
						"error_code": 0,
						"file_id": "ba4f4ac3-6729-4887-bd41-49c83da5af3b.cbz",
						"status": "running"
					},
					"cover_image": "876f651e-c491-4210-bd09-670d63c77c90.jpg",
					"id": 5,
					"meta": [
						{
							"data_type": "string",
							"key": "title",
							"value": "sample"
						}
					],
					"num_pages": 3,
					"reading_progress": {
						"page": 1,
						"read": false,
						"updated_at": "2021-11-03"
					}
				},
				{
					"book_process": {
						"error_code": 0,
						"file_id": "9c117895-e926-4233-ba86-6fd5914a1df1.cbz",
						"status": "running"
					},
					"cover_image": "7b7be72d-d8e2-48b8-9c6a-bfa5f8a3ce74.jpg",
					"id": 6,
					"meta": [
						{
							"data_type": "string",
							"key": "title",
							"value": "sample2"
						}
					],
					"num_pages": 3,
					"reading_progress": {
						"page": 1,
						"read": false,
						"updated_at": "2021-11-03"
					}
				},
				{
					"book_process": {
						"error_code": 0,
						"file_id": "c77de19a-1734-4031-a423-294ecadd2865.cbz",
						"status": "running"
					},
					"cover_image": "71b0c292-9cc5-4188-80ed-a3952e172045.jpg",
					"id": 7,
					"meta": [
						{
							"data_type": "string",
							"key": "title",
							"value": "sample"
						}
					],
					"num_pages": 3,
					"reading_progress": {
						"page": 1,
						"read": false,
						"updated_at": "2021-11-03"
					}
				},
				{
					"book_process": {
						"error_code": 0,
						"file_id": "92aeec61-0774-4eb2-a75e-2ced0c5537d4.cbz",
						"status": "running"
					},
					"cover_image": "dc67326c-c8b5-424a-8082-f885ed54b111.jpg",
					"id": 8,
					"meta": [
						{
							"data_type": "string",
							"key": "title",
							"value": "sample2"
						}
					],
					"num_pages": 3,
					"reading_progress": {
						"page": 1,
						"read": false,
						"updated_at": "2021-11-03"
					}
				},
				{
					"book_process": {
						"error_code": 0,
						"file_id": "0dad8aa0-5bb7-494d-ab8a-25906b8c7e78.cbz",
						"status": "running"
					},
					"cover_image": "c4b157bc-1544-409f-adae-7157b0e6a8c0.jpg",
					"id": 9,
					"meta": [
						{
							"data_type": "string",
							"key": "title",
							"value": "sample"
						}
					],
					"num_pages": 3,
					"reading_progress": {
						"page": 1,
						"read": false,
						"updated_at": "2021-11-03"
					}
				},
				{
					"book_process": {
						"error_code": 0,
						"file_id": "3806226c-3c42-4ca9-86fe-aac2c0b7a23a.cbz",
						"status": "running"
					},
					"cover_image": "e1b6757c-63d1-40b0-a352-172959902286.jpg",
					"id": 10,
					"meta": [
						{
							"data_type": "string",
							"key": "title",
							"value": "sample2"
						}
					],
					"num_pages": 3,
					"reading_progress": {
						"page": 1,
						"read": false,
						"updated_at": "2021-11-03"
					}
				},
				{
					"book_process": {
						"error_code": 0,
						"file_id": "55a2ced7-0b72-46fe-8871-77f54a1a8133.cbz",
						"status": "running"
					},
					"cover_image": "2b5c00f6-6f7b-40fe-a460-343a887c64e0.jpg",
					"id": 11,
					"meta": [
						{
							"data_type": "string",
							"key": "title",
							"value": "sample"
						}
					],
					"num_pages": 3,
					"reading_progress": {
						"page": 1,
						"read": false,
						"updated_at": "2021-11-03"
					}
				},
				{
					"book_process": {
						"error_code": 0,
						"file_id": "94d3dbd3-20f2-4ca7-acf7-5368d568577d.cbz",
						"status": "running"
					},
					"cover_image": "b30a27ab-6302-4e4e-a28b-fcc9d8801601.jpg",
					"id": 12,
					"meta": [
						{
							"data_type": "string",
							"key": "title",
							"value": "sample2"
						}
					],
					"num_pages": 3,
					"reading_progress": {
						"page": 1,
						"read": false,
						"updated_at": "2021-11-03"
					}
				},
				{
					"book_process": {
						"error_code": 0,
						"file_id": "b729b883-7118-4342-9be4-b1d06a49709d.cbz",
						"status": "running"
					},
					"cover_image": "c1b8055e-e068-4767-8696-e8dba37813f6.jpg",
					"id": 13,
					"meta": [
						{
							"data_type": "string",
							"key": "title",
							"value": "sample"
						}
					],
					"num_pages": 3,
					"reading_progress": {
						"page": 1,
						"read": false,
						"updated_at": "2021-11-03"
					}
				},
				{
					"book_process": {
						"error_code": 0,
						"file_id": "7da3d97e-fbc2-4c81-8f0b-e495142f3a2e.cbz",
						"status": "running"
					},
					"cover_image": "530655bc-1cb6-46ec-abd3-671d1560e9d6.jpg",
					"id": 14,
					"meta": [
						{
							"data_type": "string",
							"key": "title",
							"value": "sample2"
						}
					],
					"num_pages": 3,
					"reading_progress": {
						"page": 1,
						"read": false,
						"updated_at": "2021-11-03"
					}
				},
				{
					"book_process": {
						"error_code": 0,
						"file_id": "4663ed2b-56ce-4bba-a587-a38c57c35b19.cbz",
						"status": "running"
					},
					"cover_image": "4e49990c-2d80-44d1-b905-f13585e22352.jpg",
					"id": 15,
					"meta": [
						{
							"data_type": "string",
							"key": "title",
							"value": "sample"
						}
					],
					"num_pages": 3,
					"reading_progress": {
						"page": 1,
						"read": false,
						"updated_at": "2021-11-03"
					}
				},
				{
					"book_process": {
						"error_code": 0,
						"file_id": "365485b0-ca9f-46e2-a7a0-b6942b6eb6ef.cbz",
						"status": "running"
					},
					"cover_image": "a156a676-34fe-44bc-8c41-8da1baf81d02.jpg",
					"id": 16,
					"meta": [
						{
							"data_type": "string",
							"key": "title",
							"value": "sample2"
						}
					],
					"num_pages": 3,
					"reading_progress": {
						"page": 1,
						"read": false,
						"updated_at": "2021-11-03"
					}
				},
				{
					"book_process": {
						"error_code": 0,
						"file_id": "5ec27263-5f8c-4cf9-af19-7fc764e0ba22.cbz",
						"status": "running"
					},
					"cover_image": "6a67c774-409c-4731-b9ce-9a08f12759bd.jpg",
					"id": 17,
					"meta": [
						{
							"data_type": "string",
							"key": "title",
							"value": "sample"
						}
					],
					"num_pages": 3,
					"reading_progress": {
						"page": 1,
						"read": false,
						"updated_at": "2021-11-03"
					}
				},
				{
					"book_process": {
						"error_code": 0,
						"file_id": "fdb26d59-7bb9-4c18-b88e-61edf33d82c5.cbz",
						"status": "running"
					},
					"cover_image": "3ee2db34-8503-49b7-ae31-2cdade37a329.jpg",
					"id": 18,
					"meta": [
						{
							"data_type": "string",
							"key": "title",
							"value": "sample2"
						}
					],
					"num_pages": 3,
					"reading_progress": {
						"page": 1,
						"read": false,
						"updated_at": "2021-11-03"
					}
				},
				{
					"book_process": {
						"error_code": 0,
						"file_id": "8760176d-f9bc-4b26-bbb1-beb6c8b5241b.cbz",
						"status": "running"
					},
					"cover_image": "52fe39b0-cb77-49c3-85ba-dba8adfe290e.jpg",
					"id": 19,
					"meta": [
						{
							"data_type": "string",
							"key": "title",
							"value": "sample"
						}
					],
					"num_pages": 3,
					"reading_progress": {
						"page": 1,
						"read": false,
						"updated_at": "2021-11-03"
					}
				},
				{
					"book_process": {
						"error_code": 0,
						"file_id": "86541c1a-5df5-499d-81c7-704f4329a94f.cbz",
						"status": "running"
					},
					"cover_image": "cbf10426-b252-463f-bd50-38ce11eab5d0.jpg",
					"id": 20,
					"meta": [
						{
							"data_type": "string",
							"key": "title",
							"value": "sample2"
						}
					],
					"num_pages": 3,
					"reading_progress": {
						"page": 1,
						"read": false,
						"updated_at": "2021-11-03"
					}
				}
			]
		}
	},
	methods: {
		handleOpenFileDialog() {
			this.isFileDialogOpened = true
		}
	},
	computed: {
		theme() {
			return (this.$vuetify.theme.dark) ? 'dark' : 'light'
		}
	}
}
</script>

<style lang="scss" scoped>
.gallery {
	display: flex;
	overflow: hidden;
	overflow-x: auto;
}

.gallery > div { 
	margin: 0;
}

.gallery__item {
	max-width: 12.25rem;
}

.books-table-container {
	overflow: hidden;
	overflow-x: auto;
}
</style>
