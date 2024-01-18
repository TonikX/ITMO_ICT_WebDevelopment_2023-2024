from rest_framework import serializers
from projects.models import File, ProjectTopic, Project, GradeReport, \
ProjectOfUser, Teacher, Student, Grade, ProjectMeeting, Meeting, User, ProjectVote

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

class UserSerializerManual(DynamicFieldsModelSerializer):
  class Meta:
     model = User
     fields = ['id', 'name']

class FileSerializer(serializers.ModelSerializer):
  class Meta:
     model = File
     fields = "__all__"

class ProjectTopicSerializer(serializers.ModelSerializer):
  class Meta:
     model = ProjectTopic
     fields = "__all__"

class ProjectTopicSerializerManual(DynamicFieldsModelSerializer):
  class Meta:
     model = ProjectTopic
     fields = ['id', 'name']

class ProjectSerializerManual(DynamicFieldsModelSerializer):
  class Meta:
    model = Project
    fields = ['id', 'name', 'created', 'updated', 'creator', 'description', 'start_date', 'end_date', 'topics']

class ProjectSerializerSafe(serializers.Serializer):
  id = serializers.IntegerField()
  name = serializers.CharField(max_length=200)
  created = serializers.DateTimeField()
  updated = serializers.DateTimeField()
  creator = UserSerializerManual() # UserSerializerManual()
  description = serializers.CharField(max_length=2000)
  start_date = serializers.DateTimeField()
  end_date = serializers.DateTimeField()
  topics = ProjectTopicSerializerManual(many=True)


class ProjectSerializer(serializers.ModelSerializer):
  class Meta:
     model = Project
     fields = "__all__"

class ProjectVoteSerializerSafe(serializers.Serializer):
  id = serializers.IntegerField()
  name = serializers.CharField(max_length=200)
  user_field = UserSerializerManual()
  project_field = ProjectSerializerSafe()

class ProjectDepthSerializer(serializers.ModelSerializer):
  class Meta:
    model = Project
    fields = "__all__"

    depth = 1

class GradeReportSerializer(serializers.ModelSerializer):
  class Meta:
    model = GradeReport
    fields = "__all__"

class GradeReportDepthSerializer(serializers.ModelSerializer):
  class Meta:
    model = GradeReport
    fields = "__all__"

    depth = 1

class ProjectOfUserSerializer(serializers.ModelSerializer):
  class Meta:
    model = ProjectOfUser
    fields = "__all__"

# !!!!!!
    
# class ProjectOfUserSerializerSafe(serializers.ModelSerializer):
#   class Meta:
#     model = ProjectOfUser
#     fields = "__all__"
  
#   def validate_user_field(self, value):
#       return value.name

class ProjectOfUserSerializerSafe(serializers.Serializer):
  # email = serializers.EmailField()
  # content = serializers.CharField(max_length=200)
  # created = serializers.DateTimeField()
  id = serializers.IntegerField()
  name = serializers.CharField(max_length=200)
  created = serializers.DateTimeField()
  updated = serializers.DateTimeField()
  creator = UserSerializerManual(required=False, fields=('id'))
  # creator = serializers.ForeignKey(User, on_delete=models.SET_NULL, null=True)

  project_field = ProjectSerializerManual(required=False)

  # def get_project_field(self, projectOfUser):
  #       return ProjectSerializer(projectOfUser.project_field).data
  
  user_field = UserSerializerManual(required=False, fields=('id', 'name'))

  def get_user_field(self, value):
        return value.name
  
  def get_project_field(self, value):
        return value.id
  
  # def to_representation(self, instance):
  #       return {
  #           'name': instance.name,
  #           'created': instance.created,
  #           'updated': instance.updated,
  #           # 'project_field': instance.project_field,
  #           'user_field': instance.user_field,
  #       }

class ProjectOfUserDepthSerializer(serializers.ModelSerializer):
  class Meta:
    model = ProjectOfUser
    fields = "__all__"

    depth = 1

class TeacherSerializer(serializers.ModelSerializer): 
  class Meta:
    model = Teacher
    fields = "__all__"

class TeacherDepthSerializer(serializers.ModelSerializer): 
  class Meta:
    model = Teacher
    fields = "__all__"

    depth = 1

class StudentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Student
    fields = "__all__"

class StudentDepthSerializer(serializers.ModelSerializer):
  class Meta:
    model = Student
    fields = "__all__"

    depth = 1

class GradeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Grade
    fields = "__all__"

class GradeDepthSerializer(serializers.ModelSerializer):
  class Meta:
    model = Grade
    fields = "__all__" 

    depth = 1

class ProjectMeetingSerializer(serializers.ModelSerializer):
  class Meta:
    model = ProjectMeeting
    fields = "__all__"

class ProjectMeetingDepthSerializer(serializers.ModelSerializer):
  class Meta:
    model = ProjectMeeting
    fields = "__all__"

    depth = 1

class MeetingSerializer(serializers.ModelSerializer):
  class Meta:
    model = Meeting
    fields = "__all__"

class MeetingDepthSerializer(serializers.ModelSerializer):
  class Meta:
    model = Meeting
    fields = "__all__"

    depth = 1