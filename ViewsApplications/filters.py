import django_filters as filter

from Student_Account.models import * 

class StudentAccountFilter(filter.FilterSet):

    class Meta:
        model = StudentProfile
        fields = ['user__id_number', 'subjects__subject', 'section']
