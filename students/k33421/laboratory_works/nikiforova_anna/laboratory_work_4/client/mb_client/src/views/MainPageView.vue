<template>
  <v-container>
    <NavbarComponent />

    <div class="description-section">
      <p class="description-text">
        Добро пожаловать, мы - студенческое СМИ.
        Наши талантливые авторы предоставляют разнообразные материалы, которые касаются различных аспектов студенческой жизни,
        общественных событий и актуальных тем. Будьте в курсе новостей, получайте знания и наслаждайтесь увлекательным контентом!
      </p>
    </div>

    <h2 class="section-title">Что ещё мы делаем?</h2>
    <WhatWeDoComponent />

    <h2 class="section-title">Наши статьи</h2>
    <ArticlesComponent />
  </v-container>
</template>

<script>
import NavbarComponent from "@/components/NavbarComponent.vue";
import ArticlesComponent from "@/components/ArticlesComponent.vue";
import WhatWeDoComponent from "@/components/WhatWeDoComponent.vue";

export default {
  name: "MainPageView",
  components: {
    NavbarComponent,
    WhatWeDoComponent,
    ArticlesComponent,
  },
};
</script>

<style scoped>
.section-title {
  font-size: 2em;
  text-align: left;
  margin: 40px 0;
  color: #3c3c3c;
}

.description-section {
  text-align: left;
  margin: 40px 0;
}

.description-text {
  font-size: 1em;
  color: #777;
}
</style>
