<template>
	<div class="book-card">
    <router-link :to="readerUrl" @click.native.capture="handleSelectBook">
      <div class='cover'>
        <img :src='thumbnailUrl' :style="coverImageStylesObject" :title="title"/>
      </div>
    </router-link>
		<div class="mt-1 book-card__info-header">
				<span class="font-weight-bold text-body-1 secondary--text book-card__title me-1">{{title}}</span>
			<div>
      <v-menu offset-y>
        <template v-slot:activator="{ on, attrs }">
          <v-btn
            class="secondary--text"
            icon
            small
            v-bind="attrs"
            v-on="on"
          >
            <v-icon style="font-size: 1.42rem;">mdi-dots-vertical</v-icon>
          </v-btn>
        </template>
        <v-list>
          <v-list-item link @click="handleMarkAsRead" v-if="!read">
            Mark as read
          </v-list-item>
          <v-list-item link @click="handleMarkAsRead" v-if="read">
            Mark as unread
          </v-list-item>
          <v-divider />
          <v-list-item link @click="handleRemoveBtnClick">
            Remove
          </v-list-item>
        </v-list>
      </v-menu>
			</div>
		</div>
		<div class="mt-1">
			<v-chip color="green" small v-if="read">read</v-chip>
		</div>
	</div>
</template>

<script>
export default {
	name: 'BookCard',
	props: {
		id: {
      type: String,
      default: ""
    },
		read: {
			type: Boolean,
			default: false
		},
    title: {
      type: String,
      default: ""
    },
    thumbnailUrl: {
      type: String,
      default: ""
    },
    readerUrl: {
      type: String,
      default: ""
    },
    status: {
      type: Number,
      default: 0
    }
	},
  methods: {
    handleRemoveBtnClick() {
      this.$emit("remove", this.id)
    },
    handleMarkAsRead() {
      this.$emit("mark-as-read", this.id)
    },
    handleSelectBook(e) {
      if(this.isFinished) {
        return
      }

      e.preventDefault()
      this.$emit('book-unavailable', { bookId: this.id, status: this.status })
    }
  },
  computed: {
    coverImageStylesObject() {
      return {
        opacity: this.isFinished ? '1' : '0.25'
      }
    },
    isFinished() {
      return this.status === 1
    }
  }
}
</script>

<style scoped>
.book-card {
	background: none;
}

.book-card__title {
	white-space: nowrap;
	text-overflow: ellipsis;
	overflow: hidden;
}

.book-card__info-header {
	display: flex;
	justify-content: space-between;
	align-items: center;
}

.cover {
	display: flex;
	flex-direction: column;
  min-width: 9.14rem;
  min-height: 14.624rem;
  background-color: lightgrey;
}

.cover:hover {
	cursor: pointer;
}
</style>
