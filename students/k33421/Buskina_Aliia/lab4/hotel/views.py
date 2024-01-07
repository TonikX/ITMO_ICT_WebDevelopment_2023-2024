from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.urls import reverse
from django.views import View
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import date, datetime
from .models import *
from .serializers import *
from django.db.models import Count, Q, Prefetch
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect
from .forms import *
from rest_framework.permissions import AllowAny
class CheckinListView(generics.ListAPIView):
    permission_classes = (IsAuthenticated, IsAdminUser)
    serializer_class = CheckinSerializer

    def get_queryset(self):
        room_id = self.kwargs.get('room_id')
        start_date = self.kwargs.get('start_date')
        end_date = self.kwargs.get('end_date')

        # Проверьте, что room_id, start_date и end_date переданы в запросе
        if not (room_id and start_date and end_date):
            return Checkin.objects.none()

        # Преобразуйте даты из строки в объекты datetime
        start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
        end_date = datetime.strptime(end_date, '%Y-%m-%d').date()

        # Получите записи Checkin для заданного номера и периода времени
        queryset = Checkin.objects.filter(
            room_id=room_id,
            check_in_date__lte=end_date,
            check_out_date__gte=start_date
        )
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        data = []
        for item in queryset:
            checkin_data = {
                "id": item.id,
                "check_in_date": item.check_in_date,
                "check_out_date": item.check_out_date,
                "guest_id": item.guest_id.id,  # Assuming guest_id is a ForeignKey to the Guest model
                "room_id": item.room_id.id,
            }
            data.append(checkin_data)

        return JsonResponse(data, safe=False)

class GuestsFromCityView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated, IsAdminUser)
    serializer_class = GuestSerializer

    def get(self, request, *args, **kwargs):
        city = self.kwargs.get('city')

        # Получите количество клиентов из заданного города
        guests_count = Guest.objects.filter(hometown=city).count()

        # Отправьте ответ с количеством клиентов
        return Response({'guests_count': guests_count})


class CleanerForGuestView(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = CleaningSerializer

    def get(self, request, *args, **kwargs):
        guest_id = self.kwargs.get('guest_id')
        date = self.kwargs.get('date')

        try:
            cleaning_info = Cleaning.objects.filter(
                room_id__checkin__guest_id=guest_id,
                date_clean__date=date
            ).select_related('staff_id').first()

            if cleaning_info:
                serializer = self.serializer_class(cleaning_info)
                response_data = {
                    'cleaner': {
                        'name': cleaning_info.staff_id.name,
                        'surname': cleaning_info.staff_id.surname
                    }
                }
                return JsonResponse(response_data)
            else:
                return JsonResponse({'message': 'Cleaning information not found for the specified guest and date'})
        except Cleaning.DoesNotExist:
            return JsonResponse({'message': 'Cleaning information not found for the specified guest and date'})

class FreeRoomsView(generics.ListAPIView):
    permission_classes = (IsAuthenticated, IsAdminUser)
    serializer_class = FreeRoomsSerializer

    def get_queryset(self):
        date = self.kwargs.get('date')

        # Получите количество всех номеров в отеле
        total_rooms_count = Room.objects.count()

        # Получите количество занятых номеров для заданной даты
        occupied_rooms_count = Checkin.objects.filter(
            Q(check_in_date__lte=date) & Q(check_out_date__gte=date)
        ).count()

        # Вычтите из общего числа занятые номера
        free_rooms_count = total_rooms_count - occupied_rooms_count

        return [{'date': date, 'free_rooms_count': free_rooms_count}]


class RelatedGuestsListView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = RelatedGuestsListSerializer

    def get_queryset(self):
        guest_id = self.kwargs.get('guest_id')
        start_date = self.kwargs.get('start_date')
        end_date = self.kwargs.get('end_date')

        # Получите список клиентов с указанием места жительства,
        # которые проживали в те же дни, что и заданный клиент, в определенный период времени
        related_guests = Checkin.objects.filter(
            guest_id=guest_id,
            check_in_date__range=[start_date, end_date]
        ).values_list('check_in_date', flat=True)

        return [{
            'date': date,
            'guests': Guest.objects.filter(
                Q(checkin__check_in_date=date) & ~Q(checkin__guest_id=guest_id)
            ).values('id', 'name', 'surname', 'hometown')
        } for date in related_guests]


class RelatedGuestsListView(generics.ListAPIView):
    permission_classes = (IsAuthenticated, IsAdminUser)
    serializer_class = RelatedGuestsListSerializer

    def get_queryset(self):
        guest_id = self.kwargs.get('guest_id')
        start_date = self.kwargs.get('start_date')
        end_date = self.kwargs.get('end_date')

        # Получите список клиентов с указанием места жительства,
        # которые проживали в те же дни, что и заданный клиент, в определенный период времени
        related_guests = Checkin.objects.filter(
            guest_id=guest_id,
            check_in_date__range=[start_date, end_date]
        ).values_list('check_in_date', flat=True)

        return [{
            'date': date,
            'guests': Guest.objects.filter(
                Q(checkin__check_in_date=date) & ~Q(checkin__guest_id=guest_id)
            ).values('id', 'name', 'surname', 'hometown')
        } for date in related_guests]


class HotelReportView(APIView):
    permission_classes = [AllowAny]
    def get(self, request, start_date, end_date, *args, **kwargs):
        # Получаем данные о клиентах за указанный период в каждом номере
        reports = Checkin.objects.filter(
            check_in_date__range=[start_date, end_date]
        ).values(
            'room_id',
            'room_id__floor',
            'room_id__type',
        ).annotate(
            guests_count=Count('guest_id', distinct=True),
        ).order_by('room_id')

        # Получаем количество номеров на каждом этаже
        floor_counts = Room.objects.values('floor').annotate(room_count=Count('id'))

        # Вычисляем общую сумму дохода за каждый номер
        for report in reports:
            checkin = Checkin.objects.filter(room_id=report['room_id'], check_in_date__range=[start_date, end_date]).first()
            if checkin:
                report['room_income'] = checkin.income
            else:
                report['room_income'] = None

        # Вычисляем суммарный доход по всей гостинице
        total_income = sum(report['room_income'] for report in reports if report['room_income'] is not None)

        # Сериализация и возврат данных в формате JSON
        response_data = {
            'reports': list(reports),
            'floor_counts': list(floor_counts),
            'total_income': total_income,
        }
        return JsonResponse(response_data)

class HireStaffView(View):
    permission_classes = (IsAuthenticated, IsAdminUser)
    template_name = 'hire_staff.html'

    def get(self, request, *args, **kwargs):
        form = HireStaffForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = HireStaffForm(request.POST)
        if form.is_valid():
            form.save()
            # Редирект, если успешно
            return HttpResponseRedirect(reverse('hire_staff.html'))
        return render(request, self.template_name, {'form': form})

class FireStaffView(View):
    permission_classes = (IsAuthenticated, IsAdminUser)
    template_name = 'fire_staff.html'

    def get(self, request, *args, **kwargs):
        form = FireStaffForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = FireStaffForm(request.POST)
        if form.is_valid():
            staff_id = form.cleaned_data['staff_id'].id
            staff = Staff.objects.get(pk=staff_id)
            staff.delete()
            return redirect('success_page')  # Перенаправьте на страницу успеха

        return render(request, self.template_name, {'form': form})

class AddCleaningView(View):
    permission_classes = (IsAuthenticated, IsAdminUser)
    template_name = 'add_cleaning.html'
    form_class = AddCleaningForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            # Перенаправьте на нужный URL после успешного добавления уборки
            return redirect('success_url')
        return render(request, self.template_name, {'form': form, 'error': 'Invalid form submission'})

class DeleteCleaningView(View):
    permission_classes = (IsAuthenticated, IsAdminUser)
    template_name = 'delete_cleaning.html'
    form_class = DeleteCleaningForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            cleaning = form.cleaned_data['cleaning']
            cleaning.delete()
            # Перенаправьте на нужный URL после успешного удаления уборки
            return redirect('success_url')
        return render(request, self.template_name, {'form': form, 'error': 'Invalid form submission'})

class CheckinView(View):
    permission_classes = (IsAuthenticated, IsAdminUser)
    template_name = 'checkin.html'
    form_class = CheckinForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            # Перенаправьте на нужный URL после успешного поселения клиента
            return redirect('success_url')
        return render(request, self.template_name, {'form': form, 'error': 'Invalid form submission'})


class CheckoutView(View):
    permission_classes = (IsAuthenticated, IsAdminUser)
    template_name = 'checkout.html'
    form_class = CheckoutForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            checkin = form.cleaned_data['checkin']

            # Вы можете использовать checkin напрямую вместо checkin_id
            checkin.delete()

            # Перенаправьте на нужный URL после успешного выселения клиента
            return redirect('success_url')

        return render(request, self.template_name, {'form': form, 'error': 'Invalid form submission'})


class GuestCreateView(View):
    template_name = 'create_guest.html'
    form_class = GuestForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            # Перенаправьте на нужный URL после успешного добавления гостя
            return redirect('success_url')

        return render(request, self.template_name, {'form': form, 'error': 'Invalid form submission'})

class RoomWithGuestListView(generics.ListAPIView):
    serializer_class = RoomWithGuestSerializer
    queryset = Room.objects.all()