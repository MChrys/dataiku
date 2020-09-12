<template>
  <div>
    <h1>Welcome to the forum </h1>
    <div v-for="(thread, i) in threads" :key="i">

      <h2>{{ thread.title }}</h2>  
      <div v-for="(postId, y) in thread.posts" :key="y">
        <p>{{ users[posts[postId].userId] }}</p>
        <p>{{ posts[postId].text }}</p>  


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
      posts: sourceData.posts,
      users: sourceData.users
    }
  }
}
</script>