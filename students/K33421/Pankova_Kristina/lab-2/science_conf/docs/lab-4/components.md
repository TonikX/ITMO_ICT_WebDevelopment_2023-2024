# Vue.js Components

This documentation provides an overview of the Vue.js components used in the app.

## Appointment Components

### AppointmentEditForm.vue

Description: Component for editing appointments.

```vue
<template>
  <div>
    <form @submit.prevent="submitForm">
      <div >
        <label for="salon">Salon:</label>
        <select v-model="editedAppointment.salon" id="salon">
          <option v-for="salon in salons" :value="salon.id">{{ salon.name }}</option>
        </select>
      </div>
      <div>
        <label for="customer">Customer:</label>
        <select v-model="editedAppointment.customer" id="customer">
          <option v-for="customer in customers" :value="customer.id">{{ customer.username }}</option>
        </select>
      </div>
      <div>
        <label for="service">Service:</label>
        <select v-model="editedAppointment.service" id="service">
          <option v-for="service in services" :value="service.id">{{ service.name }}</option>
        </select>
      </div>
      <div>
        <label for="datetime">Date and Time:</label>
        <input type="datetime-local" v-model="editedAppointment.datetime" id="datetime">
      </div>
      <button type="submit">Save</button>
      <button v-on:click="cancelEdit">Cancel</button>
    </form>
  </div>
</template>


<style scoped>
button {
  background-color: #04AA6D; /* Green */
  border: none;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
}

select {
  border: 2px solid grey;
}
input {
  border: 2px solid grey;
}
</style>


<script>
import moment from "moment";
import axios from "axios";

export default {
  props: ["appointment"],
  data() {
    return {
      editedAppointment: { ...this.appointment },
      salons: [],
      customers: [],
      services: [],
    };
  },
  created() {
    this.fetchSalons();
    this.fetchCustomers();
    this.fetchServices();
  },
  methods: {
    fetchSalons() {
      fetch("http://127.0.0.1:8000/salon/salons/")
        .then((response) => response.json())
        .then((data) => {
          this.salons = data;
        });
    },
    fetchCustomers() {
      fetch("http://127.0.0.1:8000/salon/customers/")
        .then((response) => response.json())
        .then((data) => {
          this.customers = data;
        });
    },
    fetchServices() {
      fetch("http://127.0.0.1:8000/salon/services/")
        .then((response) => response.json())
        .then((data) => {
          this.services = data;
        });
    },
    submitForm() {
      const formattedDate = moment(this.editedAppointment.datetime).format(
        "YYYY-MM-DD"
      );
      this.editedAppointment.datetime = formattedDate;
      console.log(this.editedAppointment);
      axios
        .put(
          `http://127.0.0.1:8000/salon/appointments/${this.editedAppointment.id}/edit/`,
          this.editedAppointment
        )
        .then((response) => {
          // Handle successful form submission
          console.log(response.data);
        })
        .catch((error) => {
          // Handle form submission error
          console.error(error);
        });
    },
    cancelEdit() {
      this.$emit("cancel-edit");
    },
  },
};
</script>

```

### AppointmentList.vue

Description: Component for displaying a list of appointments.

```vue
<template>
  <div class="salon-appointment">
    <div v-for="appointment in appointments" :key="appointment.id">
      <div><strong>Customer:</strong> {{ appointment.customer }} </div>
      <div><strong>Service:</strong> {{ appointment.service }}</div>
      <div><strong>Datetime:</strong> {{ appointment.datetime }}</div>
      <v-btn v-on:click="editAppointment(appointment)">Edit</v-btn>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  props: {
    salonId: {
      type: Number,
      required: true
    }
  },
  data() {
    return {
      appointments: []
    };
  },
  methods: {
    async fetchSalonAppointments() {
      const url = 'http://127.0.0.1:8000/salon/appointments/';
      try {
        const response = await axios.get(url);
        const appointments = response.data;

        for (const appointment of appointments) {
          const customerResponse = await axios.get(`http://127.0.0.1:8000/salon/customers/${appointment.customer}`);
          appointment.customer = customerResponse.data.username;
          const serviceResponse = await axios.get(`http://127.0.0.1:8000/salon/services/${appointment.service}`);
          appointment.service = serviceResponse.data.name;
        }
        this.appointments = appointments;
      } catch (error) {
        console.error(error);
        alert("Error fetching salon appointments");
      }
    },
    editAppointment(appointment) {
      this.$emit("edit-appointment", appointment);
    },
  },
  mounted() {
    this.fetchSalonAppointments();
  }
};
</script>

