<template>
  <div class="modal fade modal-my-config" id="loginFormModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="loginFormModal" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="staticBackdropLabel">Авторизация</h5>
          <button type="button" class="btn btn-my-main" data-bs-dismiss="modal" aria-label="Закрыть">
            <svg id="close" class="close-btn"  viewBox="0 0 16 16">
              <path fill-rule="evenodd" d="M8 2a.5.5 0 0 1 .5.5v5h5a.5.5 0 0 1 0 1h-5v5a.5.5 0 0 1-1 0v-5h-5a.5.5 0 0 1 0-1h5v-5A.5.5 0 0 1 8 2"/>
            </svg>
          </button>
        </div>
        <div class="modal-body">
          <form id="LogInForm" @submit.prevent="login">
            <div class="form-outline mb-4">
              <label class="form-label" for="LogInFormEmail">Имя пользователя</label>
              <input type="username" v-model="form.username" id="LogInFormEmail" class="form-control" name="username"/>
            </div>

            <div class="form-outline mb-4">
              <label class="form-label" for="LogInFormPassword">Пароль</label>
              <input type="password" v-model="form.password" id="LogInFormPassword" class="form-control" name="password"/>
            </div>
            <button type="submit" class="btn btn-my-main btn-block mb-3" id="LogInFormBTN" data-bs-dismiss="modal">Вход</button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import {mapActions, mapGetters, mapState} from "pinia";
import usersStore from "@/stores/user.js";

  export default {
    name: 'loginModal',
    data() {
      return {
        form: {
          username: '',
          password: '',
        },
        usState: usersStore(),
      };
    },
    computed: {
    },
    methods: {
      async login() {
        const resp = (await this.usState.loginUser(this.form));
        await this.formReset();
      },
      async formReset() {
        this.form.password = '';
        this.form.username = '';
      }
    },
  }
</script>

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