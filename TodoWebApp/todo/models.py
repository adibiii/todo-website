from django.db import models

from users.models import CustomUser


# Create your models here.


class Todo(models.Model):

    IN_PROGRESS = 1
    COMPLETED = 2
    WAITING = 3
    ATTRIBUTE_TYPE_FIELD = (
        (IN_PROGRESS, "in progress"),
        (COMPLETED, "completed"),
        (WAITING, "waiting")
    )

    A = 1
    B = 2
    C = 3
    ATTRIBUTE_TYPE_FIELD_2 = (
        (A, 'A'),
        (B, 'B'),
        (C, 'C')
    )
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=64)
    detail = models.TextField(null=True)
    priority = models.SmallIntegerField(choices=ATTRIBUTE_TYPE_FIELD_2)
    state = models.SmallIntegerField(default=IN_PROGRESS, choices=ATTRIBUTE_TYPE_FIELD)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
