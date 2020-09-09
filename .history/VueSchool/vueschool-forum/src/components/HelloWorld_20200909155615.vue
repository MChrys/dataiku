<template>
  <div>
    <h1>Welcome to the forum </h1>
    <div v-for="thread in threads" :key="thread">

      <h2>{{ thread.title }}</h2>  
      <div v-for="postId in thread.posts" :key="postId">
        <h3>{{ postId }}</h3>  
        <h3>{{ posts[postId].userId }}</h3>  

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