from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel

from wagtail.api import APIField

from wagtail.core.templatetags import wagtailcore_tags


class CalculatorPage(Page):
    
    text_field = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('text_field', classname="full")
    ]

    def text(self):
        return wagtailcore_tags.richtext(self.text_field)

    api_fields = [
        APIField('text'),
    ]
