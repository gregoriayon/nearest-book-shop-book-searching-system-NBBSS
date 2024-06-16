# Generated by Django 4.1.7 on 2023-04-27 11:10

import app_book.manager
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="last name"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=122, null=True)),
                (
                    "email",
                    models.EmailField(
                        blank=True,
                        max_length=254,
                        unique=True,
                        verbose_name="email address",
                    ),
                ),
                ("phone", models.CharField(blank=True, max_length=12, null=True)),
                ("other_phone", models.CharField(blank=True, max_length=12, null=True)),
                (
                    "role",
                    models.CharField(
                        choices=[("User", "User"), ("Shop Owner", "Shop Owner")],
                        default="User",
                        max_length=122,
                        null=True,
                    ),
                ),
                ("otp", models.CharField(blank=True, max_length=122, null=True)),
                (
                    "image",
                    models.ImageField(
                        blank=True, null=True, upload_to="profile_picture/%Y/%d/%b"
                    ),
                ),
                ("address", models.TextField(blank=True, max_length=522, null=True)),
                ("is_verified", models.BooleanField(default=False, null=True)),
                ("date", models.DateField(auto_now_add=True)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            managers=[
                ("objects", app_book.manager.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="AuthorModel",
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
                    "author_name",
                    models.CharField(blank=True, max_length=225, null=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="BookCategoryModel",
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
                    "category_name",
                    models.CharField(blank=True, max_length=225, null=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="BookModel",
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
                ("title", models.CharField(blank=True, max_length=225, null=True)),
                (
                    "description",
                    models.TextField(blank=True, max_length=925, null=True),
                ),
                (
                    "cover_image",
                    models.ImageField(
                        blank=True, null=True, upload_to="cover-image/%Y/%d/%b"
                    ),
                ),
                (
                    "publication_date",
                    models.DateField(default=django.utils.timezone.now),
                ),
                ("price", models.FloatField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "author",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="app_book.authormodel",
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="app_book.bookcategorymodel",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ContactModel",
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
                ("name", models.CharField(max_length=122)),
                ("email", models.CharField(max_length=122)),
                ("phone", models.CharField(max_length=20)),
                ("message", models.TextField(max_length=255)),
                ("date", models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="PublisherModel",
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
                    "publisher_name",
                    models.CharField(blank=True, max_length=225, null=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="StoreModel",
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
                ("name", models.CharField(blank=True, max_length=525, null=True)),
                (
                    "phone",
                    phonenumber_field.modelfields.PhoneNumberField(
                        max_length=128, region="BD", unique=True
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, null=True, unique=True
                    ),
                ),
                ("street", models.TextField(blank=True, max_length=525, null=True)),
                ("city", models.CharField(blank=True, max_length=100, null=True)),
                ("zip_code", models.IntegerField(blank=True, null=True)),
                ("licence", models.CharField(blank=True, max_length=100, null=True)),
                ("location", models.CharField(blank=True, max_length=999, null=True)),
                ("is_active", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="store",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Store",
                "verbose_name_plural": "Stores",
            },
        ),
        migrations.CreateModel(
            name="ReviewModel",
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
                ("comment", models.CharField(max_length=500, null=True)),
                ("created_at", models.DateField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="OrderModel",
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
                    "order_status",
                    models.CharField(
                        choices=[
                            ("Pending", "Pending"),
                            ("Complete", "Complete"),
                            ("Cancelled", "Cancelled"),
                        ],
                        default="Pending",
                        max_length=122,
                        null=True,
                    ),
                ),
                (
                    "payment_method",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "transaction_id",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("is_paid", models.BooleanField(default=False)),
                ("order_date", models.DateTimeField(auto_now_add=True)),
                (
                    "book",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="app_book.bookmodel",
                    ),
                ),
                (
                    "customer",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="customer_orders",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "seller",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="seller_orders",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "store",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="app_book.storemodel",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="bookmodel",
            name="publisher",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="app_book.publishermodel",
            ),
        ),
        migrations.AddField(
            model_name="bookmodel",
            name="store",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="app_book.storemodel",
            ),
        ),
    ]
