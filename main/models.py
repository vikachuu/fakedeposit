from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel

from wagtail.api import APIField


class MainPage(Page):
    
    page_description = models.CharField(max_length=200, default="string")

    content_panels = Page.content_panels + [
        FieldPanel('page_description')
    ]

    api_fields = [
        APIField('page_description'),
    ]
