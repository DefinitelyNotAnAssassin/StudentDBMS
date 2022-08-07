import django_filters as filter

from Student_Account.models import * 

class StudentAccountFilter(filter.FilterSet):

    class Meta:
        model = StudentProfile
        fields = ['user__id_number', 'user__first_name', 'user__last_name', 'section']
