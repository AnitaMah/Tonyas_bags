from decimal import Decimal

from django.core.management.base import BaseCommand
from django.utils.text import slugify

from store.models import Category, Product


class Command(BaseCommand):
    help = "Seed a handful of demo categories/products so the design has real data to render."

    def handle(self, *args, **options):
        categories = {
            "clutches": "Clutches",
            "evening-bags": "Evening Bags",
            "accessories": "Accessories",
        }
        cat_objs = {}
        for slug, name in categories.items():
            cat, _ = Category.objects.get_or_create(slug=slug, defaults={"name": name})
            cat_objs[slug] = cat

        products = [
            ("Ivory Pearl Clutch", "clutches", "185.00", True,
             "A hand-beaded ivory clutch finished with freshwater pearls — a bridal favorite."),
            ("Gilded Vine Evening Bag", "evening-bags", "225.00", True,
             "Climbing gold-bead vinework over a deep emerald base, hand-sewn bead by bead."),
            ("Rosette Beaded Clutch", "clutches", "165.00", True,
             "Layered rosette beading in blush and champagne tones, sized for an evening out."),
            ("Champagne Beaded Purse", "clutches", "175.00", False,
             "A soft champagne palette with delicate seed-bead trim."),
            ("Vintage Lace Evening Bag", "evening-bags", "210.00", False,
             "Lace-inspired beadwork over ivory silk, finished with a beaded chain strap."),
            ("Pearl Drop Hair Comb", "accessories", "68.00", False,
             "A hand-beaded hair comb with cascading pearl drops."),
            ("Beaded Bridal Belt", "accessories", "95.00", False,
             "A slim beaded belt to cinch a wedding gown or evening dress."),
            ("Rose Gold Clutch", "clutches", "195.00", False,
             "Rose-gold seed beads in a fan pattern over a structured frame."),
        ]

        created = 0
        for name, cat_slug, price, featured, desc in products:
            slug = slugify(name)
            _, was_created = Product.objects.get_or_create(
                slug=slug,
                defaults={
                    "name": name,
                    "category": cat_objs[cat_slug],
                    "price": Decimal(price),
                    "is_featured": featured,
                    "short_description": desc,
                    "is_active": True,
                },
            )
            created += int(was_created)

        self.stdout.write(self.style.SUCCESS(
            f"Seeded {len(cat_objs)} categories and {created} new products "
            f"({Product.objects.count()} total)."
        ))
