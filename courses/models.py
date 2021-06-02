from django.db import models


class Base(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Course(Base):
    title = models.CharField(max_length=255)
    url = models.URLField(unique=True)

    class Meta:
        verbose_name = 'curso'
        verbose_name_plural = 'cursos'
        ordering = ['id']

    def __str__(self) -> str:
        return self.title


class Rating(Base):
    course = models.ForeignKey(
        Course,
        related_name='ratings',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255)
    email = models.EmailField()
    comment = models.TextField(blank=True, default='')
    rate = models.DecimalField(max_digits=2, decimal_places=1)

    class Meta:
        verbose_name = 'avaliação'
        verbose_name_plural = 'avaliações'
        unique_together = ['email', 'course']
        ordering = ['id']

    def __str__(self) -> str:
        return f'{self.name} avaliou o curso {self.course} com nota {self.rate}'
