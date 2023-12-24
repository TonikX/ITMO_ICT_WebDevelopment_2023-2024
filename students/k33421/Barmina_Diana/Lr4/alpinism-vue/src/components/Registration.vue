<template>
  <form @submit.prevent="hundleSubmit">
    <h3>Зарегистрироваться</h3>

    <div class="from-group">
      <label>Имя</label>
      <input type="text" class="form-control" v-model="first_name" placeholder="Имя"/>
    </div>

    <div class="from-group">
      <label>Фамилия</label>
      <input type="text" class="form-control" v-model="last_name" placeholder="Фамилия"/>
    </div>

    <div class="from-group">
      <label>Номер телефона</label>
      <input type="text" class="form-control" v-model="phone_number" placeholder="Номер телефона"/>
    </div>

    <div class="from-group">
      <label>Электронная почта</label>
      <input type="email" class="form-control" v-model="email" placeholder="Почта"/>
    </div>

    <div class="from-group">
      <label>Паспорт</label>
      <input type="text" class="form-control" v-model="document" placeholder="СерияНомер"/>
    </div>

    <div class="from-group">
      <label>Дата рождения</label>
      <input type="date" class="form-control" v-model="birth_date"/>
    </div>

    <div class="from-group">
      <label>Адрес</label>
      <input type="text" class="form-control" v-model="address" placeholder="Адрес"/>
    </div>

    <div class="from-group">
      <label>Уровень подготовки</label>
      <select v-model="experience_level">
        <option value="Новичок">Новичок</option>
        <option value="Продвинутый">Продвинутый</option>
        <option value="Профи">Профи</option>
      </select>
    </div>

    <div class="from-group">
      <label>Имя аккаунта</label>
      <input type="text" class="form-control" v-model="username" placeholder="Имя аккаунта"/>
    </div>

    <div class="from-group">
      <label>Пароль</label>
      <input type="password" class="form-control" v-model="password" placeholder="Пароль"/>
    </div>

    <div class="from-group">
      <label>Подтверждение пароля</label>
      <input type="password" class="form-control" v-model="password_confirm" placeholder="Пароль"/>
    </div>

    <button>Зарегистрироваться</button>
  </form>
</template>

<script>
import axios from "axios";
export default {
  name: "Registration",
  data() {
    return {
      first_name: '',
      last_name: '',
      phone_number: '',
      email: '',
      document: '',
      birth_date: '',
      address: '',
      experience_level: '',
      username: '',
      password: '',
      password_confirm: '',
    }
  },
  methods: {
    async hundleSubmit() {

      const response = await axios.post('http://localhost:8000/alp/auth/users/', {
        first_name: this.first_name,
        last_name: this.last_name,
        phone_number: this.phone_number,
        email: this.email,
        document: this.document,
        birth_date: this.birth_date,
        address: this.address,
        experience_level: this.experience_level,
        username: this.username,
        password: this.password,
        password_confirm: this.password_confirm,
      });
      console.log(response);
      await this.$router.push({name: 'Login'});
    }
  },
}
</script>

<style scoped>

</style>
