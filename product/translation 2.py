from modeltranslation.translator import register, TranslationOptions
from product.models import Product, Category


@register(Product)
class ProductTranslator(TranslationOptions):
    fields = ('title', 'description',)


@register(Category)
class CategoryTranslator(TranslationOptions):
    fields = ('title',)
