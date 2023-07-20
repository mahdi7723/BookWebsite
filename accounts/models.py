# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
#
#
# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError('The Email field must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_admin', True)
#         return self.create_user(email, password, **extra_fields)
#
#
# class CustomUser(AbstractBaseUser):
#     email = models.EmailField(unique=True)
#     first_name = models.CharField(max_length=75)
#     last_name = models.CharField(max_length=75)
#     is_active = models.BooleanField(default=True)
#     last_login = models.DateTimeField(auto_now_add=False, null=True, blank=True)
#     avatar = models.ImageField(upload_to='avatars/', default='avatars/default.png')
#     phone = models.CharField(max_length=12)
#     address = models.CharField(max_length=500)
#     is_admin = models.BooleanField(default=False)
#
#     USERNAME_FIELD = 'email'
#     EMAIL_FIELD = 'email'
#     REQUIRED_FIELDS = []
#
#     objects = CustomUserManager()
#
#     def __str__(self):
#         return self.email
#
#     def update_avatar(self, new_avatar):
#         self.avatar = new_avatar
#         self.save()
#
#     def has_perm(self, perm, obj=None):
#         return self.is_admin
#
#     def has_module_perms(self, app_label):
#         return self.is_admin
#
#
# class PasswordResetToken(models.Model):
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     token = models.CharField(max_length=100, unique=True)
#     created_at = models.DateTimeField(auto_now_add=True)
