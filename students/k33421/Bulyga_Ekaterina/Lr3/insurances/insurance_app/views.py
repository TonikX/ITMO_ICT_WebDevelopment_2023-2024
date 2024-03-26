from rest_framework import generics, status
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from .serializers import *


class IndividualListCreateView(generics.ListCreateAPIView):
    serializer_class = IndividualSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Individual.objects.all()

        firstname = self.request.query_params.get('firstname')
        if firstname:
            queryset = queryset.filter(firstname=firstname)

        lastname = self.request.query_params.get('lastname')
        if lastname:
            queryset = queryset.filter(lastname=lastname)

        return queryset


class IndividualDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Individual.objects.all()
    serializer_class = IndividualSerializer
    permission_classes = [IsAuthenticated]


class TypeListCreateView(generics.ListCreateAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    permission_classes = [IsAuthenticated]


class TypeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    permission_classes = [IsAuthenticated]


class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]


class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]


class OrganizationListCreateView(generics.ListCreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Organization.objects.all()

        fullname = self.request.query_params.get('fullname')
        if fullname:
            queryset = queryset.filter(fullname=fullname)

        return queryset


class OrganizationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [IsAuthenticated]


class InsureOrganizationListCreateView(generics.ListCreateAPIView):
    queryset = InsureOrganization.objects.all()
    serializer_class = InsureOrganizationSerializer
    permission_classes = [IsAuthenticated]


class InsureOrganizationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = InsureOrganization.objects.all()
    serializer_class = InsureOrganizationSerializer
    permission_classes = [IsAuthenticated]


class InsureAgentListCreateView(generics.ListCreateAPIView):
    queryset = InsureAgent.objects.all()
    serializer_class = InsureAgentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = InsureAgent.objects.all()

        username = self.request.query_params.get('username')
        if username:
            queryset = queryset.filter(username=username)

        return queryset


class InsureAgentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = InsureAgent.objects.all()
    serializer_class = InsureAgentSerializer
    permission_classes = [IsAuthenticated]


class ContractListCreateView(generics.ListCreateAPIView):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Contract.objects.all()

        date_from = self.request.query_params.get('date_from')
        if date_from:
            queryset = queryset.filter(date_from=date_from)

        date_to = self.request.query_params.get('date_to')
        if date_to:
            queryset = queryset.filter(date_to=date_to)

        organization = self.request.query_params.get('organization')
        if organization:
            queryset = queryset.filter(organization=organization)

        client = self.request.query_params.get('client')
        if client:
            queryset = queryset.filter(client=client)

        agent = self.request.query_params.get('agent')
        if agent:
            queryset = queryset.filter(agent=agent)

        return queryset

    def post(self, request, *args, **kwargs):
        serializer = ContractSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ContractDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = [IsAuthenticated]


class InsuranceCaseListCreateView(generics.ListCreateAPIView):
    queryset = InsuranceCase.objects.all()
    serializer_class = InsuranceCaseSerializer
    permission_classes = [IsAuthenticated]


class InsuranceCaseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = InsuranceCase.objects.all()
    serializer_class = InsuranceCaseSerializer
    permission_classes = [IsAuthenticated]
