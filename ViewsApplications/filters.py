import django_filters as filter

from Student_Account.models import * 

class StudentAccountFilter(filter.FilterSet):

    class Meta:
        model = StudentProfile
        fields = ['user__first_name', 'user__last_name', 'section']
