<template>
	<select class="custom-select mr-sm-2" id="inlineFormCustomSelect">
        <option selected>Choose...</option>
        <option value="1">One</option>
        <option value="2">Two</option>
        <option value="3">Three</option>
      </select>
	<select class="custom-select mr-sm-2" id="inlineFormCustomSelect">
        <option selected>Choose...</option>
        <option value="1">One</option>
        <option value="2">Two</option>
        <option value="3">Three</option>
      </select>
	<div>
    <date-picker v-model:value="time0"></date-picker>
    <date-picker v-model:value="time1" type="datetime"></date-picker>
    <date-picker v-model:value="time2" valueType="format"></date-picker>
    <date-picker v-model:value="time3" range></date-picker>
  </div>
    <input
          class="form-control"
          type="text"
          v-model="short_name"
          text="логин"
          :placeholder="items[0].short_name"
        />
    <input
          class="form-control"
          type="text"
          v-model="address"
          name="логин"
          :placeholder="items[0].address"
        />
    <input
          class="form-control"
          type="text"
          v-model="bank_details"
          name="логин"
          :placeholder="items[0].bank_details"
        />
    <input
          class="form-control"
          type="text"
          v-model="specialization"
          name="логин"
          :placeholder="items[0].specialization"
        />
<button onclick="history.back()" class="btn btn-outline-secondary">Назад</button>
<button @click="sendData()" class="btn btn-outline-secondary">Отправить</button>
</template>

<script>
import DatePicker from 'vue-datepicker-next';
import 'vue-datepicker-next/index.css';
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
	axios.get('http://127.0.0.1:8000/company/' + firstSegment)
	  .then(response => {
	    this.items = response.data;
	  })
	  .catch(error => {
	    console.error(error);
	  });
  },
  methods : {
  	sendData() {
	axios.post('http://127.0.0.1:8000/company-trigger/create', {
		id: this.id,
		code: this.code,
		full_name: this.full_name,
		short_name: this.short_name,
		address: this.address,
		bank_details: this.bank_details,
		specialization: this.specialization
	});
  	}
  }
}
</script>