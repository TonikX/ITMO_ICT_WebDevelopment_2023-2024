##Представления


UserCreateView - это представление для регистрации новых пользователей.
Используется форма UserCreationForm из django.contrib.auth.forms для обработки создания нового пользователя.
После успешной регистрации, пользователь автоматически входит в систему с помощью auth_login.
success_url указывает, куда перенаправить пользователя после успешной регистрации.

ViewSet и DetailView для моделей:

Для каждой из моделей (Airplane, Flight, CrewMember, TransitStop, Employee) я создала два вида: ViewSet и DetailView.
ViewSet предоставляет стандартные CRUD операции для модели.
DetailView предоставляет дополнительные возможности для просмотра, обновления и удаления конкретного экземпляра модели.
Для каждой модели указываем соответствующий queryset и serializer_class для использования в представлении.

Serializer:

Для каждой модели есть соответствующий класс сериализатора (AirplaneSerializer, FlightSerializer, CrewMemberSerializer, TransitStopSerializer, EmployeeSerializer).



    from rest_framework import generics, viewsets
    from .models import Airplane, Flight, CrewMember, TransitStop, Employee
    from .serializers import AirplaneSerializer, FlightSerializer, CrewMemberSerializer, TransitStopSerializer, \
        EmployeeSerializer
    from django.contrib.auth.forms import UserCreationForm
    from django.contrib.auth import login as auth_login
    from django.views.generic.edit import FormView
    from django.urls import reverse_lazy
    from django.http import HttpResponseRedirect
    
    
    class UserCreateView(FormView):
        template_name = 'register.html'
        form_class = UserCreationForm
        success_url = reverse_lazy('token_create')
    
        def form_valid(self, form):
            user = form.save()
            auth_login(self.request, user)
            return HttpResponseRedirect(self.get_success_url())
    
    
    class AirplaneViewSet(viewsets.ModelViewSet):
        queryset = Airplane.objects.all()
        serializer_class = AirplaneSerializer
    
    
    class AirplaneDetailView(generics.RetrieveUpdateDestroyAPIView):
        queryset = Airplane.objects.all()
        serializer_class = AirplaneSerializer
    
    
    class FlightViewSet(viewsets.ModelViewSet):
        queryset = Flight.objects.all()
        serializer_class = FlightSerializer
    
    
    class FlightDetailView(generics.RetrieveUpdateDestroyAPIView):
        queryset = Flight.objects.all()
        serializer_class = FlightSerializer
    
    
    class CrewMemberViewSet(viewsets.ModelViewSet):
        queryset = CrewMember.objects.all()
        serializer_class = CrewMemberSerializer
    
    
    class CrewMemberDetailView(generics.RetrieveUpdateDestroyAPIView):
        queryset = CrewMember.objects.all()
        serializer_class = CrewMemberSerializer
    
    
    class TransitStopViewSet(viewsets.ModelViewSet):
        queryset = TransitStop.objects.all()
        serializer_class = TransitStopSerializer
    
    
    class TransitStopDetailView(generics.RetrieveUpdateDestroyAPIView):
        queryset = TransitStop.objects.all()
        serializer_class = TransitStopSerializer
    
    
    class EmployeeViewSet(viewsets.ModelViewSet):
        queryset = Employee.objects.all()
        serializer_class = EmployeeSerializer
    
    
    class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
        queryset = Employee.objects.all()
        serializer_class = EmployeeSerializer
