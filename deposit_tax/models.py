from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel

from wagtail.api import APIField

from wagtail.core.templatetags import wagtailcore_tags


class DepositTaxPage(Page):
    
    text_field = RichTextField(blank=True)
    page_description = models.CharField(max_length=200, default="string")

    content_panels = Page.content_panels + [
        FieldPanel('text_field', classname="full"),
        FieldPanel('page_description'),
    ]

    def text(self):
        return wagtailcore_tags.richtext(self.text_field)

    api_fields = [
        APIField('text'),
        APIField('page_description'),
    ]
