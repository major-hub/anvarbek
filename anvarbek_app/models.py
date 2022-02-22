from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name="Категории")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Products(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название")
    desc = models.TextField(blank=True, null=True, verbose_name="Описание")
    image = models.ImageField(upload_to='anvarbek_app/', verbose_name="Изображение")
    price = models.DecimalField(max_digits=1000, decimal_places=2, verbose_name="Цена", default=10_000_000)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, default=3, verbose_name="Категория")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
