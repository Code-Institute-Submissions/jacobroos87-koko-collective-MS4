from django.shortcuts import redirect, reverse, get_object_or_404
from django.db.models import Avg
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from decimal import Decimal
from .models import Reviews
from .forms import ReviewForm
from products.models import Product
from profiles.models import UserProfile


@login_required
def add_review(request, product_id):
    user = UserProfile.objects.get(user=request.user)
    product = get_object_or_404(Product, pk=product_id)

    review_form = ReviewForm()
    # Get info from form
    review_submission = {
        'title': request.POST['title'],
        'description': request.POST['description'],
        'rating': request.POST['rating'],
    }

    review_form = ReviewForm(review_submission)
    # Prevents a user from reviewing the same product twice
    existing_review = Reviews.objects.filter(user=user, product=product)
    if existing_review:
        messages.error(request, 'You have already reviewed this product')

    else:
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = user
            review.product = product
            review.save()
            # Update average rating
            reviews = Reviews.objects.filter(product=product)
            avg_rating = reviews.aggregate(Avg('rating'))['rating__avg']
            product.avg_rating = Decimal(avg_rating)
            product.save()

            messages.info(request, 'Success! Your review has been added!')

        else:
            messages.error(
                request, 'Error! Make sure the form information is valid.')

    return redirect(reverse('product_detail', args=(product_id,)))


@login_required
def edit_review(request, review_id):
    review = get_object_or_404(Reviews, pk=review_id)
    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        product = Product.objects.get(name=review.product)
        if form.is_valid():
            review.save()

            reviews = Reviews.objects.filter(product=product)
            avg_rating = reviews.aggregate(Avg('rating'))['rating__avg']
            product.avg_rating = Decimal(avg_rating)
            product.save()

            messages.info(request, "Your review has been updated.")
        else:
            messages.error(request,
                           "Unable to update review, please try again.")

        return redirect(reverse(
                                'product_detail', args=(review.product.id,)))


@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Reviews, pk=review_id)
    product = Product.objects.get(name=review.product)

    try:
        review.delete()

        reviews = Reviews.objects.filter(product=product)
        avg_rating = reviews.aggregate(Avg('rating'))['rating__avg']
        if avg_rating:
            product.avg_rating = Decimal(avg_rating)
        else:
            product.avg_rating = 0
        product.save()

        messages.info(request,
                      "Your review has been deleted")

    except Exception as e:
        messages.error(request, "We couldn't delete your review because "
                                f" error:{e} occured.")
    return redirect(reverse('product_detail', args=(review.product.id,)))
