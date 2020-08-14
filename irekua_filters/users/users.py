from django.utils.translation import gettext as _
from django_filters import FilterSet

from irekua_database.models import User


class Filter(FilterSet):
    class Meta:
        model = User

        fields = {
            'username': ['exact', 'icontains'],
            'email': ['exact'],
            'first_name': ['icontains'],
            'last_name': ['gt', 'lt'],
            'institution': ['exact'],
        }


search_fields = (
    'first_name',
    'username',
    'last_name',
    'email',
)


ordering_fields = (
    ('created_on', _('added on')),
    ('last_name', _('last name')),
    ('first_name', _('first name')),
    ('Username', _('user name')),
)
