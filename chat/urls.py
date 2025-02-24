from rest_framework import routers

from chat.views.thread import ThreadViewSet

router = routers.SimpleRouter()

router.register('threads', ThreadViewSet)
urlpatterns = []
urlpatterns += router.urls