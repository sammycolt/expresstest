<template>
  <nav  class="navbar">
    <section class="navbar-section">
        <a class="btn btn-default" v-on:click="changeValue(true)">Create</a>
    </section>
    <section class="navbar-center"></section>
    <section class="navbar-section">
      <a class="btn btn-default" v-on:click="changeValue(false)">List</a>
    </section>
  </nav>
</template>

<script>
  export default {
    name: 'navbar',
    methods: {
      changeValue (newValue) {
        this.$parent.variant_ = newValue
      }
    }
  }
</script>
