from django.db import models

# Create your models here.
class Notebook(models.Model):

    name = models.CharField('Notebook name', max_length=60)
    price = models.PositiveIntegerField('Notebook Price')
    img = models.ImageField('Notebook image', upload_to='images')
    about = models.TextField("Notebook description")

    def __str__(self):
        return self.name

class Review(models.Model):
    email = models.EmailField('Reviewer email')
    phone = models.CharField('reviewer phone', max_length=100)
    text = models.CharField('Reviewer text', max_length=200)

    def __str__(self):
        return self.email