from rest_framework import generics

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


class NewspaperPrintingHouseSearchView(generics.ListAPIView):
    """
    Эндпоинт для поиска типографий, где печатается газета с указанным ID.
    """
    serializer_class = NewspaperSerializer

    def get_queryset(self):
        newspaper_id = self.kwargs['id']
        return Newspaper.objects.filter(id=newspaper_id).first().printrun_set.all()


class PrintingHouseChiefEditorView(generics.RetrieveAPIView):
    """
    Эндпоинт для получения фамилии редактора газеты с самым большим тиражом в указанной типографии.
    """
    serializer_class = NewspaperSerializer

    def get_queryset(self):
        printing_house_id = self.kwargs['id']
        return PrintingHouse.objects.filter(id=printing_house_id).first().printrun_set.all()


class NewspaperPriceGreaterPostOfficesView(generics.ListAPIView):
    """
    Эндпоинт для поиска почтовых отделений, куда поступает газета с ценой выше указанной.
    """
    serializer_class = NewspaperSerializer

    def get_queryset(self):
        price = self.kwargs['price']
        return Newspaper.objects.filter(price_per_copy__gt=price).first().postalarrival_set.all()


class NewspaperCopiesLessDestinationsView(generics.ListAPIView):
    """
    Эндпоинт для поиска газет и их мест назначения с количеством экземпляров меньше указанного.
    """
    serializer_class = NewspaperSerializer

    def get_queryset(self):
        count = self.kwargs['count']
        return Newspaper.objects.filter(printrun__copies_count__lt=count)


class NewspaperPrintingHouseDestinationView(generics.ListAPIView):
    """
    Эндпоинт для получения информации о том, куда поступает газета, печатающаяся по указанному адресу типографии.
    """
    serializer_class = NewspaperSerializer

    def get_queryset(self):
        newspaper_id = self.kwargs['newspaper_id']
        printing_house_id = self.kwargs['printing_house_id']
        return Newspaper.objects.filter(id=newspaper_id,
                                        printrun__printing_house_id=printing_house_id).first().postalarrival_set.all()
