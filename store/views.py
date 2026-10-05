from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User as DjangoUser
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.db.models import Q
from django.utils.http import url_has_allowed_host_and_scheme
from .models import Game, Category, Order, OrderItem, Wishlist, Review
from .translations import get_text


def _t(request, key):
    lang = request.session.get('lang', 'ru')
    return get_text(lang, key)


def home(request):
    category_id = request.GET.get('category')
    search_query = request.GET.get('q', '')
    sort = request.GET.get('sort', '')

    games = Game.objects.all()
    categories = Category.objects.all()

    if category_id:
        games = games.filter(category_id=category_id)

    if search_query:
        games = games.filter(
            Q(title__icontains=search_query) |
            Q(description__icontains=search_query)
        )

    if sort == 'newest':
        games = games.order_by('-id')
    elif sort == 'price_asc':
        games = sorted(games, key=lambda g: g.final_price)
    elif sort == 'price_desc':
        games = sorted(games, key=lambda g: g.final_price, reverse=True)

    wishlist_ids = []
    if request.user.is_authenticated:
        wishlist_ids = list(
            Wishlist.objects.filter(user=request.user).values_list('game_id', flat=True)
        )

    context = {
        'games': games,
        'categories': categories,
        'selected_category': category_id,
        'search_query': search_query,
        'sort': sort,
        'wishlist_ids': wishlist_ids,
    }
    return render(request, 'store/home.html', context)

    
def game_detail(request, pk):
    game = get_object_or_404(Game, pk=pk)
    related_games = Game.objects.filter(category=game.category).exclude(pk=pk)[:4]

    in_wishlist = False
    can_review = False
    user_review = None
    if request.user.is_authenticated:
        in_wishlist = Wishlist.objects.filter(user=request.user, game=game).exists()
        can_review = OrderItem.objects.filter(
            order__user=request.user, order__is_paid=True, game=game
        ).exists()
        user_review = Review.objects.filter(user=request.user, game=game).first()

    context = {
        'game': game,
        'related_games': related_games,
        'in_wishlist': in_wishlist,
        'reviews': game.reviews.select_related('user'),
        'can_review': can_review,
        'user_review': user_review,
    }
    return render(request, 'store/game_detail.html', context)


def add_to_cart(request, game_id):
    cart = request.session.get('cart', {})
    cart[str(game_id)] = cart.get(str(game_id), 0) + 1
    request.session['cart'] = cart
    messages.success(request, _t(request, 'msg_added'))
    return redirect('cart')


def cart_detail(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total_price = 0

    for game_id, quantity in cart.items():
        try:
            game = Game.objects.get(id=game_id)
            item_total = game.final_price * quantity
            total_price += item_total
            cart_items.append({
                'game': game,
                'quantity': quantity,
                'item_total': item_total,
            })
        except Game.DoesNotExist:
            continue

    context = {
        'cart_items': cart_items,
        'total_price': total_price,
    }
    return render(request, 'store/cart.html', context)


def remove_from_cart(request, game_id):
    cart = request.session.get('cart', {})
    if str(game_id) in cart:
        del cart[str(game_id)]
        request.session['cart'] = cart
        messages.info(request, _t(request, 'msg_removed'))
    return redirect('cart')


@login_required
def buy_now(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    request.session['cart'] = {str(game.pk): 1}
    return redirect('checkout')


@login_required
def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.warning(request, _t(request, 'msg_cart_empty'))
        return redirect('home')

    total_price = 0
    games_to_buy = []

    for game_id, quantity in cart.items():
        try:
            game = Game.objects.get(id=game_id)
            total_price += game.final_price * quantity
            games_to_buy.append((game, quantity))
        except Game.DoesNotExist:
            continue

    if request.method == 'POST':
        order = Order.objects.create(
            user=request.user,
            total_price=total_price,
            is_paid=True
        )

        for game, quantity in games_to_buy:
            for _ in range(quantity):
                OrderItem.objects.create(
                    order=order,
                    game=game
                )

        request.session['cart'] = {}
        messages.success(request, _t(request, 'msg_purchase_ok'))
        return redirect('my_orders')

    context = {
        'total_price': total_price,
        'items': [{'game': g, 'quantity': q} for g, q in games_to_buy],
    }
    return render(request, 'store/checkout.html', context)


@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'store/my_orders.html', {'orders': orders})


@login_required
def my_library(request):
    user_orders = Order.objects.filter(user=request.user, is_paid=True)
    purchased_games = Game.objects.filter(orderitem__order__in=user_orders).distinct()

    context = {
        'games': purchased_games,
    }
    return render(request, 'store/my_library.html', context)


@login_required
def toggle_wishlist(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    item = Wishlist.objects.filter(user=request.user, game=game).first()

    if item:
        item.delete()
        messages.info(request, _t(request, 'msg_wishlist_removed'))
    else:
        Wishlist.objects.create(user=request.user, game=game)
        messages.success(request, _t(request, 'msg_wishlist_added'))

    next_url = request.META.get('HTTP_REFERER', '/')
    if not url_has_allowed_host_and_scheme(next_url, allowed_hosts={request.get_host()}):
        next_url = '/'
    return redirect(next_url)


@login_required
def wishlist_view(request):
    games = Game.objects.filter(wishlist__user=request.user)
    return render(request, 'store/wishlist.html', {'games': games})


def settings_page(request):
    return render(request, 'store/settings.html')


def set_language(request, code):
    if code in ('ru', 'uz', 'en'):
        request.session['lang'] = code

    next_url = request.META.get('HTTP_REFERER', '/')
    if not url_has_allowed_host_and_scheme(next_url, allowed_hosts={request.get_host()}):
        next_url = '/'
    return redirect(next_url)


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, _t(request, 'msg_registered'))
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'store/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, _t(request, 'msg_welcome'))
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'store/login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.info(request, _t(request, 'msg_logged_out'))
    return redirect('home')

@login_required
def add_review(request, game_id):
    game = get_object_or_404(Game, pk=game_id)

    if request.method == 'POST':
        has_bought = OrderItem.objects.filter(
            order__user=request.user, order__is_paid=True, game=game
        ).exists()

        if has_bought:
            try:
                rating = int(request.POST.get('rating', 0))
            except ValueError:
                rating = 0
            comment = request.POST.get('comment', '').strip()[:1000]

            if 1 <= rating <= 5:
                Review.objects.update_or_create(
                    user=request.user,
                    game=game,
                    defaults={'rating': rating, 'comment': comment},
                )
                messages.success(request, _t(request, 'msg_review_saved'))

    return redirect('game_detail', pk=game.pk)

@login_required
def profile_view(request):
    password_form = PasswordChangeForm(user=request.user)

    if request.method == 'POST':
        if 'save_account' in request.POST:
            new_username = request.POST.get('new_username', '').strip()
            new_email = request.POST.get('new_email', '').strip()

            if new_username and new_username != request.user.username:
                if DjangoUser.objects.filter(username=new_username).exclude(pk=request.user.pk).exists():
                    messages.error(request, _t(request, 'username_taken'))
                    return render(request, 'store/profile.html', {'password_form': password_form})
                request.user.username = new_username

            request.user.email = new_email
            request.user.save()
            messages.success(request, _t(request, 'msg_username_changed'))
            return redirect('profile')

        elif 'change_password' in request.POST:
            password_form = PasswordChangeForm(user=request.user, data=request.POST)
            if password_form.is_valid():
                user = password_form.save()
                update_session_auth_hash(request, user)
                messages.success(request, _t(request, 'msg_password_changed'))
                return redirect('profile')

    return render(request, 'store/profile.html', {'password_form': password_form})