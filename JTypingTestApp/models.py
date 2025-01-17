from django.db import models
from django.contrib.auth.hashers import check_password

# Create your models here.

# Define the custom user model for MyTypingTestRecord
class MyTypingTestRecord(models.Model):
    username = models.CharField(max_length=150, unique=True) # Unique username field
    password = models.CharField(max_length=128) # Store hashed password
    last_login = models.DateTimeField(null=True, blank=True) # Track last login time

    def __str__(self):
        return self.username
    
    # Method to check if the given password matches the stored hashed password
    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
    
class Contact(models.Model):
    # Field to store the name of the contact
    name = models.CharField(max_length=100)
    # Field to store the email of the contact
    email = models.EmailField()
    # Field to store the message from the contact
    message = models.TextField()
    # Field to store the timestamp of when the contact was created
    timestamp = models.DateTimeField(auto_now_add=True)

    # Method to return a string representation of the Contact object
    def __str__(self):
        # Returns the name and email of the contact
        return f"{self.name} ({self.email})"
