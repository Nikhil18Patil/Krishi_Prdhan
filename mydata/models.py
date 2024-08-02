from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission
from django.db import models

class UserProfileManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError("The Username field must be set")
        
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(username, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=True)
    # Add other fields as needed
    # ...

    objects = UserProfileManager()

    USERNAME_FIELD = 'username'

    # Specify related_name attributes to avoid clashes
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        related_name='user_profiles',  # Custom related_name
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        related_name='user_profiles_permissions',  # Custom related_name
    )

    def __str__(self):
        return self.username



    # Add additional fields to your profile model as needed





class mynews(models.Model):
    newstitle=models.CharField(max_length=255)
    newsdescription=models.TextField()    
    class Meta:
        db_table='itsnews'



# Create your models here.
