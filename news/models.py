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


from wagtail.core.blocks import (
    CharBlock, PageChooserBlock, StructValue, StructBlock, TextBlock, URLBlock)
from wagtail.search import index

import home as HOME

# Create your models here.
class NewsMainPage(Page):
    max_count = 1
    subpage_types = ["news.NewsPage"]

    template = "news/index.html"

    show_n = models.IntegerField(default=4)

    content_panels = Page.content_panels + [FieldPanel("show_n")]


    def get_context(self, request):
        context = super(NewsMainPage, self).get_context(request)

        context['root'] = HOME.models.HomePage.objects.all()[0]
        
        pubs = NewsPage.objects.order_by('-published_date')
        paginator = Paginator(pubs, self.show_n)
        page = request.GET.get("page")

        try:
            news = paginator.page(page)
        except PageNotAnInteger:
            news = paginator.page(1)
        
        except EmptyPage:
            news = paginator.page(paginator.num_pages)
        
        context["posts"] = news

        print(news)

        return context


class NewsPage(Page):
    parent_page_type = ['news.NewsMainPage']
    subpage_types = []

    template = "news/news.html"

    news_banner = models.ForeignKey(
                    "wagtailimages.Image",
                    null=True,
                    blank=True,
                    on_delete=models.SET_NULL,
                    related_name="+"
                    )

    news_title = models.CharField(blank=True, null=True, max_length=255)
    published_date = models.DateTimeField()
    news = RichTextField(blank=True, null=True)
    news_content = RichTextField(blank=True, null=True)
    useful_link = models.URLField(blank=True, null=True)

    content_panels = Page.content_panels + [
        ImageChooserPanel("news_banner"),
        FieldPanel("news_title"),
        FieldPanel("published_date"),
        FieldPanel("news"),
        FieldPanel("news_content"),
        FieldPanel("useful_link"),
    ]

    def get_context(self, request):
        context = super(NewsPage, self).get_context(request)
        context['root'] = HOME.models.HomePage.objects.all()[0]
        return context