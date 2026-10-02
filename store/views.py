from django.views.generic import DetailView, ListView, TemplateView

from .forms import ContactForm, CustomOrderForm
from .models import Product


class HomeView(TemplateView):
    template_name = "store/home.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["featured_products"] = Product.objects.filter(
            is_active=True, is_featured=True
        )[:3]
        return ctx


class CollectionView(ListView):
    template_name = "store/collection.html"
    context_object_name = "products"
    paginate_by = 12

    def get_queryset(self):
        return Product.objects.filter(is_active=True)


class ProductDetailView(DetailView):
    template_name = "store/product_detail.html"
    context_object_name = "product"
    slug_url_kwarg = "slug"

    def get_queryset(self):
        return Product.objects.filter(is_active=True)


class CustomOrdersView(TemplateView):
    template_name = "store/custom_orders.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["form"] = CustomOrderForm()
        return ctx


class OurStoryView(TemplateView):
    template_name = "store/our_story.html"


class ContactView(TemplateView):
    template_name = "store/contact.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["form"] = ContactForm()
        return ctx


class CartView(TemplateView):
    template_name = "store/cart.html"
