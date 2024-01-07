<script>
import router from "@/router/index.js";
import {useDate} from "@/composables/date.js";
import usersStore from "@/stores/user.js";
import capsulesStore from "@/stores/capsules.js";

export default {
  name: 'commentCreation',
  data() {
    return {
      form: {
        commentText: 'Текст комментария...',
      },
      capsuleState: capsulesStore(),
    };
  },
  methods:{
    async createComment(){
      let data = this.form
      data['vault_id'] = this.capsuleState.capsule.id
      await this.capsuleState.createComment(data)
      await this.capsuleState.loadComments(this.capsuleState.capsule.id);
      this.form.commentText = "Текст комментария..."
    },
  }
}
</script>

<template>
  <div class="card comment-param">
    <div class="form-outline mb-4">
      <textarea class="form-control mb-2"  v-model="form.commentText"></textarea>
      <button class="btn btn-my-main btn-block" @click="createComment()">
        Отправить
      </button>
    </div>
  </div>
</template>

<style scoped>
  .form-control{
    height: 150px;
  }
</style>