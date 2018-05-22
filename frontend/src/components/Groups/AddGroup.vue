<template>
<div>
  <div class="panel" v-if="groupsDictionaryByName">
    <div class="panel-header text-center">
      <div class="panel-title h5 mt-10">Share test to group</div>
    </div>
    <div class="panel-body">
      <div>
        <form class="form-horizontal">
          <div class="form-group">
            <select class="form-select" v-model="grp">
              <option v-for="group in this.groups">{{ group.name }}</option>
            </select>
        </div>
        </form>
      </div>
    </div>
    <div class="panel-footer">
      <div class="form-group">
        <div>
          <button class="btn btn-primary btn-block" @click="share">Share</button>
        </div>
      </div>
    </div>
  </div>
  <groups-list :testId="this.testId"></groups-list>
</div>
</template>

<script>

import { mapGetters } from 'vuex'
import GroupsList from './GroupsList.vue'

export default{
  name: 'add-group',
  props: ['testId'],
  components: {
    'groups-list': GroupsList
  },
  computed: mapGetters(['groups', 'groupsDictionaryByName']),
  data () {
    return {
      'grp': {}
    }
  },
  methods: {
    share (event) {
      var group1 = this.groupsDictionaryByName[this.grp]
      var payload = {
        'group': group1.id,
        'quiz': this.testId
      }
      this.$store.dispatch('addGroupToTest', payload)
      event.preventDefault()
    }
  },
  created: function () {
    this.$store.dispatch('getGroups').then(response => {
//      for (var i in this.students) {
//        this.studentsDictionaryByUsername[this.students[i].username] = this.students[i]
//      }
    })
  }

}
</script>
