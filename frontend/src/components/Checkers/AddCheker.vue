<template>
<form class="form-horizontal">
<div>
  <center>
    <h5>
      Create
    </h5>
  </center>
</div>
<div class="form-group">
  <div class="col-3">
    <label class="form-label">Name</label>
  </div>
  <div class="col-9">
    <input class="form-input" type="text" v-model="name" placeholder="Type checker name..."/>
  </div>
</div>
<div class="form-group">
  <div class="col-3">
    <label class="form-label">Description</label>
  </div>
  <div class="col-9">
    <input class="form-input" type="text" v-model="description" placeholder="Type checker description..."/>
  </div>
</div>
<div class="form-group">
  <div class="col-3">
    <label class="form-label">File</label>
  </div>
  <div class="col-9">
    <input class="form-input" type="file" @change="filesChange('file', $event.target.files)"/>
  </div>
</div>
<div class="form-group">
  <div class="col-3"></div>
  <div class="col-9">
    <button class="btn btn-primary" @click="save()">Create</button>
  </div>
</div>
</form>
</template>

<script>

export default {
  name: 'add-checker',
  data () {
    return {
      'name': '',
      'description': '',
      'formData': {}
    }
  },
  methods: {
    filesChange (fieldName, fileList) {
      // handle file changes
      const formData = new FormData()

      if (!fileList.length) return

      // append the files to FormData
      Array
        .from(Array(fileList.length).keys())
        .map(x => {
          formData.append(fieldName, fileList[x], fileList[x].name)
        })

      // save it
      this.formData = formData
    },
    save () {
      if (this.formData) {
        this.formData.append('name', this.name)
        this.formData.append('description', this.description)
        this.formData.append('author', this.$store.getters.userInfo.id)

        this.$store.dispatch('createChecker', this.formData)
      }
    }
  }
}
</script>

<style>
</style>
