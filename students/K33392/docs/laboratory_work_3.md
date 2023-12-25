# Лабораторная работа 3

## Задание
Реализация серверной части приложения средствами django и djangorestframework для проекта "Блог"

## models.py

У пользователя будут дополнительные поля для описания профиля и его фотографии
```python
class User(AbstractUser):
  bio = models.TextField(blank=True)
  profile_picture = models.ImageField(upload_to="profile_pics/", blank=True, null=True)

```

У каждой публицкации есть автор, текст самой публикации, дата создания и количество лайков
```python
class Post(models.Model):
  author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  likes = models.ManyToManyField(User, related_name="liked_posts", blank=True)

```

Для каждого поста также будет возможность оставить комментарий. Создадим модель, которая будет хранить в себе публикацию и пользователя, а также текст самого комментария.
```python
class Comment(models.Model):
  post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)

```

Пользователь может подписаться на обновления другого пользователя
```python
class Follow(models.Model):
  follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name="following")
  followed = models.ForeignKey(User, on_delete=models.CASCADE, related_name="followers")
  created_at = models.DateTimeField(auto_now_add=True)
```

## serializers.py

Для CRUD операция над моделями через API нам необходимо написать `ModelSerializer` для каждой модели.

В `MyUserSerializer` нам необходимо переопределить метод `create`, так как у нас кастомная модель пользователя и нам нужно сохранять хеш пароля в базу
```python
class MyUserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = (
      "id",
      "password",
      "username",
      "email",
      "first_name",
      "last_name",
      "bio",
      "profile_picture",
    )
  def create(self, validated_data):
    return super().create({**validated_data, "password": make_password(validated_data["password"])})
```

Все остальные классы остаются без переопределений методов и выглядят следующим образом:
```python
class PostSerializer(serializers.ModelSerializer):
  class Meta:
    model = Post
    fields = ("id", "author", "content", "created_at", "likes")

class CommentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Comment
    fields = ("id", "post", "author", "content", "created_at")

class FollowSerializer(serializers.ModelSerializer):
  class Meta:
    model = Follow
    fields = ("id", "follower", "followed", "created_at")
```

## views.py

Класс `viewsets.ModelViewSet` из модуля `rest_framework` позволяет нам с легкостью создать представления для наших моделей данных без написания дополнительной логике по обработке запросов
```python
class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = MyUserSerializer

class PostViewSet(viewsets.ModelViewSet):
  queryset = Post.objects.all()
  serializer_class = PostSerializer

class CommentViewSet(viewsets.ModelViewSet):
  queryset = Comment.objects.all()
  serializer_class = CommentSerializer

class FollowViewSet(viewsets.ModelViewSet):
  queryset = Follow.objects.all()
  serializer_class = FollowSerializer
```

## settings.py

Нам необходимо установить несколько модулей, необходимых для авторизации, создания API и генерации документации
```python
INSTALLED_APPS = [
  ...
  "blog_app",
  "rest_framework",
  "rest_framework.authtoken",
  "djoser",
  "django_extensions",
  "drf_yasg",
]
```

Для того, чтобы `djoser` знал о том, какой serializer использовать для модели пользователя, нам необходимо указать путь до класса
```python
DJOSER = {
  "SERIALIZERS": {
    "user_create": "blog_app.serializers.MyUserSerializer",
  },
}
```

По умолчанию все пути нашего сервера будут доступны без авторизации. Нам необходимо обратное, поэтому укажем права доступа в данном файле
```python
REST_FRAMEWORK = {
  "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.IsAuthenticated"],
  "DEFAULT_AUTHENTICATION_CLASSES": [
    "rest_framework.authentication.TokenAuthentication",
  ],
}
```

## urls.py
Определим пути нашего сервера. Для клиента будут доступны
- `api/`
- `auth/`
- `admin/`
- `profile_pics/`
- `swagger/`
```python
# Project
urlpatterns = [
  path("admin/", admin.site.urls),
  path("api/", include("blog_app.urls")),
  path("auth/", include("djoser.urls")),
  path("auth/", include("djoser.urls.authtoken")),
  re_path(
    r"^profile_pics/(?P<path>.*)$",
    serve,
    {
      "document_root": "profile_pics/",
    },
  ),
  path(
    "swagger/",
    schema_view.with_ui("swagger", cache_timeout=0),
    name="schema-swagger-ui",
  ),
]
```

