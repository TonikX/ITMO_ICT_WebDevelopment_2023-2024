from rest_framework import serializers
from .models import User, Task, Comment, Aim, Category, TaskUserRelation


class CommentSerializer(serializers.ModelSerializer):
    user_name = serializers.ReadOnlyField(source='user.username')
    task_title = serializers.ReadOnlyField(source='task_user_relation.task.title')

    class Meta:
        model = Comment
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name')
    aim_title = serializers.CharField(source='aim.title')

    class Meta:
        model = Task
        fields = '__all__'


class TaskUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['completed']

class AimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aim
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class TaskDetailSerializer(serializers.ModelSerializer):
    aim = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = ['id', 'aim', 'category', 'title', 'description', 'deadline', 'completed']

    def get_aim(self, obj):
        return obj.aim.title if obj.aim else None

    def get_category(self, obj):
        return obj.category.name if obj.category else None


class TaskUserRelationSerializer(serializers.ModelSerializer):
    task_title = serializers.ReadOnlyField(source='task.title')
    user_name = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = TaskUserRelation
        fields = '__all__'

