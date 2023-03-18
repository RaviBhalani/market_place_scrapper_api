from rest_framework.routers import SimpleRouter

from scrapper.views import ScrapperViewSet

app_name = 'scrapper'
router = SimpleRouter(trailing_slash=False)
router.register('scrapper', ScrapperViewSet, basename='scrapper')

urlpatterns = [] + router.urls
