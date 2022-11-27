from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.


class LanguageResource(resources.ModelResource):
    class Meta:
        model = Language
        import_id_fields = ("code",)
        fields=('name', 'code')

class LanguageAdmin(ImportExportModelAdmin):
    resource_class = LanguageResource


class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category


class CategoryAdmin(ImportExportModelAdmin):
    resource_class = CategoryResource


class CountryResource(resources.ModelResource):
    class Meta:
        model = Country
        import_id_fields = ("code",)
        fields=('name', 'code', 'flag', 'languages')


class CountryAdmin(ImportExportModelAdmin):
    resource_class = CountryResource


class SubDivisionResource(resources.ModelResource):
    class Meta:
        model = SubDivision
        import_id_fields = ('code', )
        fields = ('name', 'code', 'country')

class SubDivisionAdmin(ImportExportModelAdmin):
    resource_class = SubDivisionResource


class RegionResource(resources.ModelResource):
    class Meta:
        model = Region


class RegionAdmin(ImportExportModelAdmin):
    resource_class = RegionResource


class ChannelResource(resources.ModelResource):
    class Meta:
        model = Channel


class ChannelAdmin(ImportExportModelAdmin):
    resource_class = ChannelResource


class StreamResource(resources.ModelResource):
    class Meta:
        model = Stream
        import_id_fields = ('channel', )


class StreamAdmin(ImportExportModelAdmin):
    resource_class = StreamResource


class GuideResource(resources.ModelResource):
    class Meta:
        model = Guide


class GuideAdmin(ImportExportModelAdmin):
    resource_class = GuideResource


class BlockListResource(resources.ModelResource):
    class Meta:
        model = BlockList


class BlockListAdmin(ImportExportModelAdmin):
    resource_class = BlockListResource


admin.site.register(Language, LanguageAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(SubDivision, SubDivisionAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(Channel, ChannelAdmin)
admin.site.register(Stream, StreamAdmin)
admin.site.register(Guide, GuideAdmin)
admin.site.register(BlockList, BlockListAdmin)
