from django.db import models


class ReviewDB(models.Model):
    class Meta:
        db_table = 'reviews'

    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=200, null=False)
    review = models.CharField(max_length=2000)
