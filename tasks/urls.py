from rest_framework import routers

from tasks.views import (
    CategoryViewSet,
    DashboardTaskByCategoryViewSet,
    DashboardTaskCompletionStatViewSet,
    TaskViewSet,
)

router = routers.DefaultRouter()
router.register(r"api/categories", CategoryViewSet, "categories")
router.register(r"api/tasks", TaskViewSet, "tasks")
router.register(
    r"api/dashboard/tasks-completion",
    DashboardTaskCompletionStatViewSet,
    "tasks-completion",
)
router.register(
    r"api/dashboard/tasks-category-distribution",
    DashboardTaskByCategoryViewSet,
    "tasks-category-distribution",
)

urlpatterns = router.urls
