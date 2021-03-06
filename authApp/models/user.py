from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, UserManager
from django.contrib.auth.hashers import make_password

class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError('Users Must have an username')
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(
            username=username,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user
#Se crea modelo de usuario, con los atributos respectivos:
class User(AbstractBaseUser, PermissionsMixin):
    documento_options = [
        ('cc', 'CC'),
        ('ce', 'CE'),
        ('pass', 'Pasaporte'),
    ]
    id = models.BigAutoField(primary_key=True)
    username = models.CharField('Username', max_length=50, unique=True)
    password = models.CharField('Password', max_length=255)
    nombres = models.CharField('Nombres', max_length=50)
    apellidos = models.CharField('Apellidos', max_length=50)
    email = models.EmailField(max_length=80)
    tipo_documento = models.CharField(max_length=4, choices=documento_options)
    documento = models.BigIntegerField()
    fecha_nto = models.DateField()
    telefono = models.BigIntegerField()
    lic_cond = models.BigIntegerField()
    exped_lic = models.DateField()
    is_staff = models.BooleanField(default=False)

    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)
    
    objects = UserManager()
    USERNAME_FIELD = 'username'
