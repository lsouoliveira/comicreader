<template>
  <v-dialog
    v-model="dialog"
    max-width="290"
  >
    <v-card>
      <v-card-title class="text-h6">
        {{ title }}
      </v-card-title>

      <v-card-text class="text-center">
        {{ description }}
      </v-card-text>

      <v-card-actions>
        <v-btn
          color="primary"
          text
          @click="dialog = false"
        >
          Cancel
        </v-btn>

        <v-spacer></v-spacer>

        <v-btn
          color="primary"
          @click="handleConfirmButtonClick"
        >
          {{ confirmButtonValue }}
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script lang="ts">
import { Vue, Component, Watch } from 'vue-property-decorator'

const GenericConfirmationDialogProps = Vue.extend({
  props: {
    title: {
      type: String,
      default: ""
    },
    description: {
      type: String,
      default: ""
    },
    confirmButtonValue: {
      type: String,
      default: ""
    },
    show: {
      type: Boolean,
      default: false 
    }
  }
})

@Component
export default class GenericConfirmationDialog extends GenericConfirmationDialogProps {
  dialog = this.show

  @Watch("show")
  watchShow(newValue: boolean): void {
    this.dialog = this.show
  }

  @Watch("dialog")
  watchIsDialogOpen(newValue: boolean): void {
    if(!newValue) {
      this.$emit("close")
    }
  }

  handleConfirmButtonClick() {
    this.$emit("confirm")
    this.dialog = false
  }
}
</script>
