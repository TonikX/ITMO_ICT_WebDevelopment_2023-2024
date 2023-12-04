from rest_framework import serializers
from . import models


class SubPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Person
        fields = [
            'id',
            'username',
        ]


class FriendsSerializer(serializers.ModelSerializer):
    #toPersonID_id = SubPersonSerializer()
    #fromPersonID_id = SubPersonSerializer()
    class Meta:
        model = models.FriendShip
        fields = [
            'id',
            'toPersonID_id',
            'fromPersonID_id',
            'sendDate',
            'status',
            'approvedDate',
        ]


class PersonSerializer(serializers.ModelSerializer):
    friends = SubPersonSerializer(many=True)

    class Meta:
        model = models.Person
        fields = [
            'id',
            'username',
            'password',
            'last_login',
            'is_superuser',
            'first_name',
            'last_name',
            'date_joined',
            'email',
            'lastUpdate',
            'capCount',
            'birthDate',
            'friends'
        ]


class VaultFilesSerializer(serializers.ModelSerializer):
    file = serializers.SerializerMethodField(method_name='get_file_name')

    def get_file_name(self, obj):
        return '{}.{}'.format(obj.filename, obj.extension)

    class Meta:
        model = models.File
        fields = [
            'file',
        ]


class SimpleVaultSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vault
        fields = [
            'id',
            'name',
            'description',
        ]


class FileSerializer(serializers.ModelSerializer):
    vault_id = serializers.IntegerField(source='vault.id')

    class Meta:
        model = models.File
        fields = [
            'id',
            'vault_id',
            'filename',
            'extension',
            'path',
        ]


class VaultAccessSerializer(serializers.ModelSerializer):
    vault_id = serializers.IntegerField(source='vault.id')
    person_id = serializers.IntegerField(source='person.id')

    class Meta:
        model = models.VaultAccess
        fields = [
            'vault_id',
            'person_id',
            'permissions',
        ]


'''
class VaultAccessSerializer(serializers.ModelSerializer):
    #person = SubPersonSerializer()

    class Meta:
        model = models.VaultAccess
        fields = [
            'id',
            'permissions',
        ]
'''


class VaultSerializer(serializers.ModelSerializer):
    owner = SubPersonSerializer()
    customAccessList = SubPersonSerializer(many=True)
    files = VaultFilesSerializer(source='file_set', many=True)

    class Meta:
        model = models.Vault
        fields = [
            'id',
            'name',
            'description',
            'cDate',
            'eDate',
            'owner',
            'access',
            'customAccessList',
            'text',
            'files'
        ]


class SubCommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comments
        fields = [
            'id',
        ]


class CommentsSerializer(serializers.ModelSerializer):
    person = SubPersonSerializer()
    vault = SimpleVaultSerializer()
    mainComment = SubCommentsSerializer()
    subComments = SubCommentsSerializer(many=True)

    class Meta:
        model = models.Comments
        fields = [
            'person',
            'vault',
            'id',
            'commentText',
            'commentDate',
            'mainComment',
            'subComments',
        ]


class PersonCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Person
        fields = [
            'username',
            'password',
            'email',
        ]


class VaultCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vault
        exclude = [
            'cDate',
        ]


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comments
        exclude = [
            'commentDate',
            'subComments',
        ]


class FileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.File
        fields = '__all__'


class AccessCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.VaultAccess
        fields = '__all__'


class FriendShipCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FriendShip
        fields = [
            'fromPersonID',
            'toPersonID'
        ]