from django.conf.urls.defaults import *
from chartproject.charts.models import Chart
urlpatterns = patterns('',
   
  (r'^edit/$', 'chartproject.charts.views.edit'),
  (r'^edit/(?P<cid>\d+)/$', 'chartproject.charts.views.edit'),
  (r'^view/(?P<cid>\d+)/$', 'chartproject.charts.views.view'),  
  (r'^templatetags/$','chartproject.charts.views.templatetags'),
  (r'^charts/', 'django.views.generic.list_detail.object_list', {'queryset':Chart.objects.all()}),
     (r'^$', 'chartproject.charts.views.index')
)     
