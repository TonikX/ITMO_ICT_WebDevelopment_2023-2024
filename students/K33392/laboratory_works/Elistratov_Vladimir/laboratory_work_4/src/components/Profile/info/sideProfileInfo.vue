<script>
  import {useDate} from "@/composables/date.js";
  import usersStore from "@/stores/user.js";
  export default {
    name: 'SideProfileInfo',
    props: {
      userName: {
        type: String,
      },
      firstName: {
        type: String,
      },
      lastName: {
        type: String,
      },
      capCount: {
        type: Number,
      },
    },
  }
</script>

<template>
  <div class="card col-12" id="profileCard">
    <div class="row">
      <div class="col-xl-2 col-md-4 col-sm-4">
        <img src="/src/assets/img/profile.jpg" class="img-fluid rounded-start">
      </div>
      <div class="col-xl-10 col-md-8 col-sm-8">
        <div class="card-body">
          <h5 class="card-title me-2 mt-2 text-end">{{ userName }}</h5>
          <div class="card-text text-start">
            <p class="fw-bold">Имя: <span class="fw-normal" > {{ firstName }} </span></p>
            <p class="fw-bold">Фамилия: <span class="fw-normal" > {{lastName}} </span></p>
            <p class="fw-bold">Кол-во созданных капсул: <span class="fw-normal" > {{ capCount }} </span></p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>

.card-body{
  padding: 9px;
}

.card{
  background-color: var(--color3);
  color: var(--color4);
}
</style>