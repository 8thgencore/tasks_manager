from rest_framework import routers
from tasks.views import CategoryViewSet

router = routers.DefaultRouter()
router.register(r"api/categories", CategoryViewSet, "categories")

urlpatterns = router.urls
