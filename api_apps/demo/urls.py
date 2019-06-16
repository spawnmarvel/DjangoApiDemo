from django.conf.urls import url
from rest_framework import routers
from demo.views import BagViewSet, ItemViewSet

router = routers.DefaultRouter()
router.register("bag", BagViewSet)
router.register("item", ItemViewSet)

urlpatterns = router.urls