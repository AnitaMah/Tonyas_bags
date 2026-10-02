from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=120, widget=forms.TextInput(attrs={"placeholder": "Your name"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": "you@email.com"}))
    message = forms.CharField(
        widget=forms.Textarea(attrs={"placeholder": "How can we help?", "rows": 6})
    )


class CustomOrderForm(forms.Form):
    name = forms.CharField(
        max_length=120, label="Your Name",
        widget=forms.TextInput(attrs={"placeholder": "Jane Smith"}),
    )
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": "you@email.com"}))
    event_date = forms.CharField(
        max_length=120, required=False, label="Event Date (optional)",
        widget=forms.TextInput(attrs={"placeholder": "e.g. June 14, 2027, or leave blank"}),
    )
    item = forms.CharField(
        max_length=200, label="What would you like made?",
        widget=forms.TextInput(attrs={"placeholder": "e.g. Everyday clutch, wedding clutch, hair comb"}),
    )
    details = forms.CharField(
        label="Palette & Details",
        widget=forms.Textarea(attrs={
            "placeholder": "Describe your colors, gown fabric, or attach a swatch photo by email",
            "rows": 5,
        }),
    )