<style>
.salon-appointment {
  padding: 20px;
  margin: 10px;
  margin-top: 20px;
  border: 1px solid gray;
  padding: 8px;
  text-align: center;
  text-transform: uppercase;
  color: #4CAF50;
}
</style>

```


## Registration Components

### RegisterService.vue

Description: Component for registering a service.

```vue
<template>
  <form @submit.prevent="submitForm">
    <!-- Other form fields -->
    <div>
      <label for="salon">Salon:</label>
      <select id="salon" v-model="salon" required>
        <option v-for="salon in salons" :value="salon.id">{{ salon.name }}</option>
      </select>
      <br />
            <label for="name">Customer:</label>
      <input type="text" id="customer" v-model="salon.customer" required>
    </div>
    <div>
      <label for="type">Type:</label>
      <input type="text" id="type" v-model="salon.type" required>
    </div>
    <div>
      <label for="city">City:</label>
      <input type="text" id="city" v-model="salon.city">
    </div>
    <div>
      <label for="description">Description:</label>
      <input type="text" id="description" v-model="salon.description">
      <input type="hidden" id="date_registered" v-model="salon.date_registered" />

    </div>
    <button type="submit">Submit</button>
  </form>
</template>
<style scoped>
.button["submit"] {
  background-color: #04AA6D; /* Green */
  border: none;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
}

select {
  border: 2px solid grey;
}
input {
  border: 2px solid grey;
}

div {
  border-radius: 5px;
  background-color: #f2f2f2;
  padding: 20px;
}
</style>

<script>
import axios from 'axios';
import moment from 'moment';

export default {
  data() {
    return {
      salon: {
        name: '',
        type: '',
        city: '',
        description: '',
        owner: null,  // Initialize owner as null
        date_registered: moment(new Date().toISOString()).format('YYYY-MM-DD')  // Initialize date_registered with current time
      },
      owners: []  // Array to store the list of owners
    };
  },
  computed: {
    formattedDate() {
      return moment(this.salon.date_registered).format('YYYY-MM-DD');
    }
  },
  created() {
    // Fetch the list of owners from the Django backend when the component is created
    axios.get('http://127.0.0.1:8000/salon/owners/')
      .then(response => {
        this.owners = response.data;
      })
      .catch(error => {
        console.error(error);
      });
  },
  methods: {
    submitForm() {
      axios.post('http://127.0.0.1:8000/salon/salons/create/', this.salon)
        .then(response => {
          // Handle successful form submission
          console.log(response.data);
        })
        .catch(error => {
          // Handle form submission error
          console.error(error);
        });
    }
  }
};
</script>

```


### RegistrationCustomerForm.vue

Description: Component for customer registration form.

```vue
<template>
  <form @submit.prevent="submitForm">
    <!-- Other form fields -->
    <div>
      <br />

    <label for="password">Password:</label>
      <input type="text" id="password" v-model="owner.password" required>
    </div>
    <div>
      <label for="username">Username:</label>
      <input type="text" id="username" v-model="owner.username" required>
    </div>
    <div>
      <label for="first_name">First name:</label>
      <input type="text" id="first_name" v-model="owner.first_name">
    </div>
    <div>
      <label for="last_name">Last name:</label>
      <input type="text" id="last_name" v-model="owner.last_name">
    </div>

    <div>
      <label for="email">Email:</label>
      <input type="text" id="email" v-model="owner.email">
    </div>

    <div>
      <label for="phone_number">Phone number:</label>
      <input type="text" id="phone_number" v-model="owner.phone_number">
    </div>


    <button type="submit">Submit</button>
  </form>
</template>
<style>
input[type=text], select {
  width: 100%;
  padding: 12px 20px;
  margin: 8px 0;
  display: inline-block;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
}

