from django.contrib import admin

from relations.many_to_many.models.basic import Pizza, Topping
from relations.many_to_many.models.intermediate import Post, User, PostLike
from relations.many_to_many.models.self import FacebookUser
from relations.many_to_many.models.symmetrical import InstagramUser
from relations.many_to_many.models.symmetrical_intermediate import TwitterUser, Relation

admin.site.register(Pizza)
admin.site.register(Topping)
admin.site.register(Post)
admin.site.register(User)
admin.site.register(PostLike)
admin.site.register(FacebookUser)
admin.site.register(InstagramUser)
admin.site.register(TwitterUser)
admin.site.register(Relation)