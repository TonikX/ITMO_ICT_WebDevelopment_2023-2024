<template>
<h2>Компании</h2>
<table class="table table-striped">
	<thead class="thead-dark">
	  <tr>
	    <th scope="col">Код</th>
	    <th scope="col">Полное название</th>
	    <th scope="col">Сокращение</th>
	    <th scope="col">Адрес</th>
	    <th scope="col">Банковский счет</th>
	    <th scope="col">Сфера</th>
	  </tr>
	</thead>
	<tbody>
		  	<tr v-for="item in items" :key="item.id">
	        <td>{{ item.code }}</td>
	        <td>{{ item.full_name }}</td>
	        <td>{{ item.short_name }}</td>
	        <td>{{ item.address }}</td>
	        <td>{{ item.bank_details }}</td>
	        <td>{{ item.specialization }}</td>
	        <td><button @click="gotoAgent(item.id + '')" class="btn btn-secondary">Список сотрудников</button></td>
	        <td><button @click="rmComp(item.id + '')" class="btn btn-secondary">Удалить</button></td>
	        <td><button @click="editComp(item.id + '')" class="btn btn-secondary">Изменить</button></td>
	      </tr>
	  	</tbody>
</table>
<div class="btn-group" role="group" aria-label="Basic outlined example">
	<button onclick="history.back()" class="btn btn-outline-secondary">Назад</button>
	<button @click="addComp()" class="btn btn-outline-secondary">Добавить</button>
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
    axios.get('http://127.0.0.1:8000/companies/')
      .then(response => {
        this.items = response.data;
      })
      .catch(error => {
        console.error(error);
      });
  },
  methods : {
  	gotoAgent(itemid) {
  		this.$router.push({ path: '/company-employees/' + itemid});
  	},
	rmComp(itemid) {
		axios.post('http://127.0.0.1:8000/company-trigger/delete', {id: itemid});
		location.reload();
	},
	editComp(itemid) {
		this.$router.push({ path: '/company/' + itemid});
	},
	addComp() {
		this.$router.push({ path: '/company/create/'});
	},
  }
}
</script>