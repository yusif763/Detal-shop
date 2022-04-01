from enum import unique
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.conf import settings
from django.core import validators
from django.utils.safestring import mark_safe
from django.contrib.sessions.models import Session
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from tools.slug_generator import slugify
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse_lazy

from django.contrib.auth.models import UserManager
from django.core.validators import MaxValueValidator, MinValueValidator


class AccountManager(UserManager):

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, password, **extra_fields)

# Customize User model
class User(AbstractBaseUser, PermissionsMixin):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.
    First name, last name, date of birth and email are required. Other fields are optional.
    """
    username = models.CharField(
        _('username'),
        max_length=150,
        blank=True,
        null=True,
        unique=False,
        default='user',
        help_text=_(
            'Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
    )
    first_name = models.CharField(
        _("First Name"), max_length=60, null=False, blank=False)
    last_name = models.CharField(
        _("Last Name"), max_length=70, null=False, blank=False)
    email = models.EmailField(_('Email'), unique=True)
    adress = models.CharField(_("Adress"), max_length=300, null=True, blank=True)
    phone = models.CharField(_("Phone"), max_length=15, null=True, blank=True)
    image = models.ImageField(
        _('Image'), upload_to='user_image', blank=True, null=True)
    is_market = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField('Date joined', default=timezone.now)
    # legacy fields
    old_psw_hash = models.CharField(blank=True, null=True, max_length=300)
    is_staff = models.BooleanField('staff status', default=False,
                                   help_text='Designates whether the user can log into this admin site.')
    # slug for detail page
    slug = models.SlugField(max_length=255, null=True, blank=True)
    """
        Important non-field stuff
    """
    objects = AccountManager()
    REQUIRED_FIELDS = []
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'

    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        return reverse_lazy('account:self-profile',kwargs={'slug':self.slug})

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        self.slug = slugify(str(self.date_joined.timestamp()))
        super(User, self).save(*args, **kwargs)

    def get_avatar(self):
        if self.image:
            return self.image.url
        return 'https://cdt.org/files/2015/10/2015-10-06-FB-person.png'

    @property
    def fullname(self):
        return self.name + self.surname
    


# class UserManager(BaseUserManager):
#     """
#     Custom user model manager where email is the unique identifiers
#     for authentication instead of usernames.
#     """

#     def create_user(self, email, password=None, **extra_fields):
#         """
#         Create and save a User with the given email and password.
#         """
#         if not email:
#             raise ValueError(_('The Email must be set'))

#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save()

#         return user

#     def _create_user(self, email, password, **extra_fields):
#         """
#         Create and save a user with the given username, email, and password.
#         """
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_user(self, email=None, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', False)
#         extra_fields.setdefault('is_superuser', False)
#         return self._create_user(email, password, **extra_fields)

#     def create_superuser(self, email, password, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')
#         return self._create_user(email, password, **extra_fields)


# class User(AbstractUser, PermissionsMixin):
#     """
#     in this table you can store user
#     """

#     # information`s
#     username = models.CharField(
#         _('username'),
#         max_length=150,
#         blank=True,
#         null=True,
#         unique=False,
#         default='user',
#         help_text=_(
#             'Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
#     )
#     first_name = models.CharField(
#         _("First Name"), max_length=60, null=False, blank=False)
#     last_name = models.CharField(
#         _("Last Name"), max_length=70, null=False, blank=False)
#     email = models.EmailField(_('Email'), unique=True)
#     phone = models.CharField(_("Phone"), max_length=15, null=True, blank=True)
#     image = models.ImageField(
#         _('Image'), upload_to='user_image', blank=True, null=True)

#     # moderation`s
#     is_market = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=False)
#     date_joined = models.DateTimeField(default=timezone.now)

#     REQUIRED_FIELDS = []
#     EMAIL_FIELD = 'email'
#     USERNAME_FIELD = 'email'

#     # objects = UserManager()

#     @property
#     def profile_picture(self):
#         if self.image:
#             return self.image
#         return 'https://www.pngfind.com/pngs/m/470-4703547_icon-user-icon-hd-png-download.png'

#     def __str__(self):
#         return self.email


class Rating(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_rating')
    rated_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='rated_user_rating')
    rating = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])

    class Meta:
        unique_together = ('user', 'rated_user')

    def __str__(self):
        return f"{self.user} - {self.rated_user} - {self.rating}"
    
    def save(self, *args, **kwargs):
        if self.user == self.rated_user:
            raise ValidationError('You can not rate yourself')
        super(Rating, self).save(*args, **kwargs)