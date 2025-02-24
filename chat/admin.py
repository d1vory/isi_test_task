from django.contrib import admin

from chat.models import Thread, Message

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'thread', 'sender', 'created', 'is_read')
    readonly_fields = ('created', )

class MessageInlineAdmin(admin.StackedInline):
    model = Message
    extra = 0
    readonly_fields = ('created', )
    raw_id_fields = ('sender',)


@admin.register(Thread)
class ThreadAdmin(admin.ModelAdmin):
    list_display = ('id', 'created')
    readonly_fields = ('created', 'updated')
    inlines = (MessageInlineAdmin, )