Более того доступные пути в `api/`
- `users/`
- `posts/`
- `comments/`
- `follows/`
```python
# App
r = DefaultRouter()
r.register('users', UserViewSet)
r.register('posts', PostViewSet)
r.register('comments', CommentViewSet)
r.register('follows', FollowViewSet)
urlpatterns = r.urls
```

## Endpoints

### Posts

**URL** : `/api/posts/`

**Method** : `GET, POST`

**Auth required** : YES

**Permissions required** : IsAuthenticated

#### Success Responses

**Code** : `200 OK`

**Content POST** :

```json
{
    "id": 1,
    "author": 3,
    "content": "test",
    "created_at": "2023-12-12T08:10:55.596943Z",
    "likes": []
}
```

**Content GET** :
```json
[
    {
        "id": 1,
        "author": 3,
        "content": "test",
        "created_at": "2023-12-12T08:10:55.596943Z",
        "likes": []
    }
]
```

**URL** : `/api/posts/<int:pk>`

**Method** : `GET, PUT, PATCH, DELETE`

**Auth required** : YES

**Permissions required** : IsAuthenticated

#### Success Responses

**Code** : `200 OK`

**Content** :

```json
{
    "id": 1,
    "author": 3,
    "content": "test",
    "created_at": "2023-12-12T08:10:55.596943Z",
    "likes": []
}
```

### Users
**URL** : `/api/users/`

**Method** : `GET, POST`

**Auth required** : YES

**Permissions required** : IsAuthenticated

#### Success Responses

**Code** : `200 OK`

**Content** :
```json
{
  "id": 4,
  "password": "pbkdf2_sha256$600000$F7f3v7MCJGoP6McdUIbVhy$1C2QmGpBE2qMVXQ7OmdeVMKr/S39AO1ZODnIZDJ56zE=",
  "username": "cruser",
  "email": "",
  "first_name": "",
  "last_name": "",
  "bio": "",
  "profile_picture": null
}
```

**URL** : `/api/users/<int:pk>`

**Method** : `GET, PUT, PATCH, DELETE`

**Auth required** : YES

**Permissions required** : IsAuthenticated

#### Success Responses

**Code** : `200 OK`

**Content** :

```json
{
  "email": "",
  "id": 3,
  "username": "oleg"
}
```

### Comments
**URL** : `/api/comments/`

**Method** : `GET, POST`

**Auth required** : YES

**Permissions required** : IsAuthenticated

#### Success Responses

**Code** : `200 OK`

**Content** :
```json
[
    {
        "id": 1,
        "post": 1,
        "author": 3,
        "content": "test text",
        "created_at": "2023-12-12T08:19:47.471546Z"
    }
]
```

**URL** : `/api/comments/<int:pk>`

**Method** : `GET, PUT, PATCH, DELETE`

**Auth required** : YES

**Permissions required** : IsAuthenticated

#### Success Responses

**Code** : `200 OK`

**Content** :

```json
{
    "id": 1,
    "post": 1,
    "author": 3,
    "content": "test text",
    "created_at": "2023-12-12T08:19:47.471546Z"
}
```
### Follows
**URL** : `/api/follows/`

**Method** : `GET, POST`

**Auth required** : YES

**Permissions required** : IsAuthenticated

#### Success Responses

**Code** : `200 OK`

**Content** :
```json
[
    {
        "id": 1,
        "follower": 3,
        "followed": 3,
        "created_at": "2023-12-12T08:20:54.252996Z"
    }
]
```

**URL** : `/api/follows/<int:pk>`

**Method** : `GET, PUT, PATCH, DELETE`

**Auth required** : YES

**Permissions required** : IsAuthenticated

#### Success Responses

**Code** : `200 OK`

**Content** :

```json
{
    "id": 1,
    "follower": 3,
    "followed": 3,
    "created_at": "2023-12-12T08:20:54.252996Z"
}
```