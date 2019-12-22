from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Account(models.Model):
    name=models.CharField(max_length=50)
    posts=models.IntegerField(max_length=15,default=0)
    following=models.IntegerField(max_length=15,default=0)
    followers=models.IntegerField(max_length=15,default=0)
    img=models.ImageField(upload_to='images',default='defaultuser.png',blank=True,null=True)
    uid=models.ForeignKey(User,on_delete=models.CASCADE,null=False)

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super().save()
        image=Image.open(self.img.path)
        if image.height>image.width:
            diff=(image.height-image.width)/2
            right=image.width
            bottom=image.height-diff
            new=image.crop((0,diff,right,bottom))
            new.save(self.img.path)
        elif image.height<image.width:
            diff = (image.width - image.height)/2
            right = image.width-diff
            bottom = image.height
            new = image.crop((diff,0,right,bottom))
            new.save(self.img.path)

class Feadback(models.Model):
    feadback=models.TextField(max_length=100)
    time=models.DateTimeField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
