<template>
	<v-app :style="{background: $vuetify.theme.themes[theme].background}">
		<custom-header>
			<slot name="header"/>
		</custom-header>
		<v-main>
			<slot name="main"/>
		</v-main>
	</v-app>
</template>

<script>
import CustomHeader from './../components/CustomHeader.vue'

export default {
	name: 'DefaultLayout',
	components: {
		CustomHeader
	},
	computed:{
    theme(){
      return (this.$vuetify.theme.dark) ? 'dark' : 'light'
    }
  }
}
</script>
