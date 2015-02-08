from django.db import models

class Tweet(models.Model):
    tweet_text = models.CharField(max_length=140, null=False)#null bos gecmesini istemiyorsam.
    rt_count = models.IntegerField(default=0)
    post_time = models.DateTimeField(auto_now_add=True)#suanki zamani otomatik olarak ekler.

    def __unicode__(self):
        return self.tweet_text #admin panelinde tweetleri gosteriyor.

# Create your models here.
