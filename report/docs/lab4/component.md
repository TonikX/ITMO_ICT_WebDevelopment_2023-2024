## Компонент

У меня реализован один компонент, который передает карточки с мероприятиями на главную страницу и осуществляет переход на страницы карточек.

``` js title="EventList.vue"
<template>
    <div class="event-list">
      <h1>Мероприятия</h1>
      <div class="row">
        <div
          v-for="event in events"
          :key="event.id"
          class="col-md-4 mb-4"
        >
          <CCard style="width: 24rem">
            <CCardBody>
              <CCardTitle>{{ event.PostTitle }}</CCardTitle>
              <CCardSubtitle class="mb-2 text-muted">
                {{ event.EventType.TypeTitle }}
              </CCardSubtitle>
              <CCardText>
                <p>Дата: {{ event.DateOfEvent }}</p>
                <p>
                  Место: {{ event.EventPlace ? event.EventPlace.PlaceTitle : 'Место не указано' }}
                </p>
              </CCardText>
              <router-link :to="{ name: 'event-detail', params: { id: event.id } }">
                <CButton color="dark">Подробнее</CButton>
              </router-link>
            </CCardBody>
          </CCard>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import {
    CCard,
    CCardBody,
    CCardTitle,
    CCardSubtitle,
    CCardText,
    CButton,
  } from '@coreui/vue';
  
  export default {
    components: {
      CCard,
      CCardBody,
      CCardTitle,
      CCardSubtitle,
      CCardText,
      CButton,
    },
  
    data() {
      return {
        events: [],
      };
    },
    mounted() {
      this.$axios
        .get('http://127.0.0.1:8000/api/events/')
        .then((response) => {
          this.events = response.data;
        })
        .catch((error) => {
          console.error('Ошибка при загрузке мероприятий:', error);
        });
    },
  };
  </script>
``` 