from django.db import models

# Create your models here.

class Pizza(models.Model):

    pizza_name = models.CharField(max_length = 200)

    def __str__(self):

        return self.pizza_name

class Toppings(models.Model):

    pizza = models.ForeignKey(Pizza, on_delete = models.CASCADE)
    topping_name = models.TextField() 

    class Meta:

        verbose_name_plural = 'toppings'

    def __str__(self):

        return self.topping_name

class Comment(models.Model):

    pizza = models.ForeignKey(Pizza, on_delete = models.CASCADE)
    comment = models.TextField()

    class Meta:

        verbose_name_plural = 'comments'
    
    def __str__(self):

        return self.comment