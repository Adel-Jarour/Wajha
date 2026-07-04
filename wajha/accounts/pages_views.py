from django.shortcuts import render
from django.utils import timezone
from applications.models import Application
from grants.models import GrantOpportunity

def landing_view(request):
    grants = GrantOpportunity.objects.filter(
        status='published',
        deadline__gte=timezone.now().date()
    ).prefetch_related('degree_levels', 'countries').order_by('-created_at')[:6]

    saved_grant_ids = []
    if request.user.is_authenticated:
        saved_grant_ids = Application.objects.filter(
            student=request.user
        ).values_list('grant_id', flat=True)

    return render(request, 'pages/landing.html', {
        'grants': grants,
        'saved_grant_ids': list(saved_grant_ids),
    })

def about_view(request):
    return render(request, 'pages/about.html')