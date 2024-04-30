import uuid
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    title = models.CharField(
        max_length=123
    )

    def __str__(self):
        return self.title


class House(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
    address = models.CharField(
        max_length=299
    )
    region = models.CharField(
        max_length=123
    )
    post_code = models.CharField(
        max_length=55
    )
    image = models.ImageField(
        upload_to='media/villa'
    )
    area = models.CharField(
        max_length=17
    )
    floor = models.PositiveIntegerField()
    bedroom = models.PositiveIntegerField()
    bathroom = models.PositiveIntegerField()
    parking_lot = models.PositiveIntegerField()
    description = models.TextField()
    is_security = models.BooleanField(
        default=False
    )
    authorization_type = models.PositiveIntegerField(
        choices=(
            (1, 'Белая книга'),
            (2, 'Зеленая книга'),
            (3, 'Красная книга'),
            (4, 'Для аренды'),
        )
    )
    payment_method = models.ForeignKey(
        'PaymentMethod',
        on_delete=models.CASCADE
    )
    price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0.00,
    )
    created_date = models.DateTimeField(
        auto_now_add=True
    )
    update_date = models.DateTimeField(
        auto_now=True
    )
    is_active = models.BooleanField(
        default=True
    )
    slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = str(uuid.uuid4())[:8]
        return super().save(*args, **kwargs)


    def __str__(self):
        return f"{self.address}, {self.region}{self.post_code}"


class PaymentMethod(models.Model):
    title = models.CharField(
        max_length=123
    )


    def __str__(self):
        return self.title


class Storage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    status = models.PositiveIntegerField(
        choices=(
            (1, 'В обработке'),
            (2, 'Откланен'),
            (3, 'Принят'),
        ),
        default=1
    )

    def save(self, *args, **kwargs):
        house = self.house
        if house.is_active:
            house.is_active = False
            house.save()
        return super().save(*args, **kwargs)

    def __str__(self):
        return str(self.user)