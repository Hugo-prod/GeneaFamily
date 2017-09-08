from django.conf.urls import url
from django.views.generic import TemplateView

from .suburls import urls_member, urls_location, urls_event_type

urlpatterns = [
	url(r'^$', 
		TemplateView.as_view(template_name='generic/index.html'), name='home'),
]

# Member urls
urlpatterns += urls_member.urlpatterns
# Location urls
urlpatterns += urls_location.urlpatterns
# Event_Type urls
urlpatterns += urls_event_type.urlpatterns