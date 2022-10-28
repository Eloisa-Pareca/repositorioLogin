from django.db import models

# Create your models here.
"""
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return f'Perfil de {self.user.name}'

"""
class Categoria(models.Model):
    nombrecat = models.CharField(max_length=50, null=False, unique=True, verbose_name='nombre categoria')

    def __str__(self):
        return self.nombrecat

    class Meta:

        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
        ordering = ['id']

class Producto(models.Model):
    nombrepro = models.CharField(max_length=50)
    descripcionpro = models.CharField(max_length=255,verbose_name='descripcion del producto')
    imagenpro = models.ImageField(default='default_conejo.jpg', null=True, blank=True)
    stock = models.PositiveSmallIntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    #tienda = models.ForeignKey(Tienda, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombrepro