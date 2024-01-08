<template>
    <div class="page-success">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Спасибо за заказ!</h1>

                <p>Ваш заказ будет обработан и собран в течение двух суток!</p>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Success',
    mounted() {
        document.title = 'Успешно | Книги'
    },
}
</script>