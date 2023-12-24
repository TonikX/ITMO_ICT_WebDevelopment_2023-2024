<template>
    <h1>Преподаватели</h1>
    <button @click="gotoGroup()" class="btn btn-dark">Cписок групп</button>
    <table class="table table-dark">
        <thead slot="head">
            <th>Фамилия</th>
            <th>Имя</th>
    </thead>
        <tbody slot="body" slot-scope="{displayData}">
            <tr v-for="item in items" :key="item.id">
                <td>{{ item.surname }}</td>
                <td>{{ item.name }}</td>
            </tr>
        </tbody>
    </table>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      items: []
    };
  },
  created() {
    axios.get('http://127.0.0.1:8000/tutor_js/')
      .then(response => {
        this.items = response.data;
      })
      .catch(error => {
        console.error(error);
      });
  },
  methods : {
    showTutor(item) {
        this.$router.push({ path: item});
      },
    gotoGroup() {
        this.$router.push({ path: '/group/'});
    }

  }
}
</script>