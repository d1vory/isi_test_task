from rest_framework import routers
from rest_framework_nested.routers import NestedSimpleRouter

from chat.views.message import MessageViewSet
from chat.views.thread import ThreadViewSet

router = routers.SimpleRouter()

router.register('threads', ThreadViewSet)

message_router = NestedSimpleRouter(router, r'threads', lookup='thread')
message_router.register(r'messages', MessageViewSet, basename='thread-messages')

urlpatterns = []
urlpatterns += router.urls
urlpatterns += message_router.urls