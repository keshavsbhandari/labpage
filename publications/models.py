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

class PublicationsMainPage(Page):
    max_count = 1
    template = "publications/index.html"

    subpage_types = ["publications.PublicationsPage"]

    show_n = models.IntegerField(default=10)

    content_panels = Page.content_panels + [FieldPanel("show_n"),]


    def get_context(self, request):
        context = super(PublicationsMainPage, self).get_context(request)

        context['root'] = HOME.models.HomePage.objects.all()[0]
        
        pubs = PublicationsPage.objects.order_by('-published_date')
        paginator = Paginator(pubs, self.show_n)
        page = request.GET.get("page")

        try:
            publications = paginator.page(page)
        except PageNotAnInteger:
            publications = paginator.page(1)
        
        except EmptyPage:
            publications = paginator.page(paginator.num_pages)
        
        context["posts"] = publications

        return context


class PublicationsPage(Page):
    template = "publications/publications.html"

    parent_page_type = ["publications.PublicationsMainPage"]
    subpage_types = []

    page_field = StreamField([
        ('page', CharBlock(required=False))
    ], blank=True)
    
    show_front = models.BooleanField(default=False)
    publication_title = models.CharField(blank=True, null=True, max_length=500)
    published_date = models.DateTimeField()
    author_conference_str = models.CharField(blank=True, null=True, max_length=500)
    abstract = RichTextField(blank=True, null=True)

    pub_banner = models.ForeignKey(
                    "wagtailimages.Image",
                    null=True,
                    blank=True,
                    on_delete=models.SET_NULL,
                    related_name="+"
                    )
    
    pdf_file = models.ForeignKey(
                'wagtaildocs.Document',
                null=True,
                blank=True,
                on_delete=models.SET_NULL,
                related_name='+'
                )
    
    project = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    demo = models.URLField(blank=True, null=True)

    content_panels = Page.content_panels + [
        FieldPanel("publication_title"),
        FieldPanel("show_front"),
        FieldPanel("published_date"),
        FieldPanel("author_conference_str"),
        StreamFieldPanel('page_field'),
        FieldPanel("abstract"),
        ImageChooserPanel("pub_banner"),
        DocumentChooserPanel("pdf_file"),
        FieldPanel("project"),
        FieldPanel("github"),
        FieldPanel("demo"),
    ]