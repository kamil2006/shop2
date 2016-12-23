from django.db import models


class Product(models.Model):
	title = models.CharField('Название', max_length=100)
	description = models.TextField('Описание', max_length=2000)
	price = models.IntegerField('Цена')
	img = models.ImageField('Картинка' ,upload_to='products', blank=True)


	def __str__(self):
		return '{0} {1}'.format(self.title, self.price) 


	class Meta:
		verbose_name = 'Продукт'
		verbose_name_plural = 'Продукты'

	def get_img(self):
		if self.img:
			return self.img.url
		else:
			return '/static/defolt.jpg'
