from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel

from wagtail.api import APIField


class ApplicationToFundPage(Page):
    text = RichTextField(blank=True)
    
    content_panels = Page.content_panels + [
        FieldPanel('text', classname="full")
    ]

    api_fields = [
        APIField('text'),
    ]
