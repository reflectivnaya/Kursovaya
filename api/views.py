from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError, NotFound, AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken;
from django.db.models import Q
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

# Models
from ads.models import Ads, FavouriteAdd
from authentication.models import User
from author.models import Author
from cities.models import Cities
from reviews.models import Review
from types_ads.models import TypesAds


# Serializers
from .serializers import UserSerializer
from .serializers import AdsSerializer
from .serializers import FavouriteAddSerializer
from .serializers import ReviewSerializer
from .serializers import AuthorSerializer
from .serializers import CitiesSerializer
from .serializers import TypesAdsSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    action(methods=['POST'], detail=False, url_path='register')
    def register(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'message': 'success'});

    @action(methods=['POST'], detail=False, url_path='login')
    def login(self, request):
        if 'email' not in request.data:
            raise ValidationError({'error': 'E-mail не может быть пустым'})
        if 'password' not in request.data:
            raise ValidationError({'error': 'Пароль не может быть пустым'})

        try:
            user = User.objects.get(email=request.data['email'])
        except User.DoesNotExist:
            raise NotFound({'error': 'Пользователь не найден'})

        if not user.check_password(request.data['password']):
            raise AuthenticationFailed({'error': 'Неверный пароль'})

        if not user.is_active:
            raise AuthenticationFailed({'error': 'Пользователь не активен'})

        refresh = RefreshToken.for_user(user)
        response = Response()
        response.data = {'access': str(refresh.access_token)}
        
        return response
    
    @action(methods=['GET'], detail=False, permission_classes=[IsAuthenticated], url_path='me')
    def get_user(self, request):
        user = request.user
        data = self.serializer_class(user).data
        return Response(data)


class AdsViewSet(viewsets.ModelViewSet):
    queryset = Ads.objects.all()
    serializer_class = AdsSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ('id', 'title')

    @action(methods=['POST'], detail=True, permission_classes=[IsAuthenticated], url_path='add-favourite')
    def add_favourite(self, request,pk=None):
        user = request.user
        add = self.queryset.get(pk=pk)
        try:
            add = FavouriteAdd.objects.get(user=user, add=add)
            add.delete()
            return Response({'message': 'Объявление удалено из избранных'})
        except FavouriteAdd.DoesNotExist:
            FavouriteAdd.objects.create(user=user, add=add)
            return Response({'message': 'Объявление добавлено в избранные'})


    @action(methods=['GET'], detail=False, permission_classes=[IsAuthenticated], url_path='favourites')
    def get_favourites(self, request):
        user = request.user
        add = FavouriteAdd.objects.filter(user=user)
        data = FavouriteAddSerializer(instance=add, many=True).data
        return Response(data)

    @action(methods=['GET'], detail=False, url_path='flats')
    def get_flats(self, ads):
        ads = Ads.objects.filter( Q(type_id__exact=2))
        data = AdsSerializer(instance=ads, many=True).data
        return Response(data)

    # @action(methods=['GET'], detail=False, url_path='good_end_of_day')
    # def get_good_end_of_day(self, ads):
    #     ads = Ads.objects.filter( Q(recipe_type__exact=4) | Q(recipe_type__exact=3))
    #     data = AdsSerializer(instance=ads, many=True).data
    #     return Response(data)

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class CitiesViewSet(viewsets.ModelViewSet):
    queryset = Cities.objects.all()
    serializer_class = CitiesSerializer


class TypesAdsViewSet(viewsets.ModelViewSet):
    queryset = TypesAds.objects.all()
    serializer_class = TypesAdsSerializer