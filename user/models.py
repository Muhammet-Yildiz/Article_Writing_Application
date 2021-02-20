from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from PIL import Image

class Profile(models.Model):

    user = models.OneToOneField(User,on_delete= models.CASCADE, verbose_name ="Kullanıcı"  )
    profile_image = models.ImageField(blank  = True ,null= True , default ="/profile/user.png" , upload_to ="profile/" ,verbose_name="Kullanıcı fotografı ")
    def __str__(self):
        return  self.user.username 
    def saveas(self):
        super().save()
        img = Image.open(self.profile_image.path)
        if img.height > 250 or img.width > 250 : 
            output_size = (250,250)
            img.thumbnail(output_size)
            img.save(self.profile_image.path)