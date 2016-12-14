from django.conf.urls import patterns, url, include
from thinkster_django_angular_boilerplate.views import IndexView

# .. Imports
from rest_framework_nested import routers
from authentication.views import AccountViewSet

#connection to AngularJS router?
router = routers.SimpleRouter()
router.register(r'accounts', AccountViewSet)

urlpatterns = patterns(
     '',
    # ... URLs
    url(r'^api/v1/', include(router.urls)),

    #make sure this is last, as this is the catch-all route
    url('^.*$', IndexView.as_view(), name='index'),
)