from django.urls import include, path
from rest_framework.routers import SimpleRouter

from . import views

__app_name__ = 'polls'

router = SimpleRouter()
router.register('polls', views.QuestionViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
]
