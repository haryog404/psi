from django.db import models

# Create your models here.
class Produk(models.Model):
    nama = models.CharField(max_length=250)
    deskripsi = models.CharField(max_length=250)
    gambar = models.ImageField(upload_to='produk')
    
    def __str__(self):
        return self.nama