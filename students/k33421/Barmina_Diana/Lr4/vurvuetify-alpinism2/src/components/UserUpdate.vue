<template>
  <v-sheet>
    <v-dialog width="600">
      <template v-slot:activator="{ props }">
        <v-btn icon v-bind="props" color="grey">
          <v-icon>mdi-pencil</v-icon>
        </v-btn>
      </template>

      <template v-slot:default="{ isActive }">
        <v-card
          title="Изменить данные профиля">
          <template v-slot:append>
            <v-btn icon="$close" variant="text" @click="isActive.value = false"></v-btn>
          </template>

          <v-divider></v-divider><br>
          <v-form>
            <v-text-field
              v-model="new_user.last_name"
              label="Фамилия"
              variant="outlined"
              width="300px">
            </v-text-field>
            <v-text-field
              v-model="new_user.first_name"
              label="Имя"
              variant="outlined">
            </v-text-field>
            <v-text-field
              v-model="new_user.email"
              label="Email"
              variant="outlined">
            </v-text-field>
            <v-text-field
              v-model="new_user.phone_number"
              label="Номер телефона"
              variant="outlined">
            </v-text-field>
            <v-text-field
              v-model="new_user.address"
              label="Адрес"
              variant="outlined">
            </v-text-field>
            <v-text-field
              v-model="new_user.document"
              label="Паспорт"
              variant="outlined">
            </v-text-field>
            <v-select
              v-model="new_user.experience_level"
              label="Уровень подготовки"
              :items="levels"
              item-title="definition"
              variant="outlined">
              <template v-slot:item="{ props, item }">
                <v-list-item v-bind="props" :subtitle="item.raw.name"></v-list-item>
              </template>
            </v-select>
            <div class="py-4 pr-7 text-right">
              <v-btn @click="saveChanges" color="green" variant="tonal">Сохранить</v-btn>
            </div>
          </v-form>
        </v-card>
      </template>
    </v-dialog>
  </v-sheet>
</template>

<script>
import axios from 'axios';
export default {
  props: {
    user: Object,
  },
  data() {
    return {
      new_user: { ...this.user },
      first_name: '',
      last_name: '',
      phone_number: '',
      email: '',
      document: '',
      address: '',
      experience_level: '',
      levels: [
        {
          name: 'Новичок',
          definition: 'Новичок',
        },
        {
          name: 'Продвинутый',
          definition: 'Продвинутый',
        },
        {
          name: 'Профи',
          definition: 'Профи',
        }
      ]
    };
  },
  methods: {
    async saveChanges() {
      const response = await axios.patch(`http://localhost:8000/alp/auth/users/me/`,
        {
          first_name: this.new_user.first_name,
          last_name: this.new_user.last_name,
          phone_number: this.new_user.phone_number,
          email: this.new_user.email,
          document: this.new_user.document,
          birth_date: this.new_user.birth_date,
          address: this.new_user.address,
          experience_level: this.new_user.experience_level,
          username: this.new_user.username,
          id: this.new_user.id,
          //password: this.user.password,
          //password_confirm: this.user.password_confirm,
        },
        {headers: {Authorization: 'Token ' + sessionStorage.getItem('token')}}
      ).then(() => {
        // Обновление данных прошло успешно
        location.reload(); // перезагрузить страницу
      })

      //console.log('User data updated successfully:', response.data)
      //this.$emit('changes-saved', response.data);
    },
  },
};
</script>
