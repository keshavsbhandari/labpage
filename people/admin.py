from django.contrib import admin

# Register your models here.
from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)
from .models import PeoplePage, PeopleMainPage

class PeopleMainPageAdmin(ModelAdmin):
    model = PeopleMainPage
    menu_label = 'PeopleMainPage'

    lst_display = ('order_count')

class PeoplePageAdmin(ModelAdmin):
    model = PeoplePage
    menu_label = 'PeoplePage'
    menu_icon = 'pilcrow'
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False # or True to exclude pages of this type from Wagtail's explorer view
    list_display = ('people_name','category',
                    'people_role'
                    ,'designation',
                    'display_priority',)
    list_filter = ('category',)
    search_fields = ('people_name','category',
                    'people_role'
                    ,'designation',
                    'display_priority',)


modeladmin_register(PeoplePageAdmin)
modeladmin_register(PeopleMainPageAdmin)