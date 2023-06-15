from django.db import models
from django.utils import timezone  # add timezone for field created_at


class Tag(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}"


class Task(models.Model):
    content = models.CharField(max_length=255)  # remove blank=True, чтоб поле не могло быть пустым
    created_at = models.DateTimeField(default=timezone.now)  # change auto_now_add=True to default=timezone.now  чтобы при создании объекта модели поле created_at устанавливалось на время, когда объект был создан. auto_now_add=True означает, что время будет обновляться каждый раз при изменении объекта.
    deadline = models.DateTimeField(blank=True, null=True, default=None)  # add blank=True, null=True чтоб поле было необязательным
    is_done = models.BooleanField(default=False)
    tags = models.ManyToManyField(to=Tag, related_name="tasks")

    class Meta:
        ordering = ["is_done", "-created_at"]  # change "created_at", "is_done" to "is_done", "-created_at" для сортировки от невиконаного до виконаного та від найновішого до найстарішого

    def __str__(self):
        return self.content  # remove f"Content: "