input[type=submit] {
  width: 100%;
  background-color: #4CAF50;
  color: white;
  padding: 14px 20px;
  margin: 8px 0;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

input[type=submit]:hover {
  background-color: #45a049;
}

div {
  border-radius: 5px;
  background-color: #f2f2f2;
  padding: 20px;
}
</style>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      owner: {
        password: '',
        username: '',
        first_name: '',
        last_name: '',
        email: '',
        phone_number: '',
      },
      owners: []  // Array to store the list of owners
    };
  },
  methods: {
    submitForm() {
      axios.post('http://127.0.0.1:8000/salon/customers/create/', this.owner)
        .then(response => {
          // Handle successful form submission
          console.log(response.data);
        })
        .catch(error => {
          // Handle form submission error
          console.error(error);
        });
    }
  }
};
</script>
```


### RegistrationOwnerForm.vue

Description: Component for owner registration form.

```vue
<template>
  <form @submit.prevent="submitForm">
    <!-- Other form fields -->
    <div>
      <br />

    <label for="password">Password:</label>
      <input type="text" id="password" v-model="owner.password" required>
    </div>
    <div>
      <label for="username">Username:</label>
      <input type="text" id="username" v-model="owner.username" required>
    </div>
    <div>
      <label for="first_name">First name:</label>
      <input type="text" id="first_name" v-model="owner.first_name">
    </div>
    <div>
      <label for="last_name">Last name:</label>
      <input type="text" id="last_name" v-model="owner.last_name">
    </div>

    <div>
      <label for="email">Email:</label>
      <input type="text" id="email" v-model="owner.email">
    </div>

    <div>
      <label for="phone_number">Phone number:</label>
      <input type="text" id="phone_number" v-model="owner.phone_number">
    </div>


    <button type="submit">Submit</button>
  </form>
</template>
<style scoped>
button {
  background-color: #04AA6D; /* Green */
  border: none;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
}

input[type=text], select {
  width: 100%;
  padding: 12px 20px;
  margin: 8px 0;
  display: inline-block;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
}

input[type=submit] {
  width: 100%;
  background-color: #4CAF50;
  color: white;
  padding: 14px 20px;
  margin: 8px 0;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

input[type=submit]:hover {
  background-color: #45a049;
}

div {
  border-radius: 5px;
  background-color: #f2f2f2;
  padding-left: 0px;
}
</style>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      owner: {
        password: '',
        username: '',
        first_name: '',
        last_name: '',
        email: '',
        phone_number: '',
      },
      owners: []  // Array to store the list of owners
    };
  },
  methods: {
    submitForm() {
      axios.post('http://127.0.0.1:8000/salon/owners/create/', this.owner)
        .then(response => {
          // Handle successful form submission
          console.log(response.data);
        })
        .catch(error => {
          // Handle form submission error
          console.error(error);
        });
    }
  }
};
</script>

```


## Salon Components

### SalonForm.vue

Description: Component for creating a salon.

```vue
<template>
  <form @submit.prevent="submitForm">
    <!-- Other form fields -->
    <div>
      <label for="owner">Owner:</label>
      <select id="owner" v-model="salon.owner" required>
        <option v-for="owner in owners" :value="owner.id">{{ owner.username }}</option>
      </select>
      <br />

    <label for="name">Name:</label>
      <input type="text" id="name" v-model="salon.name" required>
    </div>
    <div>
      <label for="type">Type:</label>
      <input type="text" id="type" v-model="salon.type" required>
    </div>
    <div>
      <label for="city">City:</label>
      <input type="text" id="city" v-model="salon.city">
    </div>
    <div>
      <label for="description">Description:</label>
      <input type="text" id="description" v-model="salon.description">
      <input type="hidden" id="date_registered" v-model="salon.date_registered" />

    </div>
    <button type="submit">Submit</button>
  </form>
</template>
<style scoped>
input[type=text], select {
  width: 100%;
  padding: 12px 20px;
  margin: 8px 0;
  display: inline-block;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
}

