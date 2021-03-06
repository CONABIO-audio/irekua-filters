from django.utils.translation import gettext as _
from django_filters import FilterSet

from irekua_database.models import Collection


class Filter(FilterSet):
    class Meta:
        model = Collection
        fields = {
            'collection_type': ['exact'],
            'name': ['icontains'],
            'institution': ['exact'],
            'institution__institution_name': ['exact', 'icontains'],
            'institution__institution_code': ['exact', 'icontains'],
            'institution__country': ['icontains'],
            'administrators': ['icontains'],
            'created_on': ['gt', 'lt']
        }


search_fields = (
    'name',
    'description',
    'collection_type__name',
    'institution__institution_name',
    'institution__institution_code'
)


ordering_fields = (
    ('created_on', _('created on')),
    ('last_annotation__created_on', _('last annotation')),
    ('last_item__created_on', _('last item')),
    ('name', _('name')),
)
