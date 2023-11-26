from django.contrib.postgres.aggregates import ArrayAgg
from django.db.models import Count
from django.utils import timezone
from rest_framework import serializers
from rest_framework.generics import get_object_or_404

from .models import *
from djoser.serializers import UserCreateSerializer


class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)

        # Instantiate the superclass normally
        super().__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class WhatWeDoSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = WhatWeDo
        fields = '__all__'


class RubricSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Rubric
        fields = '__all__'


class HashtagSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Hashtag
        fields = '__all__'


class HashtagsSerializer(DynamicFieldsModelSerializer):
    hashtag = HashtagSerializer()

    class Meta:
        model = Hashtags
        fields = '__all__'


class PlatformSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Platform
        fields = '__all__'


class PodcastLinkSerializer(DynamicFieldsModelSerializer):
    platform = PlatformSerializer()

    class Meta:
        model = PodcastLink
        fields = ['platform', 'external_reference_link']


class PodcastIssueSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = PodcastIssue
        exclude = ['datetime_published', 'is_hidden', 'polymorphic_ctype', 'podcast']


class PodcastSerializer(serializers.ModelSerializer):
    issues_count = serializers.SerializerMethodField(source='get_issues_count')
    date_of_last_issue_release = serializers.SerializerMethodField(source='date_of_last_issue_release')
    podcast_links = serializers.SerializerMethodField(source='get_podcast_links')

    class Meta:
        model = Podcast
        fields = ['id', 'name', 'description', 'cover_picture', 'issues_count', 'date_of_last_issue_release',
                  'podcast_links']

    def get_issues_count(self, obj):
        return obj.issues_count

    def get_date_of_last_issue_release(self, obj):
        last_issue = obj.podcast_issues.last()
        return last_issue.release_date if last_issue else None

    def get_podcast_links(self, obj):
        links = PodcastLink.objects.filter(podcast=obj)
        links_serializer = PodcastLinkSerializer(links, fields=['platform', 'external_reference_link'], many=True)
        return links_serializer.data


class UserSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'full_name']


class ContentObjectSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = ContentObject
        fields = ["id", "name", "short_description", "cover_picture", "release_date"]


class FavouriteSerializer(DynamicFieldsModelSerializer):
    content_object = ContentObjectSerializer()

    class Meta:
        model = Favourite
        fields = ['id', 'content_object']


class FavouriteCreateSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = Favourite
        fields = ['id', 'content_object']

    def create(self, validated_data):
        content_object = validated_data.pop('content_object')
        content_object = get_object_or_404(ContentObject, id=content_object)
        favourite = Favourite.objects.create(content_object=content_object)
        return favourite


class ArticleListSerializer(DynamicFieldsModelSerializer):
    rubric = serializers.StringRelatedField(source='rubric.name')
    article_hashtags = serializers.SerializerMethodField(source='get_article_hashtags')

    class Meta:
        model = Article
        fields = ['id', 'name', 'cover_picture', 'short_description', 'rubric', 'release_date', 'article_hashtags']

    def get_article_hashtags(self, obj):
        hashtags = Hashtags.objects.filter(article=obj)
        return [hashtag.hashtag.name for hashtag in hashtags]


class ArticleRetrieveSerializer(DynamicFieldsModelSerializer):
    rubric = serializers.StringRelatedField(source='rubric.name')
    article_hashtags = serializers.SerializerMethodField(source='get_article_hashtags')
    article_participants = serializers.SerializerMethodField(source='get_article_participants')

    class Meta:
        model = Article
        exclude = ['is_hidden', 'polymorphic_ctype', 'datetime_published']

    def get_article_participants(self, obj):
        participants = Participant.objects.filter(article=obj)
        participant_serializer = ParticipantSerializer(participants, fields=['id', 'user', 'role'], many=True)
        return [{'user': item['user'], 'role': item['role']['name']} for item in
                participant_serializer.data]  # TODO: figure out a way to add user-related link

    def get_article_hashtags(self, obj):
        hashtags = Hashtags.objects.filter(article=obj)
        return [hashtag.hashtag.name for hashtag in hashtags]


class BannerSerializer(DynamicFieldsModelSerializer):
    article = ArticleListSerializer()
    cover_picture = serializers.SerializerMethodField(source='get_cover_picture')

    class Meta:
        model = Banner
        exclude = ['special_cover_picture']

    def get_cover_picture(self, obj):
        if obj.special_cover_picture:
            return self.context['request'].build_absolute_uri(obj.special_cover_picture.url)
        elif obj.article and obj.article.cover_picture:
            return self.context['request'].build_absolute_uri(obj.article.cover_picture.url)
        return None


class RoleSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'


class ParticipantSerializer(DynamicFieldsModelSerializer):
    role = RoleSerializer()
    article = ArticleListSerializer()

    class Meta:
        model = Participant
        fields = ['id', 'article', 'role']


class PublicationSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Publication
        fields = ['id', 'name', 'cover_picture', 'short_description', 'release_date',
                  'attached_file', 'external_reference_link']


class PublicationPageSerializer(DynamicFieldsModelSerializer):
    article = ArticleListSerializer()

    class Meta:
        model = PublicationPage
        fields = ['id', 'article', 'n_amongst_pages', 'attached_page_file']
