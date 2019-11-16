from wagtail.wagtailimages.formats import Format, register_image_format, unregister_image_format

unregister_image_format('fullwidth')
register_image_format(Format('fullwidth', 'Full width', 'richtext-image full-width center-align', 'width-800'))

unregister_image_format('left')
register_image_format(Format('left', 'Left-aligned', 'richtext-image left left-align', 'width-500'))

unregister_image_format('right')
register_image_format(Format('right', 'Right-aligned', 'richtext-image right right-align', 'width-500'))
