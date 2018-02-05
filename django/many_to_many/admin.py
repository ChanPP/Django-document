from django.contrib import admin

# Register your models here.
from many_to_many.models import *

admin.site.register(Pizza)
admin.site.register(Topping)

admin.site.register(Post)
admin.site.register(User)
admin.site.register(PostLike)
