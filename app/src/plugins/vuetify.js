import Vue from 'vue';
import Vuetify from 'vuetify/lib/framework';


Vue.use(Vuetify);

export default new Vuetify({
  theme: {
    options: {
      customProperties: true,
    },
    themes: {
      light: {
				primary: "#000000",
				background: "#eeeeee",
				warning: "#ffb74d",
				surface: '#ffffff',
				alt: "#9e9e9e",
				green: "#81c784"
      }
    },
		dark: false,
  },
});
