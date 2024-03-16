# Backend

* Django и Django REST Framework: Для создания API бэкенда использовались фреймворки Django и Django REST Framework. Они обеспечивают быстрое создание API на основе моделей данных и предоставляют множество инструментов для обработки запросов.

* Модели данных: Были созданы модели данных для Лабораторных работ, Аудиторий, Учителей, Уроков и других сущностей. Модели определяют структуру данных и взаимосвязи между ними.


```python
class Room(models.Model):
    num = models.CharField(max_length=4)
    base = models.BooleanField(default=True)
    
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    
class Lesson(models.Model):
    name = models.CharField(max_length=100)
```
    
Маршруты и представления: Были созданы маршруты и представления для обработки запросов связанных с Аудиториями, Учителями, Уроками и другими сущностями. Представления взаимодействуют с моделями данных и возвращают JSON-ответы.

```python
class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = serializers.RoomSerializer
```

# Frontend

Vue.js и Vuetify: Во фронтенде использовались фреймворк Vue.js и UI-библиотека Vuetify для создания пользовательского интерфейса. С их помощью были созданы страницы и компоненты для отображения данных о Лабораторных работах, Аудиториях, Учителях, Уроках и других сущностях.

```vue
<template>
  <v-app>
    <div v-for="lesson in lessons" :key="lesson.id">
      <h3>{{ lesson.name }}</h3>
      <!-- Другие детали урока -->
    </div>
  </v-app>
</template>
```

Axios для выполнения запросов: Для отправки HTTP-запросов к бэкенду использовалась библиотека Axios. Она обеспечивает выполнение асинхронных запросов и обработку ответов от сервера.

```vue
<script setup>
import { ref, onMounted } from "vue";
import instance from "@/AxiosInstance";

const lessons = ref([]);

onMounted(() => {
  instance.get('/lessons/').then(response => {
    lessons.value = response.data;
  }).catch(error => console.log(error));
});
</script>
```

Эти технологии и решения обеспечивают создание полнофункционального API и интерфейса пользователя для работы с данными о Лабораторных работах, Аудиториях, Учителях, Уроках и других сущностях в вашем приложении.