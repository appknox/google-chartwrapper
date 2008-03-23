from GChartWrapper.charts import views
from django.conf.urls.defaults import *

urlpatterns = patterns('',
     url(r'^(?P<cid>\d+)/edit/$', views.edit),
     url(r'^(?P<cid>\d+)/$', views.view),
     url(r'', views.chart)
)     
