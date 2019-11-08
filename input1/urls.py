from django.conf.urls import url
from input1.views import input1_view,room_selection_view

app_name='input1'

urlpatterns=[
	url(r'^input1/$',input1_view.as_view(),name='input1_view'),
	url(r'^room_selection/$',room_selection_view,name='room_selection_view'),
]