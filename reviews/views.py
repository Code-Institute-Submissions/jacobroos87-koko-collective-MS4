from django.shortcuts import redirect, reverse, get_object_or_404
from django.db.models import Avg
from django.contrib import messages
from decimal import Decimal
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
            product.avg_rating = Decimal(avg_rating)
            product.save()

            messages.success(request, 'Success! Your review has been added!')

        else:
            messages.error(request, 'Error! Make sure the form information is valid.')

    return redirect(reverse('product_detail', args=(product_id,)))


def edit_review(request, review_id, product_id):
    review = get_object_or_404(Reviews, pk=review_id)
    if review.user is not request.user:
        messages.error(request, "You do not have permission to do this.")
        return redirect(reverse("product_detail", args=(product_id,)))
    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        product = Product.objects.get(name=review.product)
        if form.is_valid():
            review.save()

            reviews = Reviews.objects.filter(product=product)
            avg_rating = reviews.aggregate(Avg('rating'))['rating__avg']
            product.avg_rating = Decimal(avg_rating)
            product.save()

            messages.success(request, "Your review has been updated.")
        else:
            messages.error(request,
                           "Unable to update review, please try again.")

        return redirect(reverse('product_detail', args=(review.product_id,)))