input[type=submit] {
  width: 100%;
  background-color: #4CAF50;
  color: white;
  padding: 14px 20px;
  margin: 8px 0;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button {
  background-color: #04AA6D; /* Green */
  border: none;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
}

button[type="submit"] {
  background-color: #4CAF50; /* Green */
  border: none;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;
  border-radius: 10px;
}

button[type="submit"]:hover {
  background-color: #45a049; /* Darker green */
}


input[type=submit]:hover {
  background-color: #45a049;
}

div {
  border-radius: 5px;
  background-color: #f2f2f2;
  padding: 20px;
}

select {
  border: 2px solid grey;
}
input {
  border: 2px solid grey;
}

</style>

<script>
import axios from 'axios';
import moment from 'moment';

export default {
  data() {
    return {
      salon: {
        name: '',
        type: '',
        city: '',
        description: '',
        owner: null,  // Initialize owner as null
        date_registered: moment(new Date().toISOString()).format('YYYY-MM-DD')  // Initialize date_registered with current time
      },
      owners: []  // Array to store the list of owners
    };
  },
  computed: {
    formattedDate() {
      return moment(this.salon.date_registered).format('YYYY-MM-DD');
    }
  },
  created() {
    // Fetch the list of owners from the Django backend when the component is created
    axios.get('http://127.0.0.1:8000/salon/owners/')
      .then(response => {
        this.owners = response.data;
      })
      .catch(error => {
        console.error(error);
      });
  },
  methods: {
    submitForm() {
      axios.post('http://127.0.0.1:8000/salon/salons/create/', this.salon)
        .then(response => {
          // Handle successful form submission
          console.log(response.data);
        })
        .catch(error => {
          // Handle form submission error
          console.error(error);
        });
    }
  }
};
</script>

```


### SalonList.vue

Description: Component for displaying a list of salons.

```vue
<template>
 <div class="salon" v-for="salon in salons"> <!-- v-for - директива для отображения списка элементов на основе массива. -->
   <div class="salon"><strong>Название:</strong> {{ salon.name }}</div>
   <div class="salon"><strong>Город:</strong> {{ salon.city }}</div>

 </div>
</template>

<script>
import SalonServiceList from "@/components/SalonServiceList.vue";
import axios from 'axios';

export default {
 components: {
   SalonServiceList
 },
 props: {
   salons: {
     type: Array,
     required: true
   }
 },
   methods: {
    async fetchSalonServices(salonId) {
      const url = `http://127.0.0.1:8000/salon/${salonId}/services/`;
      axios
        .get(url)
        .then((response) => {
          this.salonServices = response.data;
          console.log(this.salonServices);
        })
        .catch((error) => {
          console.error(error);
          alert("Error fetching salon services");
        });
  },
},
 mounted() {
   this.fetchSalonServices(0) // Vue вызывает хук mount(), когда компонент добавляется в DOM.  В данном примере это позволяет вызвать fetchSalons для получения списка воинов до отрисовки страницы в браузере, благодаря этому страница загружается с уже полученными ранее данными.
 }

}
</script>

<style>
.salon {
  padding: 20px;
  margin: 10px;
    margin-top: 20px;

  border: 1px solid gray;
  padding: 8px;
    text-align: center;
  text-transform: uppercase;
  color: #4CAF50;
  text-indent: 50px;
  text-align: justify;
  letter-spacing: 3px;
text-decoration: none;
  color: #008CBA;
}


</style>
```

### SalonServiceForm.vue

Description: Component for creating a salon service.

```vue
<template>
  <div>
    <form @submit.prevent="submitForm">
      <div>
        <label for="salon">Salon:</label>
        <select v-model="appointment.salon" id="salon">
          <option v-for="salon in salons" :value="salon.id">{{ salon.name }}</option>
        </select>
      </div>
      <div>
        <label for="customer">Customer:</label>
        <select v-model="appointment.customer" id="customer">
          <option v-for="customer in customers" :value="customer.id">{{ customer.username }}</option>
        </select>
      </div>
      <div>
        <label for="service">Service:</label>
        <select v-model="appointment.service" id="service">
          <option v-for="service in services" :value="service.id">{{ service.name }}</option>
        </select>
      </div>
      <div>
        <label for="datetime">Date and Time:</label>
        <input type="datetime-local" v-model="appointment.datetime" id="datetime">
      </div>
      <button type="submit">Submit</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';
import moment from 'moment';

export default {
  data() {
    return {
      appointment: {
        salon: null,
        customer: null,
        service: null,
        datetime: moment(new Date().toISOString()).format('YYYY-MM-DD')
      },
      salons: [],
      customers: [],
      services: []
    };
  },
  created() {
    // Fetch data from backend endpoints
    this.fetchSalons();
    this.fetchCustomers();
    this.fetchServices();
  },
 computed: {
    formattedDate() {
      return moment(this.appointment.datetime).format('YYYY-MM-DD');
    }
  },

  methods: {
    fetchSalons() {
      fetch('http://127.0.0.1:8000/salon/salons/')
        .then(response => response.json())
        .then(data => {
          this.salons = data;
        });
    },
    fetchCustomers() {
      fetch('http://127.0.0.1:8000/salon/customers/')
        .then(response => response.json())
        .then(data => {
          this.customers = data;
        });
    },
    fetchServices() {
      fetch('http://127.0.0.1:8000/salon/services/')
        .then(response => response.json())
        .then(data => {
          this.services = data;
        });
    },
    submitForm() {
    this.appointment.datetime = moment(this.appointment.datetime).format('YYYY-MM-DD');
    console.log(this.appointment);
      axios.post('http://127.0.0.1:8000/salon/appointments/create/', this.appointment)
        .then(response => {
          // Handle successful form submission
          console.log(response.data);
        })
        .catch(error => {
          // Handle form submission error
          console.error(error);
        });
    }
  }
};
</script>

<style scoped>
select {
  border: 2px solid grey;
}
input {
  border: 2px solid grey;
}

button {
  background-color: #04AA6D; /* Green */
  border: none;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
}

</style>

```


### SalonServiceList.vue

Description: Component for displaying a list of salon services.

```vue
<template>
<div>
 <div class="service" v-for="service in salonServices"> <!-- v-for - директива для отображения списка элементов на основе массива. -->
   <div class="service"><strong>Name:</strong> {{ service.name }}</div>
   <div class="service"><strong>Description:</strong> {{ service.description }}</div>
 </div>
</div>
</template>

<script>
export default {
 props: {
   salonServices: {
     type: Array,
     required: true
   }
}
}
</script>

<style>
.salon {
  padding: 20px;
  margin: 10px;
    margin-top: 20px;

  border: 1px solid gray;
  padding: 8px;
    text-align: center;
  text-transform: uppercase;
  color: #4CAF50;
  text-indent: 50px;
  text-align: justify;
  letter-spacing: 3px;
text-decoration: none;
  color: #008CBA;
}


</style>
```


## Authentication Components

### SignIn.vue

Description: Component for user sign-in.

```vue
<template>
  <div>
    <div v-if="isAuthenticated">
      <!-- Show authenticated content -->
      <h3>You are already signed in as {{ user }}!</h3>
    </div>
    <div v-else>
      <!-- Show login form -->

      <input v-model="owners.username" type="text" placeholder="Username">
      <input v-model="owners.password" type="password" placeholder="Password">
      <v-btn @click="login">Login</v-btn>

    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  computed: {
    isAuthenticated() {
      return this.$store.state.isAuthenticated;
    },
    user() {
      return this.$store.state.user;
    }
  },
  data() {
    return {
      owners: {
        password: '',
        username: '',
      },
    };
  },
  methods: {
    login() {
  const formData = new FormData();
  formData.append('username', this.owners.username);
  formData.append('password', this.owners.password);
  this.$store.dispatch('login', formData);
    },
    logout() {
      this.$store.dispatch('logout');
    },

  }
};
</script>


<style>
input[type=text], select {
  width: 100%;
  padding: 12px 20px;
  margin: 8px 0;
  display: inline-block;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
}

input[type=submit] {
  width: 100%;
  background-color: #4CAF50;
  color: white;
  padding: 14px 20px;
  margin: 8px 0;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

input[type=submit]:hover {
  background-color: #45a049;
}

div {
  border-radius: 5px;
  background-color: #f2f2f2;
  padding-left: 0px;
}
</style>

```

### SignUpChoice.vue

Description: Component for user sign-up options.

```vue
<template>
  <div>
    <div v-if="!showForm">
      <p>Are you a customer or a business owner?</p>
      <v-btn @click="showCustomerForm">I am a customer</v-btn>
      <v-btn @click="showOwnerForm">I am an owner</v-btn>
    </div>

    <RegistrationCustomerForm v-if="showForm === 'customer'" />
    <RegistrationOwnerForm v-if="showForm === 'owner'" />
  </div>
</template>

<script>
import RegistrationCustomerForm from './RegistrationCustomerForm.vue';
import RegistrationOwnerForm from './RegistrationOwnerForm.vue';

export default {
  components: {
    RegistrationCustomerForm,
    RegistrationOwnerForm
  },
  data() {
    return {
      showForm: null
    };
  },
  methods: {
    showCustomerForm() {
      this.showForm = 'customer';
    },
    showOwnerForm() {
      this.showForm = 'owner';
    }
  }
};
</script>

```

### UserComponent.vue

Description: Component for user-related info.

```vue
<template>

    <div v-if="isAuthenticated">
      <!-- Show authenticated content -->
      <h1>Welcome, {{ user }}!</h1>
      <v-btn @click="logout">Logout</v-btn>
    </div>
    <div v-else>
      <h1>Welcome, AnonUser!</h1>
    </div>

</template>
<style>
.div {
  padding: 0;
  margin: 0;
}

.button {
  background-color: #04AA6D; /* Green */
  border: none;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
}

</style>


<script>
export default {
  computed: {
    isAuthenticated() {
      return this.$store.state.isAuthenticated;
    },
    user() {
      return this.$store.state.user;
    }
  },
  data() {
    return {
      currentUser: {}
    };
  },
  mounted() {
    this.fetchCurrentUser();
  },
  methods: {
    async fetchCurrentUser() {
      try {
        const response = await fetch('http://127.0.0.1:8000/salon/api/current_user/');
        console.log(response);
        const data = await response.json();
        console.log(data);
        this.currentUser = data;
      } catch (error) {
        console.error('Error fetching current user:', error);
      }
    }
  }
};
</script>
```


## Welcome Components

### Welcome.vue

Description: Component displaying a welcome page.

```vue
<template>
    <UserComponent />
  <div >
    <div v-if="!showComponent">
      <v-btn @click="showSignIn">Sign in</v-btn>
      <v-btn @click="showSignUp">Sign up</v-btn>
      <v-btn @click="showSalons">Show Salons</v-btn>
      <v-btn @click="showService">Register for a service</v-btn>
      <v-btn @click="showAppointment">Show appointments</v-btn>


    </div>

    <div v-if="showComponent === 'signIn'">
      <SignIn />
    </div>

    <div v-if="showComponent === 'signUp'">
      <SignUpChoice />
    </div>

    <div v-if="showComponent === 'salons'">
      <Salons />
    </div>

     <div v-if="showComponent === 'service'">
      <SalonServiceForm />
    </div>

     <div v-if="showComponent === 'appointment'">
       <appointment-edit-form
         v-if="editingAppointment"
         :appointment="editingAppointment"
         @cancel-edit="cancelEdit"
       />
       <appointment-list
         v-else
         :appointments="appointments"
         @edit-appointment="startEdit"
       />
    </div>


    <v-btn v-if="showComponent" @click="goBack">Go back</v-btn>
  </div>
</template>

<style>
button {
  background-color: #04AA6D; /* Green */
  border: none;
  color: white;
  padding: 15px 32px;
  margin: 5px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
}

.select-selected {
  background-color: DodgerBlue;
}


select {
  border: 1px;
  background-color: DodgerBlue;
  border-color: black;
}

</style>

<script>
import axios from 'axios';
import SignIn from './SignIn.vue';
import SignUpChoice from './SignUpChoice.vue';
import UserComponent from './UserComponent.vue';
import Salons from '@/views/Salons.vue';
import SalonServiceForm from './SalonServiceForm.vue';
import AppointmentList from './AppointmentList.vue';
import AppointmentEditForm from "@/components/AppointmentEditForm.vue";


export default {
  components: {
    SignIn,
    SignUpChoice,
    UserComponent,
    Salons,
    SalonServiceForm,
    AppointmentList,
    AppointmentEditForm
  },
  data() {
    return {
      showComponent: null,
      editingAppointment: null,
      appointments: []
    };
  },
  created() {
    this.fetchAppointments();
  },
  methods: {
    showSignIn() {
      this.showComponent = 'signIn';
    },
    showSignUp() {
      this.showComponent = 'signUp';
    },
    showSalons() {
      this.showComponent = 'salons';
    },
    showAppointment() {
      this.showComponent = 'appointment';
    },
    showService() {
      this.showComponent = 'service';
    },
    goBack() {
      this.showComponent = null;
    },
    fetchAppointments() {
      axios
        .get("http://127.0.0.1:8000/salon/appointments/")
        .then((response) => {
          this.appointments = response.data;
        })
        .catch((error) => {
          console.error(error);
          alert("Error fetching appointments");
        });
    },
    startEdit(appointment) {
      this.editingAppointment = appointment;
    },
    cancelEdit() {
      this.editingAppointment = null;
    },
  },

};
</script>

```
