from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.core import blocks

from wagtail.images.blocks import ImageChooserBlock

from wagtail.documents.edit_handlers import DocumentChooserPanel
from wagtail.documents.blocks import DocumentChooserBlock

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


from wagtail.core.blocks import (
    CharBlock, PageChooserBlock, StructValue, StructBlock, TextBlock, URLBlock)
from wagtail.search import index

import news as NEWS
import people as PEOPLE
import publications as PUBLICATIONS




# noinspection PyUnresolvedReferences
class CarouselBlock(blocks.StructBlock):
    carousel_title = blocks.CharBlock(required=False)
    description = blocks.RichTextBlock(required=False)
    images = ImageChooserBlock(required=False)




class HomePage(Page):
    max_count = 1
    template = "home/index.html"
    subpage_types = ["people.PeopleMainPage", "publications.PublicationsMainPage", "news.NewsMainPage", ]

    group_logo = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )

    lab_title = models.CharField(blank=True, null=True, max_length=100)
    lab_sub_title = models.CharField(blank=True, null=True, max_length=255)

    carousel_field = StreamField([
        ('carousel', CarouselBlock()),
    ], blank=True)

    page_field = StreamField([
        ('page', PageChooserBlock(required=False))
    ], blank=True)

    about_us = RichTextField(blank=True)
    org_logo = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )

    org_title = models.CharField(blank=True, null=True, max_length=255)
    org_address = models.CharField(blank=True, null=True, max_length=255)
    org_email = models.EmailField(blank=True, null=True)
    org_phone = models.CharField(blank=True, null=True, max_length=20)
    disclaimer_url = models.URLField(blank=True, null=True)

    show_n_pub = models.IntegerField(default=10)
    show_n_news = models.IntegerField(default=1)

    content_panels = Page.content_panels + [
        ImageChooserPanel("group_logo"),
        FieldPanel("lab_title"),
        FieldPanel("lab_sub_title"),
        StreamFieldPanel('page_field'),
        
        StreamFieldPanel('carousel_field'),

        FieldPanel("about_us"),
        ImageChooserPanel("org_logo"),
        FieldPanel("org_title"),
        FieldPanel("org_address"),
        FieldPanel("org_email"),
        FieldPanel("org_phone"),
        FieldPanel("disclaimer_url"),

        FieldPanel("show_n_pub"),
        FieldPanel("show_n_news")
    ]

    def get_context(self, request):
        context = super(HomePage, self).get_context(request)
        # for i in self.page_field:
        #     print(i)
        #     print(str(i).split("class=")[-1].split(">")[0])

        context['news'] = NEWS.models.NewsPage.objects.order_by('-published_date')[:self.show_n_news]
        context['publications']  = PUBLICATIONS.models.PublicationsPage.objects.filter(show_front = True).order_by('-published_date')[:self.show_n_pub]
        return context


# # <!-- {% for block in self.carousel_field %}
# #     <h1>{{block.value.images}}</h1>
# # {% endfor %} -->