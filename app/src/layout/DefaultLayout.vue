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

<script lang="ts">
import Vue from 'vue'
import CustomHeader from './../components/CustomHeader.vue'
import Component from 'vue-class-component'

@Component({
  components: {
    CustomHeader
  }
})
export default class DefaultLayout extends Vue {
  get theme(): string {
    return (this.$vuetify.theme.dark) ? 'dark' : 'light'
  }
}
</script>
