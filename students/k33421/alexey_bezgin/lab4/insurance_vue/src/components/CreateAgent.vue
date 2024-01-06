<template>
	<input
          class="form-control"
          type="text"
          v-model="id"
          name="логин"
          :placeholder="items[0].id"
        />
	<input
          class="form-control"
          type="text"
          v-model="full_name"
          name="логин"
          :placeholder="items[0].full_name"
        />
    <input
          class="form-control"
          type="text"
          v-model="passport_data"
          text="логин"
          :placeholder="items[0].passport_data"
        />
    <input
          class="form-control"
          type="text"
          v-model="contact_details"
          name="логин"
          :placeholder="items[0].contact_details"
        />
<button onclick="history.back()" class="btn btn-outline-secondary">Назад</button>
<button @click="sendData()" class="btn btn-outline-secondary">Отправить</button>
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
	axios.get('http://127.0.0.1:8000/agent/' + firstSegment)
	  .then(response => {
	    this.items = response.data;
	  })
	  .catch(error => {
	    console.error(error);
	  });
  },
  methods : {
  	sendData() {
	axios.post('http://127.0.0.1:8000/agent-trigger/create', {
		id: this.id,
		full_name: this.full_name,
		passport_data: this.passport_data,
		contact_details: this.contact_details
	});
  	}
  }
}
</script>