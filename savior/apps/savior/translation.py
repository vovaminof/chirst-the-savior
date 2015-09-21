from modeltranslation.translator import translator, TranslationOptions
from savior.apps.savior.models import Carousel, Footer

class CarouselTranslationOptions(TranslationOptions):
    fields = ('title', 'long_text', 'link_text')

class FooterTranslationOptions(TranslationOptions):
	fields = ('about_text',)

translator.register(Footer, FooterTranslationOptions)
translator.register(Carousel, CarouselTranslationOptions)