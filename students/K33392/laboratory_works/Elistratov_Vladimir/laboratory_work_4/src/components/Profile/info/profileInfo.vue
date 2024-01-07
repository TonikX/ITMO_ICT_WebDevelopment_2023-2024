<script>
  import {useDate} from "@/composables/date.js";
  import usersStore from "@/stores/user.js";
  export default {
    name: 'ProfileInfo',
    data() {
      return {
        form: {
          last_name: this.lastName,
          first_name: this.firstName,
        },
        usState: usersStore(),
      };
    },
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
      email: {
        type: String,
      },
      capCount: {
        type: Number,
      },
      dateJoined:{
        type: Date,
      },
    },
    methods:{
      getNormalDate(date){
        return useDate(date)
      },
    }
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
            <p class="fw-bold">Дата регистрации: <span class="fw-normal" > {{ getNormalDate(dateJoined) }}</span></p>
            <p class="fw-bold">Email: <span class="fw-normal" > {{ email }} </span></p>
            <p class="fw-bold">Кол-во созданных капсул: <span class="fw-normal" > {{ capCount }} </span></p>
          </div>
        </div>
        <div class="card-footer">
          <div class="justify-s-b">
            <button type="button" class="btn btn-sm btn-my-main" data-bs-toggle="modal" data-bs-target="#updateFormModal">
              Изменить данные
              <svg class="icons" id="redactIcon" viewBox="0 0 16 16">
                <path d="M12.146.146a.5.5 0 0 1 .708 0l3 3a.5.5 0 0 1 0 .708l-10 10a.5.5 0 0 1-.168.11l-5 2a.5.5 0 0 1-.65-.65l2-5a.5.5 0 0 1 .11-.168l10-10zM11.207 2.5 13.5 4.793 14.793 3.5 12.5 1.207 11.207 2.5zm1.586 3L10.5 3.207 4 9.707V10h.5a.5.5 0 0 1 .5.5v.5h.5a.5.5 0 0 1 .5.5v.5h.293l6.5-6.5zm-9.761 5.175-.106.106-1.528 3.821 3.821-1.528.106-.106A.5.5 0 0 1 5 12.5V12h-.5a.5.5 0 0 1-.5-.5V11h-.5a.5.5 0 0 1-.468-.325z"/>
              </svg>
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.card-footer{
  font-size: small;
  padding: 5px;
  background-color: var(--color3);
}

.card-header{
  padding: 10px;
  display: flex;
  align-items: center;
}

.card-body{
  padding: 9px;
}

.card{
  background-color: var(--color3);
  color: var(--color4);
}
</style>