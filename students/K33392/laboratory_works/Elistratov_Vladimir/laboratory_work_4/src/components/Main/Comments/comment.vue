<script>
import {useDate} from "@/composables/date.js";
import router from "@/router/index.js";

export default {
  name: 'comment',
  props: {
    id: {
      type: Number,
    },
    userId: {
      type: Number,
    },
    userName: {
      type: String,
    },
    commentText: {
      type: String,
    },
    commentDate: {
      type: Date,
    },
  },
  methods:{
    goToProfile() {
      router.push({name: 'profile', params: {userId: this.userId} })
    },
    getNormalDate(){
      return useDate(this.commentDate)
    },
  }
}
</script>

<template>
  <div class="card comment-param">
    <div class="card-body">
      <h5 class="owner-link card-title justify-f-e" @click="goToProfile" tabindex="0" data-bs-dismiss="modal">@{{ userName }}</h5>
      <div v-for="str in this.commentText.split('\n')">
        <p class="card-text"> {{ str }} </p>
      </div>
    </div>
    <div class="card-footer">
      <p class="card-text mb-2 justify-f-e">{{ getNormalDate() }}</p>
    </div>
  </div>
</template>

<style scoped>
  .comment-param{
    background-color: var(--color3);
    color: var(--color4);
    max-height: 460px;
  }
  .owner-link:hover{
    color: var(--color2)
  }
</style>