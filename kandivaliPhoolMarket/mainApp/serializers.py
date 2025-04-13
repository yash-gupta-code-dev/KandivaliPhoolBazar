from rest_framework import serializers
from .models import Product, Category


class ProductSerializer(serializers.ModelSerializer):
    # Optionally show category name instead of ID
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(), slug_field="name"
    )

    class Meta:
        model = Product
        fields = "__all__"

    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError(
                "Product name must be at least 3 characters long."
            )
        return value

    def validate_description(self, value):
        if not value.strip():
            raise serializers.ValidationError("Description cannot be empty.")
        return value

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be greater than zero.")
        return value

    def validate_discounted_price(self, value):
        price = self.initial_data.get("price")
        try:
            price = float(price)
            if value and price and value >= price:
                raise serializers.ValidationError(
                    "Discounted price must be less than regular price."
                )
        except ValueError:
            pass
        return value

    def validate_stock(self, value):
        if value < 0:
            raise serializers.ValidationError("Stock cannot be negative.")
        return value

    def validate_category(self, value):
        if not value.is_active:
            raise serializers.ValidationError("Selected category is not active.")
        return value

    def validate(self, data):
        # Extra layer of validation if needed
        if data.get("discounted_price") and data["discounted_price"] >= data["price"]:
            raise serializers.ValidationError(
                {
                    "discounted_price": "Discounted price must be less than the regular price."
                }
            )
        return data

    def create(self, validated_data):
        # Optional: Auto-generate slug if blank
        if not validated_data.get("slug"):
            validated_data["slug"] = slugify(validated_data["name"])
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if not validated_data.get("slug"):
            validated_data["slug"] = slugify(validated_data.get("name", instance.name))
        return super().update(instance, validated_data)
        