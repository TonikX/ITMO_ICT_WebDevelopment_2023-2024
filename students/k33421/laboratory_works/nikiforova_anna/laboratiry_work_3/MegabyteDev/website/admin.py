from django.db.models import Max
from django.urls import reverse
from django import forms
from django.contrib import admin
from django.utils.html import format_html
from django.contrib.auth.admin import UserAdmin
from .models import *


class CustomAdminSite(admin.AdminSite):
    site_header = 'Администрирование сайта'

    def __init__(self, name="admin"):
        super().__init__(name)
        self.app_list = None
        self.model_dict_cache = {}

    def get_model_dict(self, object_name):
        if object_name in self.model_dict_cache:
            return self.model_dict_cache[object_name]

        for app in self.app_list:
            for model_dict in app['models']:
                if model_dict['object_name'] == object_name:
                    model_dict_data = {
                        'model': model_dict['model'],
                        'name': model_dict['name'],
                        'object_name': model_dict['object_name'],
                        'perms': model_dict['perms'],
                        'admin_url': model_dict['admin_url'],
                        'add_url': model_dict['add_url'],
                        'view_only': model_dict['view_only'],
                    }
                    self.model_dict_cache[object_name] = model_dict_data
                    return model_dict_data
        return None

    def get_app_list(self, request):
        self.app_list = super().get_app_list(request)
        new_app_list = []

        grouped_models = {
            'Пользователи': ['User'],
            'Баннеры': ['Banner'],
            'Статьи': ['Rubric', 'Hashtag', 'Role', 'Article'],
            'Подкасты': ['Platform', 'Podcast'],
            'На бумаге': ['Newspaper', 'Newtone'],
            'Общее': ['WhatWeDo'],
            'Моё избранное': ['Favourite'],
        }

        for group_name, models in grouped_models.items():
            group = {
                'name': group_name,
                'app_label': '',
                'app_url': '',
                'has_module_perms': True,
                'models': [self.get_model_dict(model) for model in models],
            }
            new_app_list.append(group)

        return new_app_list


class IsPublishedFilter(admin.SimpleListFilter):
    title = 'Опубликовано'
    parameter_name = 'is_published'

    def lookups(self, request, model_admin):
        return (
            ('True', 'Да'),
            ('False', 'Нет'),
        )

    def queryset(self, request, queryset):
        if not self.value():
            return queryset
        else:
            pks = []
            if self.value() == 'True':
                for obj in queryset:
                    try:
                        if obj.is_published:
                            pks.append(obj.pk)
                    except Exception:
                        pass
            elif self.value() == 'False':
                for obj in queryset:
                    try:
                        if not obj.is_published:
                            pks.append(obj.pk)
                    except Exception:
                        pass
            out = queryset.filter(pk__in=pks)
            return out


class BaseModelInline(admin.options.InlineModelAdmin):
    extra = 1
    model = None

    def get_model(self):
        if self.model is None:
            raise NotImplementedError("Subclasses must set the 'model' attribute.")
        return self.model

    class Meta:
        abstract = True


class BaseStackedInline(BaseModelInline, admin.StackedInline):
    pass


class BaseTabularInline(BaseModelInline, admin.TabularInline):
    pass


class WhatWeDoAdmin(admin.ModelAdmin):
    search_fields = ['name', 'short_description']
    list_display = ('display_picture', 'name_with_link', 'truncated_description')

    def display_picture(self, obj):
        return format_html('<img src="{}" width="50" height="50" style="border-radius: 50%;" />', obj.cover_picture.url)

    display_picture.short_description = 'Обложка'

    def name_with_link(self, obj):
        return format_html('<strong><a href="{}">{}</a></strong>',
                           reverse(f'admin:{obj._meta.app_label}_{obj._meta.model_name.lower()}_change', args=[obj.id]),
                           obj.name)

    name_with_link.short_description = 'Название'

    def truncated_description(self, obj):
        return (obj.short_description[:200] + '...') if obj.short_description else ''

    truncated_description.short_description = 'Описание'


class PodcastLinkInline(BaseTabularInline):
    model = PodcastLink
    autocomplete_fields = ['platform']


class PodcastIssueInline(BaseStackedInline):
    model = PodcastIssue


class PodcastAdmin(admin.ModelAdmin):
    inlines = [PodcastLinkInline, PodcastIssueInline]
    search_fields = ['name', 'description']
    list_display = ('display_picture', 'name_with_link', 'truncated_description', 'date_of_last_release')

    def display_picture(self, obj):
        return format_html('<img src="{}" width="50" height="50" style="border-radius: 50%;" />', obj.cover_picture.url)

    display_picture.short_description = 'Обложка'

    def name_with_link(self, obj):
        return format_html('<strong><a href="{}">{}</a></strong>',
                           reverse(f'admin:{obj._meta.app_label}_{obj._meta.model_name.lower()}_change',
                                   args=[obj.id]), obj.name)

    name_with_link.short_description = 'Название'

    def truncated_description(self, obj):
        return (obj.description[:200] + '...') if obj.description else ''

    truncated_description.short_description = 'Описание'

    def date_of_last_release(self, obj):
        last_release_date = obj.podcast_issues.aggregate(Max('release_date'))['release_date__max']
        return last_release_date

    date_of_last_release.short_description = 'Дата последнего выпуска'


class PlatformAdmin(admin.ModelAdmin):
    search_fields = ['name']


class RubricAdmin(admin.ModelAdmin):
    search_fields = ['name', 'short_description']
    list_display = ('name', 'truncated_description')

    def truncated_description(self, obj):
        return (obj.short_description[:200] + '...') if obj.short_description else ''

    truncated_description.short_description = 'Описание'


class HashtagAdmin(admin.ModelAdmin):
    search_fields = ['name']


class HashtagsInline(BaseTabularInline):
    model = Hashtags
    autocomplete_fields = ['hashtag']


class RoleAdmin(admin.ModelAdmin):
    search_fields = ['name']


class ParticipantInlineForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        user_field = self.fields['user']
        if hasattr(user_field, 'queryset'):
            user_field.queryset = user_field.queryset.filter(is_active=True, is_team_member=True)


class ParticipantInline(BaseTabularInline):
    model = Participant
    form = ParticipantInlineForm
    autocomplete_fields = [
        'role']  # I wish I could add user autocomplete but it gives the whole list of users not only filtered ones


class RubricFilter(admin.SimpleListFilter):
    title = 'Рубрика'
    parameter_name = 'rubric'

    def lookups(self, request, model_admin):
        rubrics = set(model_admin.model.objects.values_list('rubric__name', flat=True))
        return [(rubric, rubric) for rubric in rubrics]

    def queryset(self, request, queryset):
        value = self.value()
        if value:
            return queryset.filter(rubric__name=value)
        return queryset


class ArticleAdmin(admin.ModelAdmin):
    inlines = [HashtagsInline, ParticipantInline]
    search_fields = ['name']
    autocomplete_fields = ['rubric']
    list_filter = ['is_hidden', IsPublishedFilter, RubricFilter]
    actions = ['mark_as_hidden', 'mark_as_not_hidden']
    admin_order_field = ['datetime_published', 'release_date']
    list_display = ('display_picture', 'name_with_link', 'truncated_description', 'rubric',
                    'view_is_published', 'is_hidden', 'datetime_published', 'release_date')

    def display_picture(self, obj):
        return format_html('<img src="{}" width="50" height="50" style="border-radius: 50%;" />',
                           obj.cover_picture.url)

    display_picture.short_description = 'Обложка'

    def name_with_link(self, obj):
        return format_html('<strong><a href="{}">{}</a></strong>',
                           reverse(f'admin:{obj._meta.app_label}_{obj._meta.model_name.lower()}_change',
                                   args=[obj.id]), obj.name)

    name_with_link.short_description = 'Название'

    def view_is_published(self, obj):
        return obj.is_published

    view_is_published.short_description = 'Опубликовано'
    view_is_published.boolean = True

    def truncated_description(self, obj):
        return (obj.short_description[:200] + '...') if obj.short_description else ''

    truncated_description.short_description = 'Описание'

    def mark_as_hidden(self, request, queryset):
        queryset.update(is_hidden=True)

    mark_as_hidden.short_description = "Скрыть выбранные"

    def mark_as_not_hidden(self, request, queryset):
        queryset.update(is_hidden=False)

    mark_as_not_hidden.short_description = "Открыть выбранные (будут отображаться, если опубликованы)"


class ArticleFilter(admin.SimpleListFilter):
    title = 'Наличие статьи'
    parameter_name = 'article'

    def lookups(self, request, model_admin):
        return [
            ('has_article', 'Статья прикриплена'),
            ('no_article', 'Статья не прикреплена'),
        ]

    def queryset(self, request, queryset):
        if self.value() == 'has_article':
            return queryset.exclude(article=None)
        elif self.value() == 'no_article':
            return queryset.filter(article=None)
        else:
            return queryset


class PublicationPageInline(BaseStackedInline):
    model = PublicationPage
    autocomplete_fields = ['article']


class PublicationAdmin(admin.ModelAdmin):
    inlines = [PublicationPageInline]

    search_fields = ['name', 'short_description']
    list_filter = ['is_hidden', IsPublishedFilter]
    actions = ['mark_as_hidden', 'mark_as_not_hidden']
    admin_order_field = ['datetime_published', 'release_date']
    list_display = ('display_picture', 'name_with_link',
                    'truncated_description', 'view_is_published', 'is_hidden',
                    'datetime_published', 'release_date')

    def display_picture(self, obj):
        return format_html('<img src="{}" width="50" height="50" style="border-radius: 50%;" />', obj.cover_picture.url)

    display_picture.short_description = 'Обложка'

    def name_with_link(self, obj):
        return format_html('<strong><a href="{}">{}</a></strong>',
                           reverse(f'admin:{obj._meta.app_label}_{obj._meta.model_name.lower()}_change',
                                   args=[obj.id]), obj.name)

    name_with_link.short_description = 'Название'

    def view_is_published(self, obj):
        return obj.is_published

    view_is_published.short_description = 'Опубликовано'
    view_is_published.boolean = True

    def truncated_description(self, obj):
        return (obj.short_description[:200] + '...') if obj.short_description else ''

    truncated_description.short_description = 'Описание'

    def mark_as_hidden(self, request, queryset):
        queryset.update(is_hidden=True)

    mark_as_hidden.short_description = "Скрыть выбранные"

    def mark_as_not_hidden(self, request, queryset):
        queryset.update(is_hidden=False)

    mark_as_not_hidden.short_description = "Открыть выбранные (будут отображаться, если опубликованы)"


class BannerAdmin(admin.ModelAdmin):
    autocomplete_fields = ['article']
    search_fields = ['article__name']

    list_display = ('display_picture', 'name_with_link', 'article_name')

    def display_picture(self, obj):
        return format_html('<img src="{}" width="50" height="50" style="border-radius: 50%;" />', obj.cover_picture.url)

    display_picture.short_description = 'Обложка'

    def name_with_link(self, obj):
        return format_html('<strong><a href="{}">{}</a></strong>',
                           reverse(f'admin:{obj._meta.app_label}_{obj._meta.model_name.lower()}_change',
                                   args=[obj.id]), str(obj))

    name_with_link.short_description = 'Название'

    def article_name(self, obj):
        if obj.article:
            return format_html('<strong><a href="{}">{}</a></strong>',
                               reverse(
                                   f'admin:{obj.article._meta.app_label}_{obj.article._meta.model_name.lower()}_change',
                                   args=[obj.article.id]), obj.article.name)
        return ''

    article_name.short_description = 'Статья'


class CustomUserAdmin(UserAdmin):
    list_filter = ['is_active', 'is_team_member', 'groups']
    search_fields = ('full_name',)

    readonly_fields = ('date_joined',)

    fieldsets = (
        (None, {
            'fields': ('first_name', 'last_name', 'patronymic', 'username', 'email',
                       'profile_picture', 'profile_info')
        }),
        ('Администрирование', {
            'classes': ('collapse',),
            'fields': ('is_active',
                       'is_team_member', 'is_superuser', 'is_staff', 'groups')
        })
    )

    actions = ['add_to_team', 'delete_from_team', 'make_active', 'make_inactive']

    list_display = ('display_picture', 'name_with_link', 'email', 'is_active',
                    'is_team_member')

    def get_readonly_fields(self, request, obj=None):
        if not request.user.is_superuser or (obj and obj != request.user):
            return self.readonly_fields + ('first_name', 'last_name', 'patronymic', 'username', 'email',
                                            'profile_picture', 'profile_info')
        return self.readonly_fields

    def display_picture(self, obj):
        return format_html('<img src="{}" width="50" height="50" style="border-radius: 50%;" />',
                           obj.profile_picture.url)

    display_picture.short_description = 'Аватарка'

    def name_with_link(self, obj):
        return format_html('<strong><a href="{}">{}</a></strong>',
                           reverse(f'admin:{obj._meta.app_label}_{obj._meta.model_name.lower()}_change',
                                   args=[obj.id]), obj.full_name)

    name_with_link.short_description = 'ФИО'

    def add_to_team(self, request, queryset):
        queryset.update(is_team_member=True)

    add_to_team.short_description = "Добавить в команду"

    def delete_from_team(self, request, queryset):
        queryset.update(is_team_member=False)

    delete_from_team.short_description = "Удалить из команды"

    def make_active(self, request, queryset):
        queryset.update(is_active=True)

    make_active.short_description = "Пометить как активных"

    def make_inactive(self, request, queryset):
        queryset.update(is_active=False)

    make_inactive.short_description = "Пометить как неактивных"


class CustomFavouriteAdmin(admin.ModelAdmin):
    list_display = ('alter', 'content_object_name',)
    search_fields = ('content_object__name',)
    exclude = ['user']

    def alter(self, obj):
        return 'Изменить'

    alter.short_description = ""

    def content_object_name(self, obj):
        if obj.content_object:
            return format_html('<strong><a href="{}">{}</a></strong>',
                               reverse(
                                   f'admin:{obj.content_object._meta.app_label}_{obj.content_object._meta.model_name.lower()}_change',
                                   args=[obj.content_object.id]), obj.content_object.name)
        return ''

    content_object_name.short_description = "Избранное"

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        if request.user.is_superuser:
            return Favourite.objects.filter(user=request.user)
        return Favourite.objects.none()


custom_admin_site = CustomAdminSite(name='custom_admin')

custom_admin_site.register(WhatWeDo, WhatWeDoAdmin)
custom_admin_site.register(Rubric, RubricAdmin)
custom_admin_site.register(Hashtag, HashtagAdmin)
custom_admin_site.register(Hashtags)
custom_admin_site.register(Article, ArticleAdmin)
custom_admin_site.register(Banner, BannerAdmin)
custom_admin_site.register(Newspaper, PublicationAdmin)
custom_admin_site.register(Newtone, PublicationAdmin)
custom_admin_site.register(PublicationPage)
custom_admin_site.register(Podcast, PodcastAdmin)
custom_admin_site.register(Platform, PlatformAdmin)
custom_admin_site.register(PodcastLink)
custom_admin_site.register(PodcastIssue)
custom_admin_site.register(User, CustomUserAdmin)
custom_admin_site.register(Favourite, CustomFavouriteAdmin)
custom_admin_site.register(Role, RoleAdmin)
custom_admin_site.register(Participant)
