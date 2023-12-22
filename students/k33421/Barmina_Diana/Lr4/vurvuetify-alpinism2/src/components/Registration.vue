<template>

  <v-row justify="center" >
    <v-col
      cols="12"
      sm="10"
      md="8"
      lg="6"
      align="center"
    >
      <v-card ref="form" title="Форма регистрации" max-width="500px" color="amber-lighten-3" style="top: 20%" >
        <v-card-text>
          <v-text-field
            label="Имя"
            class="form-control"
            v-model="first_name"
            type="text"
            placeholder="Имя"
            variant="outlined"
            required
          >
          </v-text-field>
          <v-text-field
            label="Фамилия"
            class="form-control"
            v-model="last_name"
            type="text"
            placeholder="Фамилия"
            variant="outlined"
            required
          ></v-text-field>
          <v-text-field
            label="Номер телефона"
            class="form-control"
            v-model="phone_number"
            type="text"
            placeholder="Номер телефона"
            variant="outlined"
            required
          ></v-text-field>
          <v-text-field
            v-model="email"
            label="Почта"
            class="form-control"
            type="email"
            placeholder="email"
            variant="outlined"
            required
          ></v-text-field>
          <v-text-field
            v-model="document"
            label="Паспорт"
            class="form-control"
            type="text"
            placeholder="Номер Серия"
            variant="outlined"
            required
          ></v-text-field>
          <v-text-field
            v-model="birth_date"
            label="Дата рождения"
            class="form-control"
            type="date"
            placeholder="birth date"
            variant="outlined"
            required
          ></v-text-field>
          <v-text-field
            v-model="address"
            label="Адрес"
            class="form-control"
            type="text"
            placeholder="Адрес"
            variant="outlined"
            required
          ></v-text-field>
          <v-select
            v-model="experience_level"
            label="Уровень подготовки"
            :items="levels"
            item-title="definition"
            variant="outlined">
            <template v-slot:item="{ props, item }">
              <v-list-item v-bind="props" :subtitle="item.raw.name"></v-list-item>
            </template>
          </v-select>
          <v-text-field
            v-model="username"
            label="Username"
            class="form-control"
            type="text"
            placeholder="Username"
            variant="outlined"
            required
          ></v-text-field>
          <v-text-field
            v-model="password"
            label="Пароль"
            class="form-control"
            type="password"
            placeholder="Пароль"
            variant="outlined"
            required
          ></v-text-field>
          <v-text-field
            v-model="password_confirm"
            label="Повторите пароль"
            class="form-control"
            type="password"
            placeholder="Пароль"
            variant="outlined"
            required
          ></v-text-field>

        </v-card-text>
        <v-divider class="mt-12"></v-divider>
        <v-card-actions>
          <v-btn
            color="white"
            variant="text"
            @click="$router.push(`/`)">
            Назад
          </v-btn>
          <v-spacer></v-spacer>
          <v-btn
            variant="text"
            @click="hundleSubmit"
          >
            Создать
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-col>
  </v-row>

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
      levels2: ['Новичок', 'Продвинутый', 'Профи'],
      levels: [
        {
          name: 'Новичок1',
          definition: 'Новичок',
        },
        {
          name: 'Продвинутый2',
          definition: 'Продвинутый',
        },
        {
          name: 'Профи3',
          definition: 'Профи',
        }
      ]
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
