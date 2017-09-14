from django.conf.urls import url
from django.views.generic import TemplateView

from .member import member_urlpatterns
from .location import location_urlpatterns
from .event import event_urlpatterns
from .event_type import event_type_urlpatterns
from .family import family_urlpatterns
from .child import child_urlpatterns

urlpatterns = [
	url(r'^$', 
		TemplateView.as_view(template_name='generic/index.html'), name='home'),
]

# Member urls
urlpatterns += member_urlpatterns

# Location urls
urlpatterns += location_urlpatterns

# Event urls
urlpatterns += event_urlpatterns

# Event_Type urls
urlpatterns += event_type_urlpatterns

# Family urls
urlpatterns += family_urlpatterns

# Child urls
urlpatterns += child_urlpatterns