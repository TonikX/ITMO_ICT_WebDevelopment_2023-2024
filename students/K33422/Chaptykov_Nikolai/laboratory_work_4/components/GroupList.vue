<template>
    <h1>Группы</h1>
    <button @click="gotoTutors()" class="btn btn-dark">Cписок преподавателей</button>
    <table class="table table-dark">
        <thead slot="head">
            <th>Код группы</th>
            <th>Факультет</th>
    </thead>
        <tbody slot="body" slot-scope="{displayData}">
            <tr v-for="item in items" :key="item.id">
                <td><button @click="showGroup(item.id + '')" class="btn btn-secondary">{{ item.group_name }}</button></td>
                <td>{{ item.faculty }}</td>
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
    axios.get('http://127.0.0.1:8000/group_js/')
      .then(response => {
        this.items = response.data;
      })
      .catch(error => {
        console.error(error);
      });
  },
  methods : {
    showGroup(item) {
      this.$router.push({ path: item});
      },
    gotoTutors() {
      this.$router.push({ path: '/tutor/'});
    }

  }
}
</script>