from modeltranslation.translator import register, TranslationOptions
from main.models import Marka, Modell


@register(Marka)
class MarkaTranslator(TranslationOptions):
    fields = ('title',)


@register(Modell)
class ModellTranslator(TranslationOptions):
    fields = ('title',)
