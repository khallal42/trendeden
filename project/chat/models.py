from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth import get_user
# from .models import chat_message




class chat_mesg(models.Model):
    # messages = models.OneToOneField(users, on_delete=models.CASCADE)
    sender = models.ForeignKey(User,related_name='sender' , on_delete=models.CASCADE)
    message = models.CharField(max_length=300, default=None)
    receiver = models.ForeignKey(User,related_name='recaiver' , on_delete=models.CASCADE, default=None)
    created = models.DateTimeField(auto_now_add=True)

    # def get_user(self):
    #     return 
    
    def __str__(self):
        return f'{self.sender.get_username()} send : #{self.message}# to {self.receiver.get_username()}'

    class Meta:
        ordering = ['-created']
# class user(models.Model):
#     name = models.CharField(max_length=50, unique=True)
#     avatar = models.ImageField()
#     mess = models.OneToOneField(chat_mess, on_delete=models.CASCADE, default=None)
#     sender = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    
#     def __str__(self):
#         return self.name
