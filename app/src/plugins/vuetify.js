import Vue from 'vue';
import Vuetify from 'vuetify/lib/framework';

import colors from 'vuetify/lib/util/colors';

Vue.use(Vuetify);

export default new Vuetify({
  theme: {
    options: {
      customProperties: true,
    },
    themes: {
      light: {
				primary: colors.lightBlue.base,
				background: colors.grey.lighten3,
				surface: '#ffffff'
      }
    },
		dark: false,
  },
});
