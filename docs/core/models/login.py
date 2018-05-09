from django.db import models



class Login(models.Model):
    
    email = models.EmailField(max_length = 255, unique=True)
    senha = models.CharField(max_length = 140)

    class Meta:
        managed = True
        db_table = 'Login'
        app_label = 'login'