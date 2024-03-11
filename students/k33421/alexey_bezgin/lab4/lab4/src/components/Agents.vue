<template>
<h2>Список агентов</h2>
<table class="table table-striped">
	<thead class="thead-dark">
	  <tr>
	    <th scope="col">Имя</th>
	    <th scope="col">Паспортные данные</th>
	    <th scope="col">Контактная информация</th>
	    <th scope="col">Операция</th>
	  </tr>
	</thead>
	<tbody>
		  	<tr v-for="item in items" :key="item.id">
	        <td>{{ item.full_name }}</td>
	        <td>{{ item.passport_data }}</td>
	        <td>{{ item.contact_details }}</td>
	        <td><button @click="rmAgent(item.id + '')" class="btn btn-secondary">Удалить</button></td>
	        <td><button @click="gotoEdit(item.id + '')" class="btn btn-secondary">Изменить</button></td>
	      </tr>
	  	</tbody>
</table>
<div class="btn-group" role="group" aria-label="Basic outlined example">
	<button onclick="history.back()" class="btn btn-outline-secondary">Назад</button>
	<button @click="addAgent()" class="btn btn-outline-secondary">Добавить</button>
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
    axios.get('http://127.0.0.1:8000/agents/')
      .then(response => {
        this.items = response.data;
      })
      .catch(error => {
        console.error(error);
      });
  },
  methods : {
    gotoEdit(itemid){
      this.$router.push({ path: '/agent/' + itemid});
    },
    rmAgent(itemid){
    	axios.post('http://127.0.0.1:8000/agent-trigger/delete', {id : itemid});
    	location.reload();
    },
    addAgent() {
    	this.$router.push({ path: '/agent/create'});
    }
  }
}
</script>