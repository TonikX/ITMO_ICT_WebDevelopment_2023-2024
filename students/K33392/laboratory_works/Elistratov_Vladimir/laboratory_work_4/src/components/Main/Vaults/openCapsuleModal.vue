<template>
  <div class="modal fade modal-my-config-light" id="openCapsuleFormModalId" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="openCapsuleFormModal" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="modalCapsuleOpenedTitle">{{this.capState.capsule.name}}</h5>
          <button type="button" class="btn btn-my-main" data-bs-dismiss="modal" aria-label="Закрыть">
            <svg class="close-btn">
              <svg id="close" class="close-btn"  viewBox="0 0 16 16">
                <path fill-rule="evenodd" d="M8 2a.5.5 0 0 1 .5.5v5h5a.5.5 0 0 1 0 1h-5v5a.5.5 0 0 1-1 0v-5h-5a.5.5 0 0 1 0-1h5v-5A.5.5 0 0 1 8 2"/>
              </svg>
            </svg>
          </button>
        </div>
        <div class="modal-body" id="modalCapsuleOpenedBody">
          <div class="mb-4">
            <p class="fw-bold">Описание:</p>
            <div>{{ this.capState.capsule.description }}</div>
          </div>

          <hr class="content-dividing-line rounded mt-3"/>
          <div class="form-outline mb-10">
            <p class="fw-bold mb-5">Содержимое капсулы</p>
          </div>

          <div class="mb-4">
            <p class="fw-bold">Послание:</p>

            <div v-for="str in this.capState.capsule.text.split('\n')">
              <div> {{ str }} </div>
            </div>
          </div>
        </div>
        <div class="modal-footer" id="modalCapsuleOpenedFooter">
          <div class="col-12 mb-5">
            <comment-creation/>
          </div>

          <hr class="content-dividing-line rounded mt-3"/>

          <div class="col-12 mb-3" v-for="comment in this.capState.capsule.comments" :key="comment.id">
            <comment
                :id=comment.id
                :userId=comment.person.id
                :userName=comment.person.username
                :commentText=comment.commentText
                :commentDate=comment.commentDate
            />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.modal-my-config{
  --bs-modal-bg: var(--color3);
  --bs-modal-color: var(--color4);
  --bs-modal-border-color: var(--color1);
  --bs-modal-header-border-color: var(--color1);
  --bs-modal-footer-border-color: var(--color1);
}

.modal-my-config-light{
  --bs-modal-bg: var(--color1);
  --bs-modal-color: var(--color4);
  --bs-modal-border-color: var(--color3);
  --bs-modal-header-border-color: var(--color3);
  --bs-modal-footer-border-color: var(--color3);
}
</style>

<script>
import capsulesStore from "@/stores/capsules.js";
import BaseIcon from "@/components/icons/baseIcon.vue";
import Icon from "@/components/icons/baseIcon.vue";
import FriendsList from "@/components/Profile/info/friendsList.vue";
import Comment from "@/components/Main/Comments/comment.vue";
import CommentCreation from "@/components/Main/Comments/commentCreation.vue";


export default {
  name: 'openVaultModal',
  components: {CommentCreation, Comment, FriendsList, Icon, BaseIcon},
  data(){
    return{
      capState: capsulesStore(),
    }
  },
  mounted() {
    //this.capState.loadCapsules()
    this.capState.loadComments(this.capState.capsule.id)
  },
  methods: {
    getComments(){
      this.capState.loadComments(this.capState.capsule.id)
    }
  }
}
</script>