from django.db import models

# Create your models here.


class portfolioTable(models.Model):
    title = models.CharField(max_length=120)
    desc = models.TextField()
    # fileName = models.FileField()
    filename= models.FileField(upload_to='files/', null=True, verbose_name="")
    longDesc = models.TextField()

    def __str__(self):
        return self.title


class customerTable(models.Model):
    name = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    phone = models.CharField(max_length=120)
    desc = models.TextField()

    def __str__(self):
        return self.name
