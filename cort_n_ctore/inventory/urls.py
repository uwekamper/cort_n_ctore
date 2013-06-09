from rest_framework import routers

from inventory.views import PartViewSet, PlaceViewSet

router = routers.SimpleRouter()
router.register(r'parts', PartViewSet)
router.register(r'places', PlaceViewSet)

urlpatterns = router.urls