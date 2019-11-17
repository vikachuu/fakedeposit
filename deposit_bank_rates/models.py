from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.search import index

from wagtail.api import APIField

from wagtail.core.templatetags import wagtailcore_tags


class DepositBankRatesPage(Page):
    
    text_field = RichTextField(blank=True)
    page_description = models.CharField(max_length=200, default="string")

    content_panels = Page.content_panels + [
        FieldPanel('text_field', classname="full"),
        FieldPanel('page_description')
    ]

    def text(self):
        return wagtailcore_tags.richtext(self.text_field)

    api_fields = [
        APIField('text'),
        APIField('page_description'),
    ]

class BankPage(Page):
    bank_name = models.CharField(max_length=100, default="string")
    deposit_name = models.CharField(max_length=100, default="string")
    income = models.BooleanField(default=False)
    dolar = models.FloatField(default=0.0)
    euro = models.FloatField(default=0.0)
    hryvna = models.FloatField(default=0.0)
    capitalization = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(3)])
    bank_image = models.ImageField(default=None)
    body = RichTextField(blank=True)
    full_body = RichTextField(blank=True)
    page_description = models.CharField(max_length=200, default="string")
    deposit_path = models.CharField(max_length=100, default="string")
    external_link = models.CharField(max_length=200, default="link")

    search_fields = Page.search_fields + [
        index.SearchField('bank_name'),
        index.SearchField('deposit_name'),
        index.SearchField('income'),
        index.SearchField('dolar'),
        index.SearchField('euro'),
        index.SearchField('hryvna'),
        index.SearchField('capitalization'),
        index.SearchField('bank_image'),
        index.SearchField('body'),
        index.SearchField('full_body'),
        index.SearchField('page_description'),
        index.SearchField('deposit_path'),
        index.SearchField('external_link'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('bank_name'),
        FieldPanel('deposit_name'),
        FieldPanel('income'),
        FieldPanel('dolar'),
        FieldPanel('euro'),
        FieldPanel('hryvna'),
        FieldPanel('capitalization'),
        FieldPanel('bank_image'),
        FieldPanel('body', classname="full"),
        FieldPanel('full_body', classname="full"),
        FieldPanel('page_description'),
        FieldPanel('deposit_path'),
        FieldPanel('external_link'),
    ]

    api_fields = [
        APIField('bank_name'),
        APIField('deposit_name'),
        APIField('income'),
        APIField('dolar'),
        APIField('euro'),
        APIField('hryvna'),
        APIField('capitalization'),
        APIField('bank_image'),
        APIField('body'),
        APIField('full_body'),
        APIField('page_description'),
        APIField('deposit_path'),
        APIField('external_link'),
    ]
