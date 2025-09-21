from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from django.conf import settings
from .models import Contact, Review, Package, UserProfile, VillaReport, Comment
from .forms import ContactForm, ReviewForm, CustomUserCreationForm, UserProfileForm, VillaReportForm, CommentForm





def home(request):
    
    # Get approved reviews
    reviews = Review.objects.filter(is_approved=True)[:6]
    
    # Get packages
    packages = Package.objects.all()
    
    # Handle contact form submission
    if request.method == 'POST' and 'contact_form' in request.POST:
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, 'Thank you for your message! We will get back to you soon.')
            return redirect('home')
    else:
        contact_form = ContactForm()
    
    # Handle review form submission
    if request.method == 'POST' and 'review_form' in request.POST:
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.is_approved = False  # Reviews need approval
            review.save()
            messages.success(request, 'Thank you for your review! It will be published after approval.')
            return redirect('home')
    else:
        review_form = ReviewForm()
    
    context = {
        'contact_form': contact_form,
        'review_form': review_form,
        'reviews': reviews,
        'packages': packages,
    }
    
    return render(request, 'main/home.html', context)


def submit_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True, 'message': 'Thank you for your message!'})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    return JsonResponse({'success': False, 'message': 'Invalid request'})


def submit_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.is_approved = False
            review.save()
            return JsonResponse({'success': True, 'message': 'Thank you for your review!'})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    return JsonResponse({'success': False, 'message': 'Invalid request'})


# Authentication Views
def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Create user profile
            UserProfile.objects.create(user=user)
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'main/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {user.first_name}!')
                return redirect('dashboard')
    else:
        form = AuthenticationForm()
    
    return render(request, 'main/login.html', {'form': form})


@login_required
def dashboard(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    recent_reports = VillaReport.objects.filter(user=request.user)[:5]
    
    # Get statistics
    total_reports = VillaReport.objects.filter(user=request.user).count()
    pending_reports = VillaReport.objects.filter(user=request.user, status='pending').count()
    completed_reports = VillaReport.objects.filter(user=request.user, status='completed').count()
    
    context = {
        'user_profile': user_profile,
        'recent_reports': recent_reports,
        'total_reports': total_reports,
        'pending_reports': pending_reports,
        'completed_reports': completed_reports,
    }
    
    return render(request, 'main/dashboard.html', context)


@login_required
def profile_view(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
    else:
        form = UserProfileForm(instance=user_profile)
    
    return render(request, 'main/profile.html', {'form': form, 'user_profile': user_profile})


@login_required
def villa_reports(request):
    reports = VillaReport.objects.filter(user=request.user)
    paginator = Paginator(reports, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'main/villa_reports.html', {'page_obj': page_obj})


# Admin-only functions
def is_admin(user):
    return user.is_authenticated and user.is_staff

@user_passes_test(is_admin)
def admin_dashboard(request):
    # Get statistics
    total_reports = VillaReport.objects.count()
    pending_reports = VillaReport.objects.filter(status='pending').count()
    in_progress_reports = VillaReport.objects.filter(status='in_progress').count()
    completed_reports = VillaReport.objects.filter(status='completed').count()
    
    # Get recent reports
    recent_reports = VillaReport.objects.all()[:10]
    
    # Get recent comments
    recent_comments = Comment.objects.all()[:10]
    
    context = {
        'total_reports': total_reports,
        'pending_reports': pending_reports,
        'in_progress_reports': in_progress_reports,
        'completed_reports': completed_reports,
        'recent_reports': recent_reports,
        'recent_comments': recent_comments,
    }
    
    return render(request, 'main/admin_dashboard.html', context)

@user_passes_test(is_admin)
def admin_create_report(request):
    if request.method == 'POST':
        form = VillaReportForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Villa report created successfully!')
            return redirect('admin_dashboard')
    else:
        form = VillaReportForm()
    
    return render(request, 'main/admin_create_report.html', {'form': form})

@user_passes_test(is_admin)
def admin_edit_report(request, report_id):
    report = get_object_or_404(VillaReport, id=report_id)
    
    if request.method == 'POST':
        form = VillaReportForm(request.POST, instance=report)
        if form.is_valid():
            form.save()
            messages.success(request, 'Villa report updated successfully!')
            return redirect('admin_dashboard')
    else:
        form = VillaReportForm(instance=report)
    
    return render(request, 'main/admin_edit_report.html', {'form': form, 'report': report})

@user_passes_test(is_admin)
def admin_report_detail(request, report_id):
    report = get_object_or_404(VillaReport, id=report_id)
    comments = Comment.objects.filter(villa_report=report)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.villa_report = report
            comment.user = request.user
            comment.is_admin_comment = True
            comment.save()
            messages.success(request, 'Admin comment added successfully!')
            return redirect('admin_report_detail', report_id=report_id)
    else:
        form = CommentForm()
    
    context = {
        'report': report,
        'comments': comments,
        'form': form,
    }
    
    return render(request, 'main/admin_report_detail.html', context)

# User functions (updated)
@login_required
def villa_report_detail(request, report_id):
    report = get_object_or_404(VillaReport, id=report_id, user=request.user)
    comments = Comment.objects.filter(villa_report=report)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.villa_report = report
            comment.user = request.user
            comment.is_admin_comment = False
            comment.save()
            messages.success(request, 'Your comment has been added!')
            return redirect('villa_report_detail', report_id=report_id)
    else:
        form = CommentForm()
    
    context = {
        'report': report,
        'comments': comments,
        'form': form,
    }
    
    return render(request, 'main/villa_report_detail.html', context)