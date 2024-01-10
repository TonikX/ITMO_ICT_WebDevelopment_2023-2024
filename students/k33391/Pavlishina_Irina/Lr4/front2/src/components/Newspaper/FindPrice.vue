<script setup>
import {ref} from "vue";
import instance from "@/AxiosInstance";
import router from "@/router/router";
import {TokenStore} from "@/stores/TokenStore";

const Token = TokenStore()

const error = ref(false)

const form = ref('')
const addresses = ref()

function create(){
  instance.post('/system/do/more-expensive-newspapers/', form.value, {
    headers: {
      'Authorization': `Bearer ${Token.token}`
    }
  }).then(response => {
        if (response.status === 200){
          addresses.value = response.data
        }
      }
  ).catch(e => error.value = true )
}

</script>

<template>
  <v-app>
    <div class="w-50 mx-auto">
      <h2>Найти по цене</h2>
      <v-text-field label="Цена" v-model="form"></v-text-field>
      <v-btn @click="create">Найти</v-btn>
    </div>
    <div v-if="error" class="text-red">
      Не найдено
    </div>
    <div v-else-if="addresses">
      <template v-for="printed in addresses" :key="printed">
        <v-card
            width="400"
            :title="printed.newspaper.name"
            :subtitle="`${printed.newspaper.redactor_last_name} ${printed.newspaper.redactor_first_name} ${printed.newspaper.redactor_patronic}`"
            :text="`Цена ${printed.newspaper.cost}`"
        >
          <v-card-actions>
            <v-btn>
              Отделение: {{ printed.post_office.num }}
            </v-btn>
          </v-card-actions>
        </v-card>
      </template>
    </div>
  </v-app>
</template>

<style scoped>

</style>
