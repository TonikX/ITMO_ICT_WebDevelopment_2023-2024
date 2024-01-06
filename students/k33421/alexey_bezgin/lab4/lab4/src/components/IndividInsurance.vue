<template>

<div class="card" style="width: 18rem;">
  <div class="card-header">
    Страховой случай
  </div>
  <ul class="list-group list-group-flush">
  	<tr v-for="item in items" :key="item.id">
  		<li class="list-group-item"><strong>Идентификатор соглашения:</strong> {{ item.employee }}</li>
  		<li class="list-group-item"><strong>Время случая:</strong> {{ item.date_of_claim }}</li>
  		<li class="list-group-item"><strong>Причина:</strong> {{ item.cause }}</li>
  		<li class="list-group-item"><strong>Решение:</strong> {{ item.decision }}</li>
  		<li class="list-group-item"><strong>Сумма выплат:</strong> {{ item.payout_amount }}</li>
  	</tr>
  </ul>
</div>
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
    axios.get('http://127.0.0.1:8000/ind-ins/' + firstSegment)
      .then(response => {
        this.items = response.data;
      })
      .catch(error => {
        console.error(error);
      });
  }
}
</script>