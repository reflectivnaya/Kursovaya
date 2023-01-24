from .models import Ads
from modeltranslation.translator import TranslationOptions, register

@register(Ads)
class AdsTranslation(TranslationOptions):
    fields = ('title', 'description',)
