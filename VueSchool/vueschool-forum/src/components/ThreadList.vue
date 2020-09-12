<template>
  <div class="thread-list">
    <h2 class= "mist-little">Threads</h2>
    <ThreadListItem/>
  </div>
</template>
<script>
import ThreadListItem from './ThreadListItem'
export default {
  components: {
    ThreadListItem
  }
}
</script>