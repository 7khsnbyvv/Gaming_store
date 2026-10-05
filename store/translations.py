DEFAULT_LANG = 'ru'
LANG_INDEX = {'ru': 0, 'uz': 1, 'en': 2}

# kalit: (Русский, O'zbekcha, English)
TEXTS = {
    # Menyu
    'nav_home': ("Главная", "Bosh sahifa", "Home"),
    'nav_store': ("Магазин", "Do'kon", "Store"),
    'nav_cart': ("Корзина", "Savat", "Cart"),
    'nav_library': ("Мои игры", "Mening o'yinlarim", "My games"),
    'nav_orders': ("Мои заказы", "Buyurtmalarim", "My orders"),
    'nav_login': ("Войти", "Kirish", "Log in"),
    'nav_register': ("Регистрация", "Ro'yxatdan o'tish", "Sign up"),
    'nav_logout': ("Выйти", "Chiqish", "Log out"),
    'nav_admin': ("Админ-панель", "Admin panel", "Admin panel"),
    'settings': ("Настройки", "Sozlamalar", "Settings"),
    'language': ("Язык", "Til", "Language"),

    # Bosh sahifa
    'hero_title': ("Магазин игр", "O'yinlar do'koni", "Game store"),
    'hero_sub': ("Лучшие игры по лучшим ценам", "Eng yaxshi o'yinlar eng yaxshi narxlarda", "The best games at the best prices"),
    'search_placeholder': ("Поиск игр...", "O'yin qidirish...", "Search games..."),
    'all_categories': ("Все категории", "Barcha kategoriyalar", "All categories"),
    'search_btn': ("Найти", "Qidirish", "Search"),
    'no_games': ("Игры не найдены.", "O'yinlar topilmadi.", "No games found."),
    'details': ("Подробнее", "Batafsil", "Details"),
    'add_to_cart': ("В корзину", "Savatga", "Add to cart"),
    'buy_now': ("Купить", "Sotib olish", "Buy"),
    'free': ("Бесплатно", "Bepul", "Free"),
    'off': ("СКИДКА", "CHEGIRMA", "OFF"),

    # Kutubxona
    'library_title': ("Мои игры", "Mening o'yinlarim", "My games"),
    'library_empty': ("У вас пока нет купленных игр.", "Sizda hali sotib olingan o'yinlar yo'q.", "You haven't bought any games yet."),
    'go_catalog': ("Перейти в каталог", "Katalogga o'tish", "Go to the catalog"),
    'open': ("Открыть", "Ochish", "Open"),

    # Savat va xarid
    'cart_title': ("Корзина", "Savat", "Shopping cart"),
    'cart_empty': ("Ваша корзина пуста.", "Savatingiz bo'sh.", "Your cart is empty."),
    'col_game': ("Игра", "O'yin", "Game"),
    'price': ("Цена", "Narxi", "Price"),
    'col_qty': ("Кол-во", "Soni", "Qty"),
    'total': ("Итого", "Jami", "Total"),
    'remove': ("Удалить", "O'chirish", "Remove"),
    'checkout_btn': ("Оформить заказ", "Buyurtma berish", "Checkout"),
    'continue_shopping': ("Продолжить покупки", "Xaridni davom ettirish", "Continue shopping"),
    'checkout_title': ("Оформление заказа", "Buyurtmani rasmiylashtirish", "Checkout"),
    'confirm_purchase': ("Подтвердить покупку", "Xaridni tasdiqlash", "Confirm purchase"),
    'back_to_cart': ("Назад в корзину", "Savatga qaytish", "Back to cart"),

    # To'lov oynasi
    'card_number': ("Номер карты", "Karta raqami", "Card number"),
    'expiry': ("Срок действия", "Amal qilish muddati", "Expiry"),
    'cvv': ("CVV", "CVV", "CVV"),
    'cardholder': ("Имя владельца", "Egasining ismi", "Cardholder name"),
    'processing': ("Обработка...", "Toʻlov bajarilmoqda...", "Processing..."),
    'pay_amount': ("Оплатить", "Toʻlash", "Pay"),

    # Buyurtmalar
    'orders_title': ("Мои заказы", "Mening buyurtmalarim", "My orders"),
    'orders_empty': ("У вас пока нет заказов.", "Sizda hali buyurtmalar yo'q.", "You have no orders yet."),
    'order_label': ("Заказ", "Buyurtma", "Order"),
    'paid': ("Оплачен", "To'langan", "Paid"),
    'not_paid': ("Не оплачен", "To'lanmagan", "Not paid"),
    'activation_key': ("Ключ активации", "Aktivatsiya kaliti", "Activation key"),

    # O'yin sahifasi
    'category': ("Категория", "Kategoriya", "Category"),
    'related_games': ("Похожие игры", "O'xshash o'yinlar", "Related games"),
    'back_home': ("На главную", "Bosh sahifaga", "Back to home"),

    # Kirish / ro'yxatdan o'tish
    'login_title': ("Вход", "Kirish", "Log in"),
    'register_title': ("Регистрация", "Ro'yxatdan o'tish", "Sign up"),
    'username': ("Имя пользователя", "Foydalanuvchi nomi", "Username"),
    'password': ("Пароль", "Parol", "Password"),
    'password_confirm': ("Повторите пароль", "Parolni takrorlang", "Confirm password"),
    'login_btn': ("Войти", "Kirish", "Log in"),
    'register_btn': ("Зарегистрироваться", "Ro'yxatdan o'tish", "Sign up"),
    'no_account': ("Нет аккаунта?", "Akkauntingiz yo'qmi?", "Don't have an account?"),
    'have_account': ("Уже есть аккаунт?", "Akkauntingiz bormi?", "Already have an account?"),
    'settings_guest': ("Войдите в аккаунт, чтобы покупать игры и видеть свою библиотеку.", "O'yin sotib olish va kutubxonangizni ko'rish uchun akkauntga kiring.", "Log in to buy games and see your library."),

    # Xabarlar
    'msg_added': ("Игра добавлена в корзину!", "O'yin savatga qo'shildi!", "Game added to the cart!"),
    'msg_removed': ("Игра удалена из корзины.", "O'yin savatdan olib tashlandi.", "Game removed from the cart."),
    'msg_cart_empty': ("Ваша корзина пуста!", "Savatingiz bo'sh!", "Your cart is empty!"),
    'msg_purchase_ok': ("Покупка успешно оформлена!", "Xarid muvaffaqiyatli amalga oshirildi!", "Purchase completed successfully!"),
    'msg_registered': ("Вы успешно зарегистрировались!", "Muvaffaqiyatli ro'yxatdan o'tdingiz!", "You have registered successfully!"),
    'msg_welcome': ("Добро пожаловать!", "Xush kelibsiz!", "Welcome!"),
    'msg_logged_out': ("Вы вышли из системы.", "Tizimdan chiqdingiz.", "You have logged out."),
    'profile_title': ("Профиль", "Profil", "Profile"),
    'change_username': ("Изменить имя пользователя", "Foydalanuvchi nomini o'zgartirish", "Change username"),
    'new_username': ("Новое имя пользователя", "Yangi foydalanuvchi nomi", "New username"),
    'change_password': ("Изменить пароль", "Parolni o'zgartirish", "Change password"),
    'old_password': ("Текущий пароль", "Joriy parol", "Current password"),
    'new_password': ("Новый пароль", "Yangi parol", "New password"),
    'new_password_confirm': ("Повторите новый пароль", "Yangi parolni takrorlang", "Confirm new password"),
    'save_changes': ("Сохранить", "Saqlash", "Save"),
    'msg_username_changed': ("Имя пользователя обновлено!", "Foydalanuvchi nomi yangilandi!", "Username updated!"),
    'msg_password_changed': ("Пароль успешно изменён!", "Parol muvaffaqiyatli o'zgartirildi!", "Password changed successfully!"),
    'username_taken': ("Это имя уже занято.", "Bu nom band.", "This username is already taken."),
    'email': ("Email", "Email", "Email"),
    'email_optional': ("Необязательно", "Ixtiyoriy", "Optional"),
    'want_change_password': ("Хотите изменить пароль?", "Parolni o'zgartirmoqchimisiz?", "Want to change your password?"),
    'cancel': ("Отмена", "Bekor qilish", "Cancel"),
    'msg_email_changed': ("Email обновлён!", "Email yangilandi!", "Email updated!"),
    'account_info': ("Данные аккаунта", "Akkaunt ma'lumotlari", "Account details"),
    'reviews_title': ("Отзывы", "Sharhlar", "Reviews"),
    'your_rating': ("Ваша оценка", "Sizning bahoyingiz", "Your rating"),
    'comment_placeholder': ("Напишите отзыв...", "Sharh yozing...", "Write a review..."),
    'submit_review': ("Отправить", "Yuborish", "Submit"),
    'review_need_purchase': ("Отзыв можно оставить после покупки игры.", "Sharh qoldirish uchun avval o'yinni sotib oling.", "Buy the game to leave a review."),
    'no_reviews': ("Отзывов пока нет.", "Hozircha sharhlar yo'q.", "No reviews yet."),
    'msg_review_saved': ("Отзыв сохранён!", "Sharh saqlandi!", "Review saved!"),
    'sort_default': ("Сортировка", "Saralash", "Sort by"),
    'sort_price_asc': ("Сначала дешевле", "Avval arzonlari", "Price: low to high"),
    'sort_price_desc': ("Сначала дороже", "Avval qimmatlari", "Price: high to low"),
    'sort_newest': ("Новинки", "Yangi qo'shilganlar", "Newest"),
    'wishlist_title': ("Избранное", "Sevimlilarim", "Wishlist"),
    'wishlist_empty': ("Список избранного пуст.", "Sevimlilar ro'yxati bo'sh.", "Your wishlist is empty."),
    'nav_wishlist': ("Избранное", "Sevimlilarim", "Wishlist"),
    'msg_wishlist_added': ("Добавлено в избранное!", "Sevimlilarga qo'shildi!", "Added to wishlist!"),
    'msg_wishlist_removed': ("Удалено из избранного.", "Sevimlilardan olib tashlandi.", "Removed from wishlist."),
}


def get_text(lang, key):
    values = TEXTS.get(key)
    if values is None:
        return key
    return values[LANG_INDEX.get(lang, 0)]