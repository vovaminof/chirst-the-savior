from modeltranslation.translator import translator, TranslationOptions
from savior.apps.savior.models import Carousel

class CarouselTranslationOptions(TranslationOptions):
    fields = ('title', 'long_text', 'link_text')

translator.register(Carousel, CarouselTranslationOptions)