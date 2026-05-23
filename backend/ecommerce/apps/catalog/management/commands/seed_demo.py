from django.core.management.base import BaseCommand

from ecommerce.apps.catalog.models import Category, Product, ProductImage, ProductVariant
from ecommerce.apps.shipping.models import ShippingMethod


class Command(BaseCommand):
    help = "Seed demo catalog and shipping data for local development."

    def handle(self, *args, **options):
        categories = {
            "audio": Category.objects.get_or_create(
                slug="audio",
                defaults={
                    "name": "Audio",
                    "description": "Headphones, speakers, and studio-ready sound.",
                    "image": "https://images.unsplash.com/photo-1546435770-a3e426bf472b?auto=format&fit=crop&w=900&q=80",
                },
            )[0],
            "wearables": Category.objects.get_or_create(
                slug="wearables",
                defaults={
                    "name": "Wearables",
                    "description": "Smart accessories for fitness, travel, and daily routines.",
                    "image": "https://images.unsplash.com/photo-1575311373937-040b8e1fd5b6?auto=format&fit=crop&w=900&q=80",
                },
            )[0],
            "home": Category.objects.get_or_create(
                slug="home",
                defaults={
                    "name": "Home",
                    "description": "Connected essentials for calm, capable spaces.",
                    "image": "https://images.unsplash.com/photo-1558002038-1055907df827?auto=format&fit=crop&w=900&q=80",
                },
            )[0],
            "travel": Category.objects.get_or_create(
                slug="travel",
                defaults={
                    "name": "Travel",
                    "description": "Useful gear for smarter packing and smoother trips.",
                    "image": "https://images.unsplash.com/photo-1488646953014-85cb44e25828?auto=format&fit=crop&w=900&q=80",
                },
            )[0],
        }

        products = [
            {
                "category": categories["audio"],
                "name": "AeroTune Wireless Headphones",
                "slug": "aerotune-wireless-headphones",
                "description": "Comfortable over-ear headphones with active noise control, 40-hour battery life, and a warm everyday sound profile.",
                "base_price": "149.00",
                "discount_price": "119.00",
                "stock": 28,
                "image": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?auto=format&fit=crop&w=900&q=80",
                "variants": ["Graphite", "Ivory"],
            },
            {
                "category": categories["wearables"],
                "name": "PulseFit Smart Band",
                "slug": "pulsefit-smart-band",
                "description": "A slim activity tracker with heart-rate monitoring, sleep insights, water resistance, and seven-day battery life.",
                "base_price": "89.00",
                "discount_price": None,
                "stock": 44,
                "image": "https://images.unsplash.com/photo-1576243345690-4e4b79b63288?auto=format&fit=crop&w=900&q=80",
                "variants": ["Small", "Large"],
            },
            {
                "category": categories["home"],
                "name": "GlowHub Smart Lamp",
                "slug": "glowhub-smart-lamp",
                "description": "A dimmable smart lamp with sunrise routines, app control, and a soft ceramic finish for desks and nightstands.",
                "base_price": "64.00",
                "discount_price": "52.00",
                "stock": 16,
                "image": "https://images.unsplash.com/photo-1507473885765-e6ed057f782c?auto=format&fit=crop&w=900&q=80",
                "variants": ["Warm White", "Sage"],
            },
            {
                "category": categories["travel"],
                "name": "PackLite Organizer Set",
                "slug": "packlite-organizer-set",
                "description": "Compression packing cubes, cable pouch, and toiletry sleeve made from lightweight recycled nylon.",
                "base_price": "42.00",
                "discount_price": None,
                "stock": 33,
                "image": "https://images.unsplash.com/photo-1553531384-cc64ac80f931?auto=format&fit=crop&w=900&q=80",
                "variants": ["Forest", "Slate"],
            },
            {
                "category": categories["audio"],
                "name": "DeskWave Mini Speaker",
                "slug": "deskwave-mini-speaker",
                "description": "Compact Bluetooth speaker with clear calls, braided carry loop, and enough punch for small rooms.",
                "base_price": "58.00",
                "discount_price": None,
                "stock": 21,
                "image": "https://images.unsplash.com/photo-1608043152269-423dbba4e7e1?auto=format&fit=crop&w=900&q=80",
                "variants": ["Cobalt", "Charcoal"],
            },
            {
                "category": categories["home"],
                "name": "BrewScale Precision Timer",
                "slug": "brewscale-precision-timer",
                "description": "A fast kitchen scale with pour-over timer, silicone cover, and USB-C charging for daily coffee routines.",
                "base_price": "36.00",
                "discount_price": "31.00",
                "stock": 19,
                "image": "https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?auto=format&fit=crop&w=900&q=80",
                "variants": ["Black", "Cream"],
            },
        ]

        for item in products:
            variants = item.pop("variants")
            image = item.pop("image")
            product, _created = Product.objects.update_or_create(
                slug=item["slug"],
                defaults=item,
            )
            ProductImage.objects.update_or_create(
                product=product,
                is_primary=True,
                defaults={"image": image, "alt_text": product.name},
            )
            for variant_name in variants:
                ProductVariant.objects.get_or_create(
                    product=product,
                    name=variant_name,
                    defaults={"sku": f"{product.slug[:18]}-{variant_name.lower().replace(' ', '-')}", "stock": product.stock},
                )

        shipping_methods = [
            ("Standard", "Arrives in 4 to 6 business days.", "5.00", 5),
            ("Express", "Arrives in 2 business days.", "12.00", 2),
            ("Local Pickup", "Collect from the nearest partner desk.", "0.00", 1),
        ]
        for name, description, cost, days in shipping_methods:
            ShippingMethod.objects.update_or_create(
                name=name,
                defaults={"description": description, "cost": cost, "estimated_days": days, "is_active": True},
            )

        self.stdout.write(self.style.SUCCESS("Demo catalog data is ready."))
