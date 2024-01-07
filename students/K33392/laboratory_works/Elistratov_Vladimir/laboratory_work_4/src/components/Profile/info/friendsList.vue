<script>
  import {useDate} from "@/composables/date.js";
  import router from "@/router/index.js";

  export default {
    name: 'friendsList',
    props: {
      id: {
        type: Number,
      },
      userName: {
        type: String,
      },
      firstName: {
        type: String,
      },
      lastName: {
        type: String,
      },
    },
    methods:{
      goToProfile(){
        location.href=`/vaulttec/profile/${this.id}`
      }
    }
  }
</script>

<template>
  <div class="card capsule-param">
    <div class="card-body">
      <h5 class="owner-link card-title justify-f-e" @click="goToProfile" tabindex="0" >@{{ userName }}</h5>
      <p class="card-text mb-2">Имя: {{ firstName }}</p>
      <p class="card-text mb-2">Фамилия: {{ lastName }}</p>
    </div>
  </div>
</template>

<style scoped>
.card-footer{
  font-size: small;
  height: 35px;
}

.card-text{
  display: -webkit-box;
  -webkit-line-clamp: 6;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.card-body{
  padding: 9px;
  max-height: 255px;
}

.capsule-param{
  background-color: var(--color1);
  color: var(--color4);
  max-height: 460px;
}

.owner-link:hover{
  color: var(--color11)
}

</style>