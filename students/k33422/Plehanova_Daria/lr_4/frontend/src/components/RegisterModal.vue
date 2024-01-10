<template>
  <v-dialog v-model="dialog" max-width="500px">
    <v-card>
      <v-card-title class="headline">Регистрация</v-card-title>
      <v-card-text>
        <v-form>
          <v-text-field label="Email" v-model="email" required></v-text-field>
          <v-text-field label="Пароль" v-model="password" type="password" required></v-text-field>
        </v-form>
      </v-card-text>
      <v-card-actions>
        <v-btn text color="red" @click="dialog = false">Отмена</v-btn>
        <v-spacer></v-spacer>
        <v-btn color="primary" text @click="register">Зарегистрироваться</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
  <v-snackbar v-model="snackbar.show">
    {{ snackbar.text }}
    <v-btn color="red" text @click="snackbar.show = false">Закрыть</v-btn>
  </v-snackbar>
</template>

<script>
export default {
  data() {
    return {
      dialog: false,
      email: '',
      password: '',
      snackbar: {
        show: false,
        text: ''
      }
    };
  },
  computed: {
    authError() {
      return this.$store.state.authError;
    },
    authStatus() {
      return this.$store.state.authStatus;
    }
  },
  methods: {
    async register() {
      await this.$store.dispatch('register', {email: this.email, password: this.password});
      if (this.authStatus === 'success') {
        this.snackbar.text = 'Success registration!';
        this.snackbar.show = true;
        this.dialog = false;
      } else {
        this.snackbar.text = this.authError;
        this.snackbar.show = true;
      }
    }
  }
};
</script>
