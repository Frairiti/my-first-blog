from django.db import models

from django.utils import timezone


class Post(models.Model):#model.Model indica che quella classe è un mdoello Django, quindi Django sa che dovrebbe essere salvato nel Database.
    author = models.ForeignKey('auth.User') #link ad un altro modello
    title = models.CharField(max_length=200) #testo limitato alla lunghezza che riceve
    sesso = models.CharField(max_length=7)
    oggetto = models.TextField()
    text = models.TextField() #definisco un testo senza limite
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
