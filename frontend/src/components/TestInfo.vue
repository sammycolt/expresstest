<template>
<div>
  <a>Test: {{ title }}</a>
</div>
</template>

<script>

import { mapState } from 'vuex'

export default {
  name: 'test-info',
  computed: mapState({
    title (state) {
      if (state.testDetails[this.id]) {
        return state.testDetails[this.id].title
      }
    }
  }),
  data () {
    return {
      id: this.$route.params.id
    }
  },
  created: function () {
    this.$store.dispatch('getTestDetails', this.id)
  }
}
</script>
