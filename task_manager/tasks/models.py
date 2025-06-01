from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class TaskBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

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
    assigned_to = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='tasks_assigned'
        )
    label = models.ManyToManyField(Label, through='TaskLabel')


class TaskLabel(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    label = models.ForeignKey(Label, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('task', 'label')
