from django.contrib import admin
from .models import Contact, Review, Package, UserProfile, VillaReport, Comment


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'email']
    readonly_fields = ['created_at']


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['name', 'rating', 'is_approved', 'created_at']
    list_filter = ['rating', 'is_approved', 'created_at']
    search_fields = ['name', 'comment']
    readonly_fields = ['created_at']
    list_editable = ['is_approved']
    
    def get_queryset(self, request):
        return super().get_queryset(request).order_by('-created_at')


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ['name', 'package_type', 'price', 'is_featured', 'created_at']
    list_filter = ['package_type', 'is_featured', 'created_at']
    search_fields = ['name', 'description']
    readonly_fields = ['created_at']
    list_editable = ['is_featured']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'package_type', 'description', 'price')
        }),
        ('Features', {
            'fields': ('features',)
        }),
        ('Settings', {
            'fields': ('is_featured',)
        }),
        ('Timestamps', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone', 'villa_type', 'subscription_package', 'created_at']
    list_filter = ['villa_type', 'subscription_package', 'created_at']
    search_fields = ['user__username', 'user__email', 'phone', 'villa_address']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('User Information', {
            'fields': ('user', 'phone', 'address')
        }),
        ('Villa Information', {
            'fields': ('villa_address', 'villa_type', 'subscription_package')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(VillaReport)
class VillaReportAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'report_type', 'priority', 'status', 'created_at']
    list_filter = ['report_type', 'priority', 'status', 'created_at']
    search_fields = ['user__username', 'title', 'description', 'location']
    readonly_fields = ['created_at', 'updated_at']
    list_editable = ['status', 'priority']
    
    fieldsets = (
        ('Report Information', {
            'fields': ('user', 'report_type', 'priority', 'title', 'description', 'location')
        }),
        ('Status & Scheduling', {
            'fields': ('status', 'scheduled_date', 'completed_date')
        }),
        ('Admin Notes', {
            'fields': ('admin_notes',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('user')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'villa_report', 'is_admin_comment', 'created_at']
    list_filter = ['is_admin_comment', 'created_at']
    search_fields = ['user__username', 'villa_report__title', 'comment']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Comment Information', {
            'fields': ('villa_report', 'user', 'comment', 'is_admin_comment')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('user', 'villa_report')