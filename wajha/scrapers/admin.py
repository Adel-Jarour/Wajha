from django.contrib import admin
from django.utils.html import format_html
from django.utils import timezone
from .models import GrantSource, ScrapedGrant


# ─────────────────────────────────────────────────────────────────────────────
# GrantSource Admin
# ─────────────────────────────────────────────────────────────────────────────

@admin.register(GrantSource)
class GrantSourceAdmin(admin.ModelAdmin):
    list_display  = ('name', 'url', 'frequency', 'is_active', 'failure_count', 'last_scraped_at')
    list_filter   = ('is_active', 'frequency')
    search_fields = ('name', 'url')
    list_editable = ('is_active',)
    readonly_fields = ('last_scraped_at', 'failure_count')

    fieldsets = (
        ('Source Info', {
            'fields': ('name', 'url', 'frequency', 'is_active')
        }),
        ('Scraper Config', {
            'fields': ('selector_map',),
            'classes': ('collapse',),
        }),
        ('Health Stats', {
            'fields': ('last_scraped_at', 'failure_count'),
            'classes': ('collapse',),
        }),
    )


# ─────────────────────────────────────────────────────────────────────────────
# Custom Admin Actions
# ─────────────────────────────────────────────────────────────────────────────

@admin.action(description='✅ Approve selected scraped grants')
def approve_grants(modeladmin, request, queryset):
    queryset.update(status='approved', reviewed_by=request.user)


@admin.action(description='❌ Reject selected scraped grants')
def reject_grants(modeladmin, request, queryset):
    queryset.update(status='rejected', reviewed_by=request.user)


# ─────────────────────────────────────────────────────────────────────────────
# ScrapedGrant Admin (The Review Queue Page)
# ─────────────────────────────────────────────────────────────────────────────

@admin.register(ScrapedGrant)
class ScrapedGrantAdmin(admin.ModelAdmin):
    list_display   = (
        'short_title', 'source',        'status_badge', 'deadline_display', 'source_link', 'scraped_at', 'reviewed_by'
    )
    list_filter    = ('status', 'source', 'scraped_at')
    search_fields  = ('raw_title', 'parsed_data')
    actions        = [approve_grants, reject_grants]
    readonly_fields = (
        'source', 'raw_title', 'raw_html_snippet', 'preview_html',
        'parsed_data', 'scraped_at', 'reviewed_by'
    )
    list_per_page  = 25

    fieldsets = (
        ('Raw Scraped Data', {
            'fields': ('source', 'raw_title', 'raw_html_snippet', 'preview_html', 'scraped_at')
        }),
        ('Parsed Details', {
            'fields': ('parsed_data',),
        }),
        ('Review', {
            'fields': ('status', 'reviewed_by'),
        }),
    )

    # ── Custom display columns ────────────────────────────────────────────────

    @admin.display(description='Title')
    def short_title(self, obj):
        return obj.raw_title[:70] + '…' if len(obj.raw_title) > 70 else obj.raw_title

    @admin.display(description='Status')
    def status_badge(self, obj):
        colors = {
            'pending':  '#f59e0b',
            'approved': '#10b981',
            'rejected': '#ef4444',
        }
        color = colors.get(obj.status, '#6b7280')
        return format_html(
            '<span style="background:{};color:#fff;padding:2px 10px;'
            'border-radius:12px;font-size:11px;font-weight:600;">{}</span>',
            color, obj.get_status_display()
        )

    @admin.display(description='Deadline')
    def deadline_display(self, obj):
        return obj.parsed_data.get('deadline', '—')

    @admin.display(description='Source URL')
    def source_link(self, obj):
        url = obj.parsed_data.get('url', '')
        if url:
            return format_html('<a href="{}" target="_blank">🔗 Open</a>', url)
        return '—'

    @admin.display(description='HTML Preview')
    def preview_html(self, obj):
        if obj.raw_html_snippet:
            return format_html(
                '<iframe srcdoc="{}" style="width:100%; height:300px; border:1px solid #ccc; border-radius:4px; background:#fff;" sandbox=""></iframe>',
                obj.raw_html_snippet
            )
        return 'No snippet available'
