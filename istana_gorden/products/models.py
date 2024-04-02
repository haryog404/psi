from django.db import models
import myapp

# Create your models here.
class Item(models.Model):
    jenis_produk = models.ForeignKey(myapp.models.Produk, on_delete=models.CASCADE)
    nama = models.CharField(max_length=250)
    deskripsi = models.CharField(max_length=250)
    gambar = models.ImageField(upload_to='items', default='static/images/default.png')

    def __str__(self):
        return self.nama