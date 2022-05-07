from rest_framework import routers
from tasks.views import CategoryViewSet, TaskViewSet

router = routers.DefaultRouter()
router.register(r"api/categories", CategoryViewSet, "categories")
router.register(r"api/tasks", TaskViewSet, "tasks")

urlpatterns = router.urls
