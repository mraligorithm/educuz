from django.db import models

class Review(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Content(models.Model):
    CONTENT_TYPE_CHOICES = [
        ('video', 'Video'),
        ('text', 'Text'),
        ('audio', 'Audio'),
        ('attachment', 'Downloadable Attachment'),
        ('quiz', 'Quiz'),
    ]
    content_type = models.CharField(choices=CONTENT_TYPE_CHOICES, max_length=20)
    content = models.TextField()
    attachment = models.FileField(upload_to='attachments', blank=True, null=True)


class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    author = models.ForeignKey('users.User', on_delete=models.CASCADE)
    language = models.CharField(max_length=50)
    reviews = models.ManyToManyField('Review')
    contents = models.ManyToManyField('Content')