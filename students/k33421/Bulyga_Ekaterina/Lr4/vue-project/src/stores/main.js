import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import axios from 'axios'
import router from "@/router";

export const useMainStore = defineStore('main', () => {
  const token = ref('');
  const userName = ref('');

  if (localStorage.getItem('auth_token')) {
    setUser({'auth_token': localStorage.getItem('auth_token')})
  }

  const isFieldFocusRegistered = ref(false)

  function setUser(payload) {
    if (payload.auth_token) {
      token.value = payload.auth_token;
      localStorage.setItem('auth_token', payload.auth_token);
      axios.get('http://127.0.0.1:8000/auth/users/me', {headers: {'Authorization': `Token ${token.value}`}})
        .then(resp => userName.value = resp.data.username)
    }
  }

  function unsetUser() {
    localStorage.removeItem('auth_token');
    token.value = '';
    localStorage.setItem('logout', 'true');
  }

  return {
    isFieldFocusRegistered,
    setUser,
    token,
    userName,
    unsetUser,
  }
})
