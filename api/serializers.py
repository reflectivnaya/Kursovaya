from rest_framework import serializers

# Models
from ads.models import Ads, FavouriteAdd
from authentication.models import User
from author.models import Author
from cities.models import Cities
from reviews.models import Review
from types_ads.models import TypesAds


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'name', 'password', 'photo', 'bio', 'is_active']
        extra_kwargs = {
            'password': {'write_only': True}
        }


class AdsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ads
        fields = '__all__'

class FavouriteAddSerializer(serializers.ModelSerializer):
    user_data = UserSerializer(source='user')
    add_data = AdsSerializer(source='add')

    class Meta:
        model = FavouriteAdd
        exclude = ['user', 'add']
    


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class CitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cities
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class TypesAdsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypesAds
        fields = '__all__'