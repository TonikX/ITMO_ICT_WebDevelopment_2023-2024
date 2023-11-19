from django.db.models import Max
from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Newspaper, PrintingHouse, Editor, PrintRun, PostOffice, PostalArrival
from .serializers import NewspaperSerializer, PrintingHouseSerializer, EditorSerializer, PrintRunSerializer, \
    PostOfficeSerializer, PostalArrivalSerializer


class NewspaperListCreateView(generics.ListCreateAPIView):
    """
    Эндпоинт для получения списка всех газет и создания новой газеты.
    """
    queryset = Newspaper.objects.all()
    serializer_class = NewspaperSerializer


class NewspaperRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    Эндпоинт для получения, обновления и удаления информации о конкретной газете.
    """
    queryset = Newspaper.objects.all()
    serializer_class = NewspaperSerializer


class PrintingHouseListCreateView(generics.ListCreateAPIView):
    """
    Эндпоинт для получения списка всех типографий и создания новой типографии.
    """
    queryset = PrintingHouse.objects.all()
    serializer_class = PrintingHouseSerializer


class PrintingHouseRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    Эндпоинт для получения, обновления и удаления информации о конкретной типографии.
    """
    queryset = PrintingHouse.objects.all()
    serializer_class = PrintingHouseSerializer


class EditorListCreateView(generics.ListCreateAPIView):
    """
    Эндпоинт для получения списка всех редакторов и создания нового редактора.
    """
    queryset = Editor.objects.all()
    serializer_class = EditorSerializer


class EditorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    Эндпоинт для получения, обновления и удаления информации о конкретном редакторе.
    """
    queryset = Editor.objects.all()
    serializer_class = EditorSerializer


class PrintRunListCreateView(generics.ListCreateAPIView):
    """
    Эндпоинт для получения списка всех тиражей и создания нового тиража.
    """
    queryset = PrintRun.objects.all()
    serializer_class = PrintRunSerializer


class PrintRunRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    Эндпоинт для получения, обновления и удаления информации о конкретном тираже.
    """
    queryset = PrintRun.objects.all()
    serializer_class = PrintRunSerializer


class PostOfficeListCreateView(generics.ListCreateAPIView):
    """
    Эндпоинт для получения списка всех почтовых отделений и создания нового почтового отделения.
    """
    queryset = PostOffice.objects.all()
    serializer_class = PostOfficeSerializer


class PostOfficeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    Эндпоинт для получения, обновления и удаления информации о конкретном почтовом отделении.
    """
    queryset = PostOffice.objects.all()
    serializer_class = PostOfficeSerializer


class PostalArrivalListCreateView(generics.ListCreateAPIView):
    """
    Эндпоинт для получения списка всех почтовых поступлений и создания нового почтового поступления.
    """
    queryset = PostalArrival.objects.all()
    serializer_class = PostalArrivalSerializer


class PostalArrivalRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    Эндпоинт для получения, обновления и удаления информации о конкретном почтовом поступлении.
    """
    queryset = PostalArrival.objects.all()
    serializer_class = PostalArrivalSerializer


class PrintingHouseAddressesView(APIView):
    """
    Эндпоинт для поиска типографий, где печатается газета с указанным именем
    """

    def get(self, request, *args, **kwargs):
        newspaper_name = request.data.get('newspaper_name', None)

        if newspaper_name is None:
            return Response({'error': 'Newspaper name is required in the request body'},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            newspaper = get_object_or_404(Newspaper, name=newspaper_name)
            print_runs = PrintRun.objects.filter(newspaper=newspaper)
            printing_house_addresses = [run.printing_house.address for run in print_runs]

            response_data = {
                'newspaper_name': newspaper.name,
                'printing_house_addresses': printing_house_addresses
            }

            return Response(response_data)
        except Newspaper.DoesNotExist:
            return Response({'error': 'Newspaper not found'}, status=status.HTTP_404_NOT_FOUND)


class MaxPrintRunEditorView(APIView):
    """
       Эндпоинт для получения фамилии редактора газеты с самым большим тиражом в указанной типографии.
    """

    def get(self, request, *args, **kwargs):
        printing_house_name = request.data.get('printing_house_name', None)

        if printing_house_name is None:
            return Response({'error': 'Printing house name is required in the request body'},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            printing_house = get_object_or_404(PrintingHouse, name=printing_house_name)
            max_print_run = PrintRun.objects.filter(printing_house=printing_house).aggregate(Max('copies_count'))

            if max_print_run['copies_count__max'] is not None:
                newspaper_with_max_print_run = PrintRun.objects.filter(printing_house=printing_house,
                                                                       copies_count=max_print_run[
                                                                           'copies_count__max']).first()
                editor_last_name = newspaper_with_max_print_run.newspaper.editor.last_name

                response_data = {
                    'printing_house_name': printing_house.name,
                    'editor_last_name': editor_last_name,
                    'max_copies_count': max_print_run['copies_count__max']
                }

                return Response(response_data)
            else:
                return Response({'error': 'No print runs found for the specified printing house'},
                                status=status.HTTP_404_NOT_FOUND)

        except PrintingHouse.DoesNotExist:
            return Response({'error': 'Printing house not found'}, status=status.HTTP_404_NOT_FOUND)


class PostOfficeAddressesView(APIView):
    """
        Эндпоинт для поиска почтовых отделений, куда поступает газета с ценой выше указанной.
    """

    def get(self, request, *args, **kwargs):
        try:
            price_threshold = request.data.get('price_threshold', None)

            if price_threshold is None:
                return Response({'error': 'Price threshold is required in the request body'},
                                status=status.HTTP_400_BAD_REQUEST)

            newspapers_above_threshold = Newspaper.objects.filter(price_per_copy__gt=price_threshold)
            postal_arrivals = PostalArrival.objects.filter(newspaper__in=newspapers_above_threshold)
            post_office_addresses = [arrival.post_office.address for arrival in postal_arrivals]

            response_data = {
                'price_threshold': price_threshold,
                'post_office_addresses': post_office_addresses
            }

            return Response(response_data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UnderstockedNewspapersView(APIView):
    """
    Эндпоинт для поиска газет и их мест назначения с количеством экземпляров меньше указанного.
    """

    def get(self, request, *args, **kwargs):
        copies_threshold = request.data.get('copies_threshold', None)

        if copies_threshold is None:
            return Response({'error': 'Copies threshold is required as a query parameter'},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            copies_threshold = int(copies_threshold)
        except ValueError:
            return Response({'error': 'Copies threshold must be an integer'}, status=status.HTTP_400_BAD_REQUEST)

        understocked_arrivals = PostalArrival.objects.filter(copies_received__lt=copies_threshold)
        response_data = []

        for arrival in understocked_arrivals:
            arrival_info = {
                'newspaper_name': arrival.newspaper.name,
                'copies_received': arrival.copies_received,
                'post_office_number': arrival.post_office.number
            }
            response_data.append(arrival_info)

        return Response(response_data)


class NewspaperArrivalView(APIView):
    """
       Эндпоинт для получения информации о том, куда поступает газета, печатающаяся по указанному адресу типографии.
    """
    def get(self, request, *args, **kwargs):
        printing_house_address = request.data.get('printing_house_address', None)

        if printing_house_address is None:
            return Response({'error': 'Printing house address is required in the request body'},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            print_run = get_object_or_404(PrintRun, printing_house__address=printing_house_address)
            newspaper_arrivals = PostalArrival.objects.filter(newspaper=print_run.newspaper)

            arrival_info = [{
                'post_office_number': arrival.post_office.number,
                'copies_received': arrival.copies_received
            } for arrival in newspaper_arrivals]

            response_data = {
                'newspaper_name': print_run.newspaper.name,
                'printing_house_address': printing_house_address,
                'newspaper_arrivals': arrival_info
            }

            return Response(response_data)
        except PrintRun.DoesNotExist:
            return Response({'error': 'Printing house not found'}, status=status.HTTP_404_NOT_FOUND)
