<template>
  <div class="hello">
    <h1>Welcome to the forum </h1>
  </div>
</template>
<script>
import sourceData from '@/data'
console.log(sourcedData)
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