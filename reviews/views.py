from django.shortcuts import redirect, reverse, get_object_or_404
from django.db.models import Avg
from django.contrib import messages
from .models import Reviews
from .forms import ReviewForm
from products.models import Product
from profiles.models import UserProfile


def add_review(request, product_id):
    user = UserProfile.objects.get(user=request.user)
    product = get_object_or_404(Product, pk=product_id)

    review_form = ReviewForm()

    review_submission = {
        'title': request.POST['title'],
        'description': request.POST['description'],
        'rating': request.POST['rating'],
    }

    review_form = ReviewForm(review_submission)

    existing_review = Reviews.objects.filter(user=user, product=product)
    if existing_review:
        messages.error(request, 'You have already reviewed this product')

    else:
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = user
            review.product = product
            review.save()

            reviews = Reviews.objects.filter(product=product)
            avg_rating = reviews.aggregate(Avg('rating'))['rating__avg']
            product.avg_rating = int(avg_rating)
            product.save()

            messages.success(request, 'Success! Your review has been added!')

        else:
            messages.error(request, 'Error! Make sure the form information is valid.')

    return redirect(reverse('product_detail', args=(product_id,)))
