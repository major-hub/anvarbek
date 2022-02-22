from modeltranslation.translator import translator, TranslationOptions
from .models import Products, Categories


class ProductsTranslationOptions(TranslationOptions):

    fields = ('title', 'desc')


translator.register(Products, ProductsTranslationOptions)


class CategoriesTranslationOptions(TranslationOptions):

    fields = ('name',)


translator.register(Categories, CategoriesTranslationOptions)
