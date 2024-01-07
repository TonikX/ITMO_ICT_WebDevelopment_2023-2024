<script>
  import RegModal from "@/components/auth/regModel.vue";
  import VaultCreationModal from "@/components/Main/Vaults/creationCapsuleModal.vue";
  import usersStore from "@/stores/user.js";
  import capsulesStore from "@/stores/capsules.js";
  import router from "@/router/index.js";

  export default {
    name: 'loggedMainHeader',
    components: {VaultCreationModal},
    data(){
      return{
        usState: usersStore(),
        userD: {},
      }
    },
    async mounted() {
      this.userD = this.usState.user
    },
    methods: {
      goToProfile() {
        //console.log(this.usState.user)
       router.push({name: 'profile', params: {userId: this.userD.id} })
      }
    }
  }
</script>

<template>
  <nav class="navbar navbar-expand-lg">
    <div class="container-fluid">
      <h1>TimeVault</h1>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <svg class="navbar-toggler-icon" viewBox="0 0 16 16">
          <path fill-rule="evenodd" d="M2.5 12a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5m0-4a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5m0-4a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5"/>
        </svg>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav border-start border-2 ms-auto">
          <li class="nav-item ms-2 mb-1">
            <button type="button" class="btn btn-lg btn-my-main" data-bs-toggle="modal" data-bs-target="#CreateCapsuleFormModalId" tabindex="0">
              Создать капсулу
              <svg id="addIcon" class="icons" viewBox="0 0 16 16">
                <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"/>
                <path d="M8 4a.5.5 0 0 1 .5.5v3h3a.5.5 0 0 1 0 1h-3v3a.5.5 0 0 1-1 0v-3h-3a.5.5 0 0 1 0-1h3v-3A.5.5 0 0 1 8 4z"/>
              </svg>
            </button>
          </li>
          <li class="nav-item ms-2 mb-1">
            <button type="button" class="btn btn-lg btn-my-main" @click="goToProfile" tabindex="0">
              Профиль
              <svg id="profileIcon" class="icons" viewBox="0 0 16 16">
                <path d="M11 6a3 3 0 1 1-6 0 3 3 0 0 1 6 0z"/>
                <path fill-rule="evenodd" d="M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8zm8-7a7 7 0 0 0-5.468 11.37C3.242 11.226 4.805 10 8 10s4.757 1.225 5.468 2.37A7 7 0 0 0 8 1z"/>
              </svg>
            </button>
          </li>
        </ul>
      </div>
    </div>
  </nav>
  <vault-creation-modal/>
</template>

<style>

</style>