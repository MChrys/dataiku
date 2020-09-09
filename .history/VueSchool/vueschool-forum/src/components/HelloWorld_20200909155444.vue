<template>
  <div>
    <h1>Welcome to the forum </h1>
    <div v-for="thread in threads" v-bind:key="thd">

      <h2>{{ thd.title }}</h2>  
      <div v-for="postId in thd.posts" v-bind:key="pId">
        <h3>{{ pId }}</h3>  
        <h3>{{ posts[pId].userId }}</h3>  

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