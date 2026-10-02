from django.db import models
from django.db.models.query_utils import Q

from hotel.models import Hotel

class FoodCategoryStatus(models.TextChoices):
    Active = 'A'
    Inactive = 'I'

class FoodCategory(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    sort_order = models.IntegerField(default=0)
    status = models.CharField(choices=FoodCategoryStatus.choices,default=FoodCategoryStatus.Active,max_length=2)
    def __str__(self):
        return self.name
    @staticmethod
    def find_all_active(hotel: Hotel):
        return [i for i in FoodCategory.objects.filter(Q(hotel=hotel) & Q(status=FoodCategoryStatus.Active)).order_by('sort_order')]
    @staticmethod
    def find_all(hotel: Hotel):
        return [i for i in FoodCategory.objects.filter(Q(hotel=hotel)).order_by('sort_order')]
    @staticmethod
    def find_by_id(id: int):
        return FoodCategory.objects.get(pk=id)


class FoodItem(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    category = models.ForeignKey(FoodCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    sort_order = models.IntegerField(default=0)
    status = models.CharField(choices=FoodCategoryStatus.choices,default=FoodCategoryStatus.Active,max_length=2)
    state_tax_percentage=models.FloatField(default=0)
    center_tax_percentage=models.FloatField(default=0)
    isVegetated=models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return self.name
    @staticmethod
    def find_all_active(hotel: Hotel):
        return [i for i in FoodItem.objects.filter(Q(hotel=hotel) & Q(status=FoodCategoryStatus.Active)).order_by('sort_order')]
    @staticmethod
    def find_all(hotel: Hotel):
        return [i for i in FoodItem.objects.filter(Q(hotel=hotel)).order_by('sort_order')]
    @staticmethod
    def find_by_name(name: str, hotel: Hotel):
        return [i for i in FoodItem.objects.filter(Q(hotel=hotel) & Q(name__contains=name)).order_by('sort_order')]
    @staticmethod
    def find_by_id(id: int):
        return FoodItem.objects.get(pk=id)
    @staticmethod
    def find_by_category(category)->list:
        return [i for i in FoodItem.objects.filter(category_id=category).all()]





