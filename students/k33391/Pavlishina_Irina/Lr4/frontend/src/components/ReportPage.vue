<script setup>
import {ref} from "vue";
import instance from "@/AxiosInstance";
import router from "@/router/router";
import {TokenStore} from "@/stores/TokenStore";

const Token = TokenStore()

const error = ref(false)

const form = ref({
  id: ""
})

const printer = ref(null)

function find(id) {
  instance.get(`/system/do/${form.value.id}/report/`).then(response => {
        if (response.status === 200) {
          printer.value = response.data
        }
      }
  ).catch(e => error.value = true)
}

</script>

<template>
  <v-app>
    <h2 class="w-50 mx-auto">Отчет</h2>
    <div class="w-50 mx-auto d-flex">
      <v-text-field label="Типография" v-model="form.id"></v-text-field>
      <v-btn @click="find">Найти</v-btn>
    </div>
    <div v-if="error" class="w-50 mx-auto">
      Данные не найдены
    </div>
    <div v-else-if="printer" class="w-50 mx-auto d-flex flex-column ga-4">
      <v-card
          class=""
          width="400"
      >
        <template v-slot:title>
          Самый продаваемый редактор
        </template>

        <v-card-text>
          {{ printer["most-sold-redactor"].redactor_last_name + ' ' + printer["most-sold-redactor"].redactor_first_name + ' ' + printer["most-sold-redactor"].redactor_patronic }}
        </v-card-text>
      </v-card>
      <v-card
          class=""
          width="400"
      >
        <template v-slot:title>
          Печатаются
        </template>

        <v-card-text>
          {{ printer.printed_here }}
        </v-card-text>
      </v-card>
      <h2>Что печатается</h2>
      <template v-for="printed in printer.show_printed" :key="printed.id">
        <v-card
            width="400"
            :title="printed.newspaper.name"
            :subtitle="`${printed.newspaper.redactor_last_name} ${printed.newspaper.redactor_first_name} ${printed.newspaper.redactor_patronic}`"
            :text="`Цена ${printed.newspaper.cost}`"
        >
          <v-card-actions>
            <v-btn>
              Количество: {{ printed.how_many_to_print }}
            </v-btn>
          </v-card-actions>
        </v-card>
      </template>
<!--      <h2>Где отправляются</h2>
      <template v-for="printed in printer['where-to-sell']" :key="printed?.id">
        <v-card
            width="400"
            :title="`Отделение: ${printed?.post_office?.num}`"
            :subtitle="`Газета: ${printed?.newspaper?.name}`"
            :text="`Необходимо: ${printed?.how_many_needed}`"
        >
        </v-card>
      </template>-->
    </div>
  </v-app>
</template>

<style scoped>

</style>
