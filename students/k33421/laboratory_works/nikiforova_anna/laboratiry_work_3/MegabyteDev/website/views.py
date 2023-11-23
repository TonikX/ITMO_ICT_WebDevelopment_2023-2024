import random
from rest_framework import viewsets, status
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import *
from .models import *
from django_filters import rest_framework as filters


N_WHAT_WE_DOS = 2


class StandardPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'p'
    max_page_size = 100


class RandomWhatWeDoViewSet(viewsets.ReadOnlyModelViewSet):
    """ Отдает N случайных записей WhatWeDo из базы """
    serializer_class = WhatWeDoSerializer
    base_queryset = WhatWeDo.objects.all()
    pagination_class = StandardPagination
    number_of_items = min(N_WHAT_WE_DOS, len(base_queryset))

    def get_queryset(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        if pk:
            queryset = self.base_queryset.filter(pk=pk)
        else:
            queryset = random.sample(list(self.base_queryset), self.number_of_items)
        return queryset


class RubricViewSet(viewsets.ReadOnlyModelViewSet):
    """ Возвращает информацию о рубриках """
    serializer_class = RubricSerializer
    queryset = Rubric.objects.all()
    pagination_class = StandardPagination


class HashtagViewSet(viewsets.ReadOnlyModelViewSet):
    """ Возвращает информацию о хэштегах """
    serializer_class = HashtagSerializer
    queryset = Hashtag.objects.all()
    pagination_class = StandardPagination
    filter_backends = (SearchFilter,)
    search_fields = ('name',)


class PlatformViewSet(viewsets.ReadOnlyModelViewSet):
    """ Возвращает информацию о платформах, на которых могут быть размещены подкасты """
    serializer_class = PlatformSerializer
    queryset = Platform.objects.all()
    pagination_class = StandardPagination
    filter_backends = (SearchFilter, OrderingFilter)
    ordering_fields = ('name',)
    search_fields = ('name',)


class ArticleFilter(filters.FilterSet):
    rubric = filters.ModelMultipleChoiceFilter(
        queryset=Rubric.objects.all(),
        field_name='rubric',
    )

    hashtags = filters.ModelMultipleChoiceFilter(
        queryset=Hashtag.objects.all(),
        field_name='article_hashtags',
    )

    class Meta:
        model = Article
        fields = ['rubric', 'hashtags']


class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
    """ Возвращает информацию об опубликованных статьях """
    queryset = Article.objects.filter(
        is_hidden=False,
        datetime_published__lte=timezone.now()
    )
    pagination_class = StandardPagination
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    filterset_class = ArticleFilter
    ordering_fields = ('release_date',)
    search_fields = ('name', 'short_description')

    def get_serializer_class(self):
        if self.action == 'list':
            return ArticleListSerializer
        return ArticleRetrieveSerializer


class BannerViewSet(viewsets.ReadOnlyModelViewSet):
    """ Возвращает информацию о баннерах """
    serializer_class = BannerSerializer
    queryset = Banner.objects.all().order_by('n_amongst_banners')
    filter_backends = (SearchFilter,)
    search_fields = ('article__name', 'article__short_description')


class PodcastViewSet(viewsets.ReadOnlyModelViewSet):
    """ Возвращает информацию о подкастах """
    queryset = Podcast.objects.all()
    serializer_class = PodcastSerializer
    pagination_class = None
    filter_backends = [SearchFilter, OrderingFilter]
    ordering_fields = ('date_of_last_issue_release',)
    search_fields = ('name', 'description')


class PodcastIssueViewSet(viewsets.ReadOnlyModelViewSet):
    """ Возвращает информацию об опубликованных выпусках определенного подкаста (по podcast_id) """
    serializer_class = PodcastIssueSerializer
    queryset = Podcast.objects.all()
    pagination_class = None
    filter_backends = [SearchFilter, OrderingFilter]
    ordering_fields = ('release_date', 'n_issue')
    search_fields = ('name', 'short_description')

    def get_queryset(self, *args, **kwargs):
        podcast_id = self.kwargs.get('pk')
        if podcast_id:
            queryset = PodcastIssue.objects.filter(podcast__id=podcast_id,
                                                   is_hidden=False).order_by('n_issue')
            return queryset
        return None


class ParticipantViewSet(viewsets.ReadOnlyModelViewSet):
    """ Возвращает информацию об участии в статьях определенного пользователя (по user_id) """
    serializer_class = ParticipantSerializer

    def get_queryset(self, *args, **kwargs):
        user_id = self.kwargs.get('pk')
        if user_id:
            queryset = (
                Participant.objects
                .filter(
                    user__id=user_id,
                    article__is_hidden=False,
                    article__datetime_published__lte=timezone.now(),
                ).order_by('article__release_date')
            )

            return queryset
        return None

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        def transform_data(input_data):
            transformed_data = []
            for item in input_data:
                article_info = item['article']
                role_info = item['role']['name']
                existing_article = next(
                    (article for article in transformed_data if article['article'] == article_info),
                    None
                )
                if existing_article:
                    existing_article['roles'].append(role_info)
                else:
                    transformed_data.append({'article': article_info, 'roles': [role_info]})
            return transformed_data

        return Response(transform_data(serializer.data))


class FavouriteViewSet(viewsets.ModelViewSet):
    """ Возвращает информацию об избранном пользователя. Аутентификация обязательна """
    serializer_class = FavouriteSerializer
    pagination_class = StandardPagination
    filter_backends = [SearchFilter]
    search_fields = ('content_object__name', 'content_object__short_description')
    permission_classes = (IsAuthenticated,)

    def get_queryset(self, *args, **kwargs):
        user_id = self.kwargs.get('pk')
        if user_id and str(self.request.user.id) == user_id:
            queryset = (
                Favourite.objects
                .filter(
                    user__id=user_id,
                    content_object__is_hidden=False,
                    content_object__datetime_published__lte=timezone.now(),
                )
                .order_by('content_object__release_date')
            )
            return queryset
        return Response({'detail': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)

    def create(self, request, *args, **kwargs):
        user_id = self.kwargs.get('pk')
        if str(request.user.id) == user_id:
            content_object_id = request.data.get('content_object')
            content_object = get_object_or_404(ContentObject, id=content_object_id)
            existing_favourite = Favourite.objects.filter(user=request.user, content_object=content_object).first()
            if existing_favourite:
                return Response({'detail': 'Object already exists in favorites'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                Favourite.objects.create(user=request.user, content_object=content_object)
                return Response({'detail': 'Favorite object created successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'detail': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)

    def destroy(self, request, *args, **kwargs):
        user_id = self.kwargs.get('pk')
        if str(request.user.id) == user_id:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response({'detail': 'Объект избранного успешно удален'}, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)


class PublicationViewSet(viewsets.ReadOnlyModelViewSet):
    """ Возвращает информацию обо всех публикациях на бумаге """
    queryset = Publication.objects.filter(
        is_hidden=False,
        datetime_published__lte=timezone.now()
    )
    serializer_class = PublicationSerializer
    pagination_class = StandardPagination
    filter_backends = [SearchFilter, OrderingFilter]
    ordering_fields = ('release_date',)
    search_fields = ('name', 'short_description')


class PublicationPageViewSet(viewsets.ReadOnlyModelViewSet):
    """ Возвращает информацию о страницах публикации """
    serializer_class = PublicationPageSerializer
    pagination_class = StandardPagination

    def get_queryset(self, *args, **kwargs):
        publication_id = self.kwargs.get('publication_id')
        if publication_id:
            queryset = (
                PublicationPage.objects
                .filter(
                    publication__id=publication_id,
                    publication__is_hidden=False,
                    publication__datetime_published__lte=timezone.now(),
                    ).order_by('n_amongst_pages')
            )
            return queryset
        return None


class NewtoneViewSet(viewsets.ReadOnlyModelViewSet):
    """ Возвращает информацию о журналах """
    queryset = Newtone.objects.filter(
        is_hidden=False,
        datetime_published__lte=timezone.now()
    )
    serializer_class = PublicationSerializer
    pagination_class = StandardPagination
    filter_backends = [SearchFilter, OrderingFilter]
    ordering_fields = ('release_date',)
    search_fields = ('name', 'short_description')


class NewspaperViewSet(viewsets.ReadOnlyModelViewSet):
    """ Возвращает информацию о газетах """
    queryset = Newspaper.objects.filter(
        is_hidden=False,
        datetime_published__lte=timezone.now()
    )
    serializer_class = PublicationSerializer
    pagination_class = StandardPagination
    filter_backends = [SearchFilter, OrderingFilter]
    ordering_fields = ('release_date',)
    search_fields = ('name', 'short_description')
