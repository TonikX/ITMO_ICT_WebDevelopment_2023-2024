from django.apps import AppConfig # для настройки конфигурации приложения


class HomeworkBoardConfig(AppConfig): # для homework board
    default_auto_field = 'django.db.models.BigAutoField' # указывает, какое поле будет использоваться по умолчанию для автоматического создания уникальных ID для моделей
    name = 'homework_board'
