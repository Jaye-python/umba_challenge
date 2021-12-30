from django.db import models


# Create your models here.

class GithubUsersDB(models.Model):
    
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=300)
    avatar_url = models.CharField(max_length=300)
    type = models.CharField(max_length=100)
    url = models.CharField(max_length=300)
    html_url = models.CharField(max_length=300, default='None')

    def __str__(self):
        return self.username

    # def get_absolute_url(self):
    #     return reverse('user-detail', kwargs={'pk': self.pk})
    
    class Meta:
        ordering = ['id', 'type']