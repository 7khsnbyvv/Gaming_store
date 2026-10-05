import uuid
from django.db import models
from django.db.models import Avg
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='games/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='games', null=True, blank=True)
    discount_percent = models.PositiveIntegerField(default=0, help_text="0 dan 100 gacha, masalan 30")

    @property
    def final_price(self):
        if self.discount_percent:
            return round(self.price * (100 - self.discount_percent) / 100, 2)
        return self.price

    @property
    def has_discount(self):
        return self.discount_percent > 0

    @property
    def average_rating(self):
        result = self.reviews.aggregate(avg=Avg('rating'))['avg']
        return round(result, 1) if result else 0

    @property
    def review_count(self):
        return self.reviews.count()

    @property
    def stars(self):
        full = int(round(self.average_rating))
        return '★' * full + '☆' * (5 - full)

    def __str__(self):
        return self.title


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Order #{self.id} - {self.user.username if self.user else 'Guest'}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    activation_key = models.CharField(max_length=50, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.activation_key:
            prefix = self.game.title[:3].upper().replace(' ', 'X')
            self.activation_key = f"{prefix}-{uuid.uuid4().hex[:4].upper()}-{uuid.uuid4().hex[:4].upper()}-{uuid.uuid4().hex[:4].upper()}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.game.title} Key"


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wishlist_items')
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'game')


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'game')
        ordering = ['-created_at']

    @property
    def stars(self):
        return '★' * self.rating + '☆' * (5 - self.rating)

    def __str__(self):
        return f"{self.user.username} - {self.game.title} ({self.rating})"