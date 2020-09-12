<template>
  <div>
    <div v-for="(thread, z) in threads" v-bind:key="z" class="col-large push-top">

        <h1>{{ thread.title }}</h1>

        <div class="post-list">

            <div v-for="(postId,o) in thread.posts" :key="o" class="post">

                <div class="user-info">
                    <a href="#" class="user-name"> {{ users[posts[postId].userId].name }} </a>
                    <!-- <p>{{ users[posts[postId].userId].avatar  }}</p>-->
                    <a href="#">
                        <img class="avatar-large" v-bind:src="users[posts[postId].userId].avatar" alt="">
                    </a>

                    <p class="desktop-only text-small">107 posts</p>

                </div>

                <div class="post-content">
                    <div>
                      {{posts[postId].text}}
                    </div>
                    
                </div>



                <div class="post-date text-faded">
                    {{ posts[postId].publishedAt }}
                </div>



            </div>
        </div>
    </div>
  </div>


</template>
<script>
import sourceData from '@/data'
import ThreadList from './ThreadList'
console.log(sourceData)
export default {
  name: 'HelloWorld',
  components: {
    ThreadList
  },
  
  data () {
    return {
      threads: sourceData.threads,
      posts: sourceData.posts,
      users: sourceData.users
    }
  }
}
</script>

