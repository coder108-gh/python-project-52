from django.db import models
from ..users.models import UserProxy


User = UserProxy


class TaskBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        abstract = True


class Status(TaskBaseModel):
    name = models.CharField(max_length=100, null=False, unique=True)


class Label(TaskBaseModel):
    name = models.CharField(max_length=100, null=False, unique=True)


class Task(TaskBaseModel):
    name = models.CharField(max_length=250, null=False, unique=True)
    description = models.TextField()
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    creator = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='tasks_created'
        )
    executor = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='tasks_executed',
        null=True,
        blank=True
        )
    label = models.ManyToManyField(Label, through='TaskLabel', blank=True)


class TaskLabel(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    label = models.ForeignKey(Label, on_delete=models.PROTECT)

    class Meta:
        unique_together = ('task', 'label')
