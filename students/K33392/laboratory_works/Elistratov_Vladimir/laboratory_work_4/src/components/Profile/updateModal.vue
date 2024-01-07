<template>
  <div class="modal fade modal-my-config" id="updateFormModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="regFormModal" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="staticBackdropLabel">Обновление профиля</h5>
          <button type="button" class="btn btn-my-main" data-bs-dismiss="modal" aria-label="Закрыть">
            <svg id="close" class="close-btn"  viewBox="0 0 16 16">
              <path fill-rule="evenodd" d="M8 2a.5.5 0 0 1 .5.5v5h5a.5.5 0 0 1 0 1h-5v5a.5.5 0 0 1-1 0v-5h-5a.5.5 0 0 1 0-1h5v-5A.5.5 0 0 1 8 2"/>
            </svg>
          </button>
        </div>
        <div class="modal-body">
          <form id="RegistrationForm" @submit.prevent="update">

            <div class="form-outline mb-4">
              <label class="form-label" for="registerName">Имя</label>
              <input type="text" v-model="form.first_name" id="registerName" class="form-control" name="firstName"/>
            </div>

            <div class="form-outline mb-4">
              <label class="form-label" for="registerName">Фамилия</label>
              <input type="text" v-model="form.last_name" id="registerName2" class="form-control" name="lastName"/>
            </div>

            <button type="submit" class="btn btn-my-main btn-block mb-3" data-bs-dismiss="modal">Сохранить изменения</button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import usersStore from "@/stores/user.js";

  export default {
    name: 'ProfileUpdateModal',
    data() {
      return {
        usState: usersStore(),
        form: {
          first_name: "",
          last_name: "",
        },
      };
    },
    computed: {
    },
    methods: {
      async update() {
        const resp = await this.usState.updateUser(this.form)
        await this.formReset();
        location.reload()
      },
      async formReset() {
        this.form.first_name = this.usState.user['first_name']
        this.form.last_name = this.usState.user['last_name']
      }
    },
    mounted() {
      this.form.first_name = this.usState.user['first_name']
      this.form.last_name = this.usState.user['last_name']
    }
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