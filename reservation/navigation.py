from django.urls import reverse_lazy

NAV_SHOWS = 'Shows'
NAV_ITEMS = (
    (NAV_SHOWS, reverse_lazy('home')),
)
def navigation_items(selected_item):
    items = []
    for name, url in NAV_ITEMS:
        items.append({
            'name': name,
            'url' : url ,
            'active' : True if selected_item == name else False
        })