<template>
  <div class="news-list">
    <div v-for="newsItem in medicalNews" :key="newsItem.id" class="news-item">
      <h3>{{ newsItem.title }}</h3>
      <p>{{ newsItem.description }}</p>
    </div>
  </div>
</template>
  
  <script>
export default {
  data() {
    return {
      medicalNews: [
        { id: 1, title: "С новым годом!", description: "Поздравляем вас с наступающим праздником! Спасибо, что выбираете нас" },
        { id: 2, title: "Открыта запись на январь 2024", description: "График работы в январьские праздники :1 января - выходной, со 2 января в обычном графике - 10:00-20:00" },
        { id: 3, title: "Новые врачи", description: "Скидки на первое посещение!" }
      ],

    };
  }
};
</script>

<style>
.news-list {
  display: flex;
  flex-direction: column;
  align-items: center;
  max-width: 800px;
  margin: 0 auto;
}

.news-item {
  margin-bottom: 20px;
  padding: 20px;
  border: 1px solid #e3e3e3;
  border-radius: 10px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  width: 100%;
  transition: box-shadow 0.3s ease-in-out;
}

.news-item:hover {
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

h3 {
  margin-top: 0;
  color: #333;
  font-size: 24px;
}

p {
  color: #555;
  line-height: 1.5;
}
</style>