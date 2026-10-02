# Tonea Bags — Django storefront (design pass)

A Django implementation of the "Elegant Beaded" store design: a handmade
beaded-bags-and-accessories shop. This pass covers the **front end only** —
pages, templates, styling, and real (but minimal) product data via the
Django admin. There is no cart/checkout/payment logic yet.

## Pages

- `/` — Home (hero + "A Few Favorites")
- `/collection/` — full product grid
- `/collection/<slug>/` — product detail
- `/custom-orders/` — custom order info + inquiry form
- `/our-story/` — about page
- `/contact/` — contact form
- `/cart/` — empty-cart state (no cart logic yet)
- `/admin/` — Django admin, for managing Categories and Products

## Running it locally

```bash
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt

python manage.py migrate
python manage.py runserver
```

Then open http://127.0.0.1:8000/

A superuser and 8 sample products are already seeded in `db.sqlite3` so the
pages render with real data out of the box:

- Admin login: **admin** / **tonyabags-admin-2026** (change this before any
  real deployment — it's a dev-only placeholder).

To reseed the demo catalog at any time:

```bash
python manage.py seed_demo
```

## Design notes

- Colors, type (Cormorant Garamond + Marcellus via Google Fonts), and layout
  in `store/static/store/css/style.css` were matched directly from the
  uploaded mockup.
- Product photos are rendered as labeled placeholder blocks
  (`.placeholder`) until real photography is uploaded. Add an image to a
  `Product` in the admin and it will replace the placeholder automatically.
- Brand name was filled in as "Tonea Bags" (from the project name) in place
  of the mockup's `[YOUR BRAND NAME]` placeholder — swap it in
  `store/templates/store/base.html` and `store/templates/store/home.html`
  footer/header if you want something different.

## Next steps (not in this pass)

- Cart/session logic, checkout, payments
- Wiring the Contact / Custom Orders forms to actually send email or save
  inquiries
- Real product photography
- Production settings (secret key, `ALLOWED_HOSTS`, static file serving)
