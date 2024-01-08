from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.generics import get_object_or_404

from LR1_secondApp.serializers import *


class DisksS(APIView):
    permission_classes = [permissions.AllowAny, ]

    def get(self, request, pk=None):
        diskS = Disks.objects.all()
        if pk is not None:
            diskS = Disks.objects.filter(pk=pk)
        serializerDis = DisksSerializers(diskS, many=True)
        return Response({"data": serializerDis.data})

    def post(self, request):
        diskPost = DisksSerializers(data=request.data)
        if diskPost.is_valid():
            diskPost.save()
            return Response(status=201)
        else:
            return Response(status=400)

    def put(self, request, pk):
        saved_diskP = get_object_or_404(Disks.objects.all(), pk=pk)
        data = request.data
        serializer = DisksSerializers(instance=saved_diskP, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201)
        else:
            return Response(status=400)

    def delete(self, request, pk):
        diskP = get_object_or_404(Disks.objects.all(), pk=pk)
        diskP.delete()
        return Response(status=204)


class GamesS(APIView):
    permission_classes = [permissions.AllowAny, ]

    def get(self, request, pk=None):
        gamesS = Games.objects.all()
        if pk is not None:
            gamesS = Games.objects.filter(pk=pk)
            serializerGam = GamesSerializers(gamesS, many=True)
            disksS = Disks.objects.filter(id=Games.objects.values_list('id', flat=True).get(pk=pk))
            serializerDisks = DisksSerializers(disksS, many=True)
            return Response({"data": serializerGam.data, "disks": serializerDisks.data})
        serializerGam = GamesSerializers(gamesS, many=True)
        return Response({"data": serializerGam.data})

    def post(self, request):
        gamePost = GamesSerializers(data=request.data)
        if gamePost.is_valid():
            gamePost.save()
            return Response(status=201)
        else:
            return Response(status=400)

    def put(self, request, pk):
        saved_gameP = get_object_or_404(Games.objects.all(), pk=pk)
        data = request.data
        serializer = GamesSerializers(instance=saved_gameP, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201)
        else:
            return Response(status=400)

    def delete(self, request, pk):
        gameP = get_object_or_404(Games.objects.all(), pk=pk)
        gameP.delete()
        return Response(status=204)


class SaleS(APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request, pk=None):
        saleS = Sale.objects.all()
        if pk is not None:
            saleS = Sale.objects.filter(pk=pk)
            serializerSal = SaleSerializers(saleS, many=True)
            disksS = Disks.objects.filter(id=Sale.objects.values_list('id', flat=True).get(pk=pk))
            serializerDisks = DisksSerializers(disksS, many=True)
            return Response({"data": serializerSal.data, "disks": serializerDisks.data})
        serializerSal = SaleSerializers(saleS, many=True)
        return Response({"data": serializerSal.data})

    def post(self, request):
        salePost = SaleSerializers(data=request.data)
        if salePost.is_valid():
            salePost.save()
            return Response(status=201)
        else:
            return Response(status=400)

    def put(self, request, pk):
        saved_saleP = get_object_or_404(Sale.objects.all(), pk=pk)
        data = request.data
        serializer = SaleSerializers(instance=saved_saleP, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201)
        else:
            return Response(status=400)

    def delete(self, request, pk):
        saleP = get_object_or_404(Sale.objects.all(), pk=pk)
        saleP.delete()
        return Response(status=204)


class AdmissionS(APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request, pk=None):
        admissionS = Admission.objects.all()
        if pk is not None:
            admissionS = Admission.objects.filter(pk=pk)
            serializerAdm = AdmissionSerializers(admissionS, many=True)
            disksS = Disks.objects.filter(id=Admission.objects.values_list('id', flat=True).get(pk=pk))
            serializerDisks = DisksSerializers(disksS, many=True)
            return Response({"data": serializerAdm.data, "disks": serializerDisks.data})
        serializerAdm = AdmissionSerializers(admissionS, many=True)
        return Response({"data": serializerAdm.data})

    def post(self, request):
        # return Response({"data": request.data})
        admissionPost = AdmissionSerializers(data=request.data)
        if admissionPost.is_valid():
            admissionPost.save()
            return Response(status=201)
        else:
            return Response(status=400)

    def put(self, request, pk):
        saved_admissionP = get_object_or_404(Admission.objects.all(), pk=pk)
        data = request.data
        serializer = AdmissionSerializers(instance=saved_admissionP, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201)
        else:
            return Response(status=400)

    def delete(self, request, pk):
        admissionP = get_object_or_404(Admission.objects.all(), pk=pk)
        admissionP.delete()
        return Response(status=204)


class Sale_pointS(APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        sale_pointS = Sale_point.objects.all()
        serializer = Sale_pointSerializers(sale_pointS, many=True)
        return Response({"data": serializer.data})


class Admission_pointS(APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        admission_pointS = Admission_point.objects.all()
        serializer = Admission_pointSerializers(admission_pointS, many=True)
        return Response({"data": serializer.data})
