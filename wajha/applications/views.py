from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.utils import timezone
from datetime import timedelta
from .models import Application
from grants.models import GrantOpportunity


STATUS_COLUMNS = [
    ('saved', 'Saved', 'c-saved'),
    ('in_progress', 'In Progress', 'c-progress'),
    ('submitted', 'Submitted', 'c-submitted'),
    ('under_review', 'Under Review', 'c-review'),
    ('accepted', 'Accepted', 'c-accepted'),
    ('rejected', 'Rejected', 'c-rejected'),
]


@login_required
def dashboard(request):
    applications = Application.objects.filter(
        student=request.user
    ).select_related('grant')

    columns = {key: [] for key, _, _ in STATUS_COLUMNS}
    for app in applications:
        if app.status in columns:
            columns[app.status].append(app)

    today = timezone.now().date()
    deadlines_this_week = applications.filter(
        grant__deadline__range=[today, today + timedelta(days=7)]
    ).exclude(status__in=['accepted', 'rejected']).count()

    context = {
        'status_columns': STATUS_COLUMNS,
        'columns': columns,
        'total_tracked': applications.count(),
        'deadlines_this_week': deadlines_this_week,
    }
    return render(request, 'applications/dashboard.html', context)


@login_required
def update_status(request, application_id):
    if request.method != 'POST':
        return JsonResponse({'ok': False}, status=405)

    application = get_object_or_404(Application, pk=application_id, student=request.user)
    new_status = request.POST.get('status')

    valid_statuses = [key for key, _, _ in STATUS_COLUMNS]
    if new_status not in valid_statuses:
        return JsonResponse({'ok': False, 'error': 'invalid_status'}, status=400)

    application.status = new_status
    application.save()
    return JsonResponse({'ok': True})


@login_required
def save_grant(request, grant_id):
    if request.method != 'POST':
        return JsonResponse({'ok': False}, status=405)

    grant = get_object_or_404(GrantOpportunity, pk=grant_id)

    application = Application.objects.filter(
        student=request.user,
        grant=grant
    ).first()

    if application:
        if application.status == 'saved':
            application.delete()
            return JsonResponse({'ok': True, 'saved': False})
        else:
            return JsonResponse({'ok': False, 'error': 'already_in_progress'})
    else:
        Application.objects.create(
            student=request.user,
            grant=grant,
            status='saved'
        )
        return JsonResponse({'ok': True, 'saved': True})