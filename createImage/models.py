from django.db import models


class Image(models.Model):
    text = models.CharField(max_length=150, verbose_name="текст для создания картинки",
                               help_text="Напишите текст, по которому сгенерируется картинка")
    image = models.ImageField(
        upload_to='images/', verbose_name='изображение', blank=True, null=True)

    def __str__(self):
        return f"Изображение для текста: {self.text.content}"

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"