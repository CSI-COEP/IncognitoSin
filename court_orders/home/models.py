from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here

class custom_user(AbstractUser):
    judge = "0"
    clerk = "1"
    lawyer = "2"
    client = "3"
    
    user_role_choice =(
        (judge,"judge"),
        (clerk,"clerk"),
        (lawyer,"lawyer"),
        (client,"client")
    )


    user_role = models.CharField(max_length=1,choices=user_role_choice,null=True,blank=True)
    first_name = models.CharField(max_length=100,null=True,blank=True)
    larst_name = models.CharField(max_length=100,null=True,blank=True)
    mobile_no = models.CharField(max_length=100,null=True,blank=True)
    profile_pic = models.ImageField(upload_to="Profile_pic/",null=True,blank=True)

    # def __str__(self) -> str:
    #     return str(self.first_name + self.last_name)

    
class judge(models.Model):
    user = models.ForeignKey("home.custom_user",on_delete=models.CASCADE,null=True,blank=True)
    reg_no = models.CharField(max_length=250,blank=True,null=True)
    id_proof = models.FileField(upload_to="id_proof/",null=True,blank=True)
    certificate = models.FileField(upload_to="certificate/",blank=True,null=True)
    add_info = models.TextField(blank=True,null=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.reg_no +"---Verification--->"+ str(self.is_verified)

class clerk(models.Model):
    user = models.ForeignKey("home.custom_user",on_delete=models.CASCADE,null=True,blank=True)
    clerk_id = models.CharField(max_length=250,blank=True,null=True)
    id_proof = models.FileField(upload_to="id_proof/",null=True,blank=True)
    certificate = models.FileField(upload_to="certificate/",blank=True,null=True)
    add_info = models.TextField(blank=True,null=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.clerk_id +"---Verification--->"+ str(self.is_verified)

class lawyer(models.Model):
    user = models.ForeignKey("home.custom_user",on_delete=models.CASCADE,null=True,blank=True)
    reg_no = models.CharField(max_length=250,blank=True,null=True)
    id_proof = models.FileField(upload_to="id_proof/",null=True,blank=True)
    certificate = models.FileField(upload_to="certificate/",blank=True,null=True)
    add_info = models.TextField(blank=True,null=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.reg_no +"---Verification--->"+ str(self.is_verified)
