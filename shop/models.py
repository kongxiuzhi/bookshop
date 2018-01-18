from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MaxLengthValidator,MinLengthValidator
from django.core.exceptions import ValidationError
from django.urls import reverse
import datetime


# Create your models here.


class Category(models.Model):
	name = models.CharField(_('Category'),max_length=64)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = _('Category')
		verbose_name_plural = _('Category')

	def get_absolute_url(self):
		return reverse('shop:book_list_by_category',args=[str(self.id)])


		

today_str 	= "({} {})".format(_(".etc"),datetime.datetime.now().strftime("%Y-%m-%d"))


class BookEditValidator(object):
	@staticmethod
	def isdigit(value):
		if not value.isdigit():
			raise ValidationError(_('%s not pure digits') % value)


class Book(models.Model):

	#isbn10		= models.CharField(_('ISBN10'),default="",max_length=10,blank=True)
	isbn13		= models.CharField(_('ISBN13'),max_length=13,validators=[BookEditValidator.isdigit,MaxLengthValidator(13),MinLengthValidator(13)])
	title		= models.CharField(_('Title'),max_length=128)
	subtitle 	= models.CharField(_('Subtitle'),max_length=128,default="",blank=True)
	pages		= models.PositiveSmallIntegerField(_('Pages'),default=0,blank=0,null=0)
	author		= models.CharField(_('Author'),max_length=256,default="",blank=True)
	translator	= models.CharField(_('Translator'),max_length=256,default="",blank=True)
	publisher	= models.CharField(_('Publisher'),max_length=256,default="",blank=True)
	price		= models.DecimalField(_('Price'),max_digits=5,decimal_places=2,default=0,blank=True,null=True)
	binding		= models.CharField(_('Binding'),max_length=128,default="",blank=True)
	pubdate		= models.DateField(_('Date Published'),blank=True,null=True,help_text=today_str)
	authorDesc	= models.TextField(_('Author Desc'),blank=True,default="")
	cover		= models.ImageField(_('Book Cover'),upload_to="face/%Y/%m/%d",default="defa/1.jpg")
	summary		= models.TextField(_('Summary'),blank=True,default="")
	rating		= models.DecimalField(_('Rating'),max_digits=5,decimal_places=2,default=0,blank=True,null=True)
	category	= models.ForeignKey(Category,on_delete=models.SET_NULL,default="",blank=True,null=True,verbose_name=_('Category'))
	stock		= models.PositiveSmallIntegerField(_('Stock'),default=0,blank=True,null=True)
	sale		= models.BooleanField(_('Sale'),default=True,blank=True)
	douban		= models.URLField(_('douban'),max_length=255,default="",blank=True)
	#readPages	= models.PositiveSmallIntegerField(_('Read Pages'),default=0,blank=0,null=0,help_text="(%s)" %(_("Pages Be Read")))
	#readStart	= models.DateField(_('Reading Start'),blank=True,null=True,help_text=today_str)
	#readEnd		= models.DateField(_('Reading Finished'),blank=True,null=True,help_text=today_str)
	#readTags	= models.TextField(_('Reading Tags'),default="",blank=True)
	#readNote	= models.TextField(_('Reading Note'),default="",blank=True)
	#boughtPrice	= models.DecimalField(_('Price Bought'),max_digits=5,decimal_places=2,default=0,blank=True,null=True)
	#boughtDate 	= models.DateField(_('Date Bought'),blank=True,null=True,help_text=today_str)
	#location	= models.ForeignKey(Location,default="",blank=True,null=True,verbose_name=_('Location')) 
	def __str__(self):
		return self.title

	class Meta:
		verbose_name = _("Book")
		verbose_name_plural =verbose_name

	def get_absolute_url(self):

		return reverse('shop:book_detail',args=[str(self.id)])