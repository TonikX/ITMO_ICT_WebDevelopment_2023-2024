from datetime import datetime

from django.contrib import admin
from django.db.models import Q

from .models import *


class AgreementAdmin(admin.ModelAdmin):
    model = CollectiveAgreement  # Use the appropriate model here
    search_fields = ('agent__full_name',)

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)

        # Filter agents based on valid contracts
        valid_agent_ids = AgentContract.objects.filter(
            Q(end_date__gte=datetime.now()) &
            Q(start_date__lte=datetime.now())
        ).values_list('agent_id', flat=True).distinct()

        queryset = queryset.filter(agent_id__in=valid_agent_ids)

        return queryset, use_distinct


admin.site.register(Company)
admin.site.register(Employee)
admin.site.register(Agent)
admin.site.register(AgentContract)
admin.site.register(CollectiveAgreement, AgreementAdmin)
admin.site.register(IndividualAgreement, AgreementAdmin)
admin.site.register(CollectiveInsuranceClaim)
admin.site.register(IndividualInsuranceClaim)
