<template>
	<h1>Состав группы</h1>
	<button @click="gotoGroup()" class="btn btn-dark">Обратно к списку групп</button>
	    <table class="table table-dark">
	        <thead slot="head">
	            <th>Имя</th>
	            <th>Фамилия</th>
		    </thead>
			<tbody slot="body" slot-scope="{displayData}">
	            <tr v-for="item in items" :key="item.id">
	                <td>{{ item.name }}</td>
	                <td>{{ item.surname }}</td>
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
  	const str = window.location.href
  	const firstSegment = (new URL(str)).pathname.split('/')[2];
    axios.get('http://127.0.0.1:8000/group_js/' + firstSegment)
      .then(response => {
        this.items = response.data;
      })
      .catch(error => {
        console.error(error);
      });
  },
  methods : {
	  gotoGroup() {
	        this.$router.push({ path: '/group/'});
	    }
  }
  }
</script>