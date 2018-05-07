from django.db import models

class Curso(models.Model):
    #id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(unique=True, max_length=20, blank=True, null=True)
    
    class Meta:
        managed = True
        db_table = 'Curso'
        app_label = 'disciplinas'