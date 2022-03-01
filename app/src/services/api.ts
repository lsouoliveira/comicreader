import axios from "axios"

export default axios.create({
	baseURL: process.env.VUE_APP_COMIC_READER_API 
})
