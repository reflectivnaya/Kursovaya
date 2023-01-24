from django.contrib import admin
from import_export.admin import ImportExportMixin
from modeltranslation.admin import TranslationAdmin
from ads.models import Ads

class AdsAdmin(ImportExportMixin, TranslationAdmin):
    list_display = ('id', 'title', 'author', 'city', 'type')

admin.site.register(Ads, AdsAdmin)