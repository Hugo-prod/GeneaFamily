from GeneaFamily import settings
from django.conf.urls import url
from django.views.generic import TemplateView
from django.conf.urls.static import static

from .member import member_urlpatterns
from .location import location_urlpatterns
from .event import event_urlpatterns
from .event_type import event_type_urlpatterns
from .family import family_urlpatterns
from .child import child_urlpatterns
from .union import union_urlpatterns
from .military import military_urlpatterns
from .baptism import baptism_urlpatterns
from .birth import birth_urlpatterns
from .death import death_urlpatterns
from .residence import residence_urlpatterns
from .job import job_urlpatterns
from .source import source_urlpatterns


urlpatterns = [
	url(r'^$', 
		TemplateView.as_view(template_name='generic/index.html'), name='home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

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

# Wedding urls
urlpatterns += union_urlpatterns

# Military urls
urlpatterns += military_urlpatterns

# Birth urls
urlpatterns += birth_urlpatterns

# Death urls
urlpatterns += death_urlpatterns

# Baptism urls
urlpatterns += baptism_urlpatterns

# Residence urls
urlpatterns += residence_urlpatterns

# Job urls
urlpatterns += job_urlpatterns

# Source urls
urlpatterns += source_urlpatterns