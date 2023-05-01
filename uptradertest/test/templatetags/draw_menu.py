from django import template

from test.models import MenuItem

register = template.Library()

@register.inclusion_tag('templatetags/menu.html', takes_context=True)
def draw_menu(context, *args):
    try:
        current_menu_item = MenuItem.objects.get(slug=context['slug'])
    except:
        if args:
            current_menu_item = MenuItem.objects.get(slug=args[0])
        else:
            current_menu_item = MenuItem.objects.first()
    menu_items = MenuItem.objects.all()
    return {'menu_items': menu_items, 'current_menu_item': current_menu_item}
