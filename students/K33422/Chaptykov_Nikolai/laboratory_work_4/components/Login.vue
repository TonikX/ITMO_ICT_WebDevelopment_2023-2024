<template>
<section class="vh-100 gradient-custom">
  <div class="container py-5 h-100">
    <div class="row d-flex justify-content-center align-items-center h-100">
      <div class="col-12 col-md-8 col-lg-6 col-xl-5">
        <div class="card bg-dark text-white" style="border-radius: 1rem;">
          <div class="card-body p-5 text-center">

            <div class="mb-md-5 mt-md-4 pb-5">

              <h2 class="fw-bold mb-2 text-uppercase">Войти</h2>
              <p class="text-white-50 mb-5">Введите логин и пароль</p>
              <form @submit.prevent="signin">
              <div class="form-outline form-white mb-4">
                <input type="text" v-model="username" class="form-control form-control-lg" />
                <label class="form-label" for="text">Логин</label>
              </div>

              <div class="form-outline form-white mb-4">
                <input type="password" v-model="password" class="form-control form-control-lg" />
                <label class="form-label" for="text">Пароль</label>
              </div>

              <button class="btn btn-outline-light btn-lg px-5" type="submit">Войти</button>
              </form>

              <div class="d-flex justify-content-center text-center mt-4 pt-1">
                <a href="#!" class="text-white"><i class="fab fa-facebook-f fa-lg"></i></a>
                <a href="#!" class="text-white"><i class="fab fa-twitter fa-lg mx-4 px-2"></i></a>
                <a href="#!" class="text-white"><i class="fab fa-google fa-lg"></i></a>
              </div>

            </div>

            <div>
              <p class="mb-0">Нет аккаунта? <a href="register" class="text-white-50 fw-bold">Зарегистрироваться</a>
              </p>
            </div>

          </div>
        </div>
      </div>
    </div>
  </div>
</section>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      username: '',
      password: ''
    }
  },
  methods: {
    signin() {
      axios.post('http://127.0.0.1:8000/login_js/', {
        username: this.username,
        password: this.password
      })
      .then(response => {
        console.log(response.data);
        if(response.status==200){this.$router.push({ path: '/group/'});}
      });
    },
    gotoSignUp() {
        this.$router.push({ path: '/register'});
    }
  }
}
</script>

<style>
#app {
  font-family: Arial, sans-serif;
  text-align: center;
}

h1 {
  margin-bottom: 20px;
}

input {
  margin-bottom: 10px;
}

button {
  margin-top: 10px;
}
</style>