import django_filters
from django_filters import DateFilter

from .models import *

class OrderFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="date_created",lookup_expr='gte', label='Starting date')
    end_date = DateFilter(field_name="date_created",lookup_expr='lte', label='Ending date')
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['custumer', 'date_created']