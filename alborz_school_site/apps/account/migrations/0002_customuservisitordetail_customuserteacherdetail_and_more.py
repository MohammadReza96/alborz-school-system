# Generated by Django 4.1.4 on 2023-06-03 19:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import modules.file_upload_module


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="CustomUserVisitorDetail",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(blank=True, max_length=50, verbose_name="نام"),
                ),
                (
                    "family",
                    models.CharField(
                        blank=True, max_length=50, verbose_name="نام خانوادگی"
                    ),
                ),
                (
                    "email",
                    models.EmailField(blank=True, max_length=200, verbose_name="ایمیل"),
                ),
                (
                    "register_date",
                    models.DateField(
                        default=django.utils.timezone.now, verbose_name="تاریخ ثبت نام"
                    ),
                ),
                (
                    "update_date",
                    models.DateField(auto_now=True, verbose_name="تاریخ آپدیت"),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="کاربر",
                    ),
                ),
            ],
            options={
                "verbose_name": "جدول اطلاعات کاربر عادی",
                "verbose_name_plural": "جدول اطلاعات کاربران عادی",
            },
        ),
        migrations.CreateModel(
            name="CustomUserTeacherDetail",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(blank=True, max_length=50, verbose_name="نام"),
                ),
                (
                    "family",
                    models.CharField(
                        blank=True, max_length=50, verbose_name="نام خانوادگی"
                    ),
                ),
                (
                    "email",
                    models.EmailField(blank=True, max_length=200, verbose_name="ایمیل"),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to=modules.file_upload_module.FileUploader.upload_to,
                        verbose_name="عکس کاربر",
                    ),
                ),
                (
                    "address",
                    models.TextField(blank=True, null=True, verbose_name="ادرس"),
                ),
                (
                    "city",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="شهر"
                    ),
                ),
                (
                    "province",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="استان"
                    ),
                ),
                (
                    "postal_code",
                    models.CharField(
                        blank=True, max_length=12, null=True, verbose_name="کدپستی"
                    ),
                ),
                (
                    "register_date",
                    models.DateField(
                        default=django.utils.timezone.now, verbose_name="تاریخ ثبت نام"
                    ),
                ),
                (
                    "update_date",
                    models.DateField(auto_now=True, verbose_name="تاریخ آپدیت"),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="کاربر",
                    ),
                ),
            ],
            options={
                "verbose_name": "جدول اطلاعات استاد",
                "verbose_name_plural": "جدول اطلاعات اساتید",
            },
        ),
        migrations.CreateModel(
            name="CustomUserStudentDetail",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(blank=True, max_length=50, verbose_name="نام"),
                ),
                (
                    "family",
                    models.CharField(
                        blank=True, max_length=50, verbose_name="نام خانوادگی"
                    ),
                ),
                (
                    "email",
                    models.EmailField(blank=True, max_length=200, verbose_name="ایمیل"),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to=modules.file_upload_module.FileUploader.upload_to,
                        verbose_name="عکس کاربر",
                    ),
                ),
                (
                    "address",
                    models.TextField(blank=True, null=True, verbose_name="ادرس"),
                ),
                (
                    "city",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="شهر"
                    ),
                ),
                (
                    "province",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="استان"
                    ),
                ),
                (
                    "postal_code",
                    models.CharField(
                        blank=True, max_length=12, null=True, verbose_name="کدپستی"
                    ),
                ),
                (
                    "register_date",
                    models.DateField(
                        default=django.utils.timezone.now, verbose_name="تاریخ ثبت نام"
                    ),
                ),
                (
                    "update_date",
                    models.DateField(auto_now=True, verbose_name="تاریخ آپدیت"),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="کاربر",
                    ),
                ),
            ],
            options={
                "verbose_name": "جدول اطلاعات دانش آموز",
                "verbose_name_plural": "جدول اطلاعات دانش آموزان",
            },
        ),
    ]
