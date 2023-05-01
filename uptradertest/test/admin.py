from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from .models import MenuItem


admin.site.register(MenuItem,
                    DraggableMPTTAdmin,
                    list_display=(
                        'tree_actions',
                        'indented_title',
                     ),
                    list_display_links=(
                        'indented_title',
                    ),
                    prepopulated_fields={'slug':['name']}
                    )
