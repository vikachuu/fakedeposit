from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel

from wagtail.api import APIField


class CalculatorPage(Page):
    intro = RichTextField(blank=True)
    # intro = models.CharField(max_length=250)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
        # FieldPanel('intro'),
    ]

    api_fields = [
        APIField('intro'),
    ]
