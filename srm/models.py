from django.db import models


class Lead(models.Model):
    full_name = models.CharField(max_length=123)
    email = models.EmailField()
    subject_line = models.CharField(max_length=123, blank=True, null=True)
    message = models.TextField()
    status = models.PositiveIntegerField(
        choices=(
            (1, 'Теплый'),
            (2, 'Горячий'),
            (3, 'Мертвый'),
            (4, 'Другое')
        ),
        default=1
    )
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.full_name

