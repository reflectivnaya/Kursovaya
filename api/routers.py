from rest_framework import routers
from .views import AdsViewSet, UserViewSet, AuthorViewSet, CitiesViewSet, ReviewViewSet, TypesAdsViewSet

router = routers.DefaultRouter()

router.register(r'ads', AdsViewSet)
router.register(r'user', UserViewSet)
router.register(r'author', AuthorViewSet)
router.register(r'cities', CitiesViewSet)
router.register(r'review', ReviewViewSet)
router.register(r'typesads', TypesAdsViewSet)
