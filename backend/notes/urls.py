from rest_framework import routers

from .views import NoteViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r'notes', NoteViewSet)
router.register(r'users', UserViewSet)
urlpatterns = router.urls
