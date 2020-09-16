from django.utils.translation import ugettext_lazy as _

from mayan.apps.smart_settings.classes import SettingNamespace

from .literals import (
    DEFAULT_RESULTS_LIMIT, DEFAULT_SEARCH_MATCH_ALL_DEFAULT_VALUE
)

namespace = SettingNamespace(label=_('Search'), name='search')

setting_backend = namespace.add_setting(
    global_name='SEARCH_BACKEND',
    default='mayan.apps.dynamic_search.backends.django.DjangoSearchBackend',
    help_text=_(
        'Full path to the backend to be used to handle the search.'
    )
)
setting_backend_arguments = namespace.add_setting(
    global_name='SEARCH_BACKEND_ARGUMENTS',
    default={}
)
setting_disable_simple_search = namespace.add_setting(
    global_name='SEARCH_DISABLE_SIMPLE_SEARCH',
    default=False, help_text=_(
        'Disables the single term bar search leaving only the advanced '
        'search button.'
    )
)
setting_match_all_default_value = namespace.add_setting(
    global_name='SEARCH_MATCH_ALL_DEFAULT_VALUE',
    default=DEFAULT_SEARCH_MATCH_ALL_DEFAULT_VALUE,
    help_text=_('Sets the default state of the "Match all" checkbox.')
)
setting_results_limit = namespace.add_setting(
    global_name='SEARCH_RESULTS_LIMIT', default=DEFAULT_RESULTS_LIMIT,
    help_text=_('Maximum number search results to fetch and display.')
)
