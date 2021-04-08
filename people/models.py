from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.blocks import ImageChooserBlock

from wagtail.documents.edit_handlers import DocumentChooserPanel
from wagtail.documents.blocks import DocumentChooserBlock

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)


from wagtail.core.blocks import (
    CharBlock, PageChooserBlock, StructValue, StructBlock, TextBlock, URLBlock)
from wagtail.search import index
import home as HOME
import publications as PUBLICATIONS
# Create your models here.

class PeopleMainPage(Page):
    max_count = 1
    subpage_types = ["people.PeoplePage"]
    order_count = models.IntegerField(default=0)
    template = "people/index.html"

    content_panels = Page.content_panels + [FieldPanel("order_count")]

    def get_context(self, request):
        context = super(PeopleMainPage, self).get_context(request)

        context['root'] = HOME.models.HomePage.objects.all()[0]
        
        people = PeoplePage.objects.all()
        
        context['alumni'] = people.filter(category="alumni").order_by("display_priority")
        context['student'] = people.filter(category="student").order_by("display_priority")

        print(context['student'])

        context['phd'] = people.filter(category="phd-student").order_by("display_priority")
        context['faculty'] = people.filter(category="faculty").order_by("display_priority")

        return context

class PeoplePage(Page):
    template = "people/people.html"
    parent_page_type = ['people.PeopleMainPage']
    subpage_types = []

    people_name = models.CharField(blank=True, null=True, max_length=100)
    category = models.CharField(default="Student", blank=False, max_length=25, null=False,
                    choices=[ ('faculty', 'Faculty'),
                              ('phd-student','PhD-Student'), 
                              ('student','Student'), 
                              ('visiting-scholar','Visiting-Scholar'), 
                              ('alumni','Alumni')])
    profile_picture = models.ForeignKey(
                    "wagtailimages.Image",
                    null=True,
                    blank=True,
                    on_delete=models.SET_NULL,
                    related_name="+"
                    )
    
    resume = models.ForeignKey(
                'wagtaildocs.Document',
                null=True,
                blank=True,
                on_delete=models.SET_NULL,
                related_name='+'
                )

    people_role = models.CharField(blank=True, null=True, max_length=100)
    designation = models.CharField(blank=True, null=True, max_length=100)
    organization = models.CharField(blank=True, null=True, max_length=100)
    bio = RichTextField(blank=True, null=True)
    profile = models.URLField(blank=True, null=True)

    display_priority = models.IntegerField(default=1)

    content_panels = Page.content_panels + [
        FieldPanel("people_name"),
        FieldPanel("category"),
        FieldPanel("display_priority"),
        ImageChooserPanel("profile_picture"),
        DocumentChooserPanel("resume"),
        FieldPanel("people_role"),
        FieldPanel("designation"),
        FieldPanel("organization"),
        FieldPanel("bio"),
        FieldPanel("profile"),
    ]

    def get_context(self, request):
        context = super(PeoplePage, self).get_context(request)
        context['root'] = HOME.models.HomePage.objects.all()[0]
        return context
        


# modeladmin_register(PeoplePage)
