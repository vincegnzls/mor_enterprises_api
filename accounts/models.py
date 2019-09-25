from django.db import models
import uuid
from django.utils import timezone
from django.contrib.auth.models import User

SHORT_LENGTH = 155
LONG_LENGTH = 255

SHORT_DIGITS = 12
LONG_DIGITS = 20


class UserProfile(models.Model):
    class Meta:
        verbose_name = 'User Profile'
        db_table = 't_user_profile'

    uuid = models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employee = models.ForeignKey(
        "Employee", null=True, blank=True, on_delete=models.CASCADE)
    role = models.ForeignKey("UserRole", on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now, blank=True)
    updated_at = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name


class UserRole(models.Model):
    class Meta:
        verbose_name = 'User Role'
        db_table = 't_user_role'

    uuid = models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=SHORT_LENGTH)
    description = models.CharField(max_length=LONG_LENGTH)
    created_at = models.DateTimeField(default=timezone.now, blank=True)
    updated_at = models.DateTimeField(default=timezone.now, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)


class Employee(models.Model):
    class Meta:
        db_table = 't_employee'

    uuid = models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)
    employee_number = models.CharField(max_length=SHORT_LENGTH)
    contact = models.CharField(max_length=SHORT_DIGITS)
    address = models.CharField(max_length=SHORT_LENGTH)
    tin = models.CharField(max_length=SHORT_DIGITS)
    sss = models.CharField(max_length=SHORT_DIGITS)
    started_at = models.DateTimeField(default=timezone.now, blank=True)
    created_at = models.DateTimeField(default=timezone.now, blank=True)
    updated_at = models.DateTimeField(default=timezone.now, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    active = models.BooleanField(default=False)
