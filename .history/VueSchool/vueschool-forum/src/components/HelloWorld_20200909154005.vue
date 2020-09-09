<template>
  <div>
    <h1>Welcome to the forum </h1>
    <div v-for="thread in threads" v-bind:key="thread">

      <h2>123</h2>  



      </div>

    </div>
  </div>
</template>
<script>
import sourceData from '@/data'
console.log(sourceData)
export default {
  name: 'HelloWorld',
  data () {
    return {
      threads: sourceData.threads,
      posts: sourceData.threads,
      users: sourceData.users
    }
  }
}
</script>