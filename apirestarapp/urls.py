from django.conf.urls import url, include
from rest_framework import routers
from apirest import views
from apirest.views import CommentByMarkerView, CommentByMarkerViewOrderKarma, CommentByMarkerViewOrderDate, VotesViewSet

router = routers.DefaultRouter()
router.register(r'comments', views.CommentViewSet)
router.register(r'users', views.UserViewSet)
#router.register(r'karma', views.VotesViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url('^comments-marker/(?P<marker>.+)/$', CommentByMarkerView.as_view()),
    url('^karma/(?P<username>.+)/$', VotesViewSet.as_view()),
    url('^comments-marker-by-date/(?P<marker>.+)/$', CommentByMarkerViewOrderDate.as_view()),
    url('^comments-marker-by-karma/(?P<marker>.+)/$', CommentByMarkerViewOrderKarma.as_view()),
]