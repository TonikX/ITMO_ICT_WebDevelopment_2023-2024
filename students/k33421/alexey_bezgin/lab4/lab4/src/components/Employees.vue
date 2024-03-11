<template>
<h2>Сотрудники</h2>
	<table class="table table-striped">
	<thead class="thead-dark">
	  <tr>
	    <th scope="col">Имя</th>
	    <th scope="col">Возраст</th>
	    <th scope="col">Категория риска</th>
	    <th scope="col">Идентификатор компании</th>
	  </tr>
	</thead>
	<tbody>
		  	<tr v-for="item in items" :key="item.id">
	        <td>{{ item.full_name }}</td>
	        <td>{{ item.age }}</td>
	        <td>{{ item.risk_category }}</td>
	        <td>{{ item.company }}</td>
	      </tr>
	  	</tbody>
</table>
<button onclick="history.back()" class="btn btn-outline-secondary">Назад</button>
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
  	const str = window.location.href
  	const firstSegment = (new URL(str)).pathname.split('/')[2];
    axios.get('http://127.0.0.1:8000/empl/' + firstSegment)
      .then(response => {
        this.items = response.data;
      })
      .catch(error => {
        console.error(error);
      });
  }
}
</script>