<template>
<h2>Индивидуальные страховые соглашения</h2>
	<table class="table table-striped">
	  <thead class="thead-dark">
	    <tr>
	      <th scope="col">Работник</th>
	      <th scope="col">Агент</th>
	      <th scope="col">Начало</th>
	      <th scope="col">Конец</th>
          <th scope="col">Сумма</th>
          <th scope="col"></th>
	    </tr>
	  </thead>
	  <tbody>
	  	<tr v-for="item in items" :key="item.id">
        <td>{{ item.employee_str }}</td>
        <td>{{ item.agent_str }}</td>
        <td>{{ item.start_date }}</td>
        <td>{{ item.end_date }}</td>
        <td>{{ item.total_payout }}</td>
        <td><button @click="gotoClaim(item.id + '')" class="btn btn-secondary">Страховые случаи</button></td>
        <td><button @click="rmAgr(item.id + '')" class="btn btn-secondary">Удалить</button></td>
        <td><button @click="gotoEdit(item.id + '')" class="btn btn-secondary">Изменить</button></td>
      </tr>
  	</tbody>
	</table>
<div class="btn-group" role="group" aria-label="Basic outlined example">
  <button @click="gotoCollAgr()" class="btn btn-outline-secondary">К коллективным соглашениям</button>
  <button @click="gotoAgents()" class="btn btn-outline-secondary">К списку агентов</button>
  <button @click="gotoCompanies()" class="btn btn-outline-secondary">К списку компаний</button>
  <button @click="addAgr(item.id + '')" class="btn btn-outline-secondary">Добавить</button>
</div>
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
    axios.get('http://127.0.0.1:8000/ind-agr/')
      .then(response => {
        this.items = response.data;
      })
      .catch(error => {
        console.error(error);
      });
  },
  methods : {
    gotoClaim(itemid){
      this.$router.push({ path: '/individual-agreement/' + itemid});
    },
    gotoAgents(){
      this.$router.push({ path: '/agents/'});
    },
    gotoAgent(itemid){
      this.$router.push({ path: '/agent/' + itemid});
    },
    gotoCompanies(){
      this.$router.push({ path: '/companies/'});
    },
    gotoCollAgr(){
      this.$router.push({ path: '/collective/'});
    }
  }
}
</script>