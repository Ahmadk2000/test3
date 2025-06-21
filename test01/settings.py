from pathlib import Path
import os
import cloudinary

# المسار الأساسي للمشروع
BASE_DIR = Path(__file__).resolve().parent.parent

# مفتاح الأمان (غيّره في الإنتاج)
SECRET_KEY = 'django-insecure-_293era6fk@kxu1#4_)$s6qr^aa8q%s!e)jxafk7&_u#$!jx*9'

# وضع التطوير
DEBUG = True

# قائمة النطاقات المسموحة
ALLOWED_HOSTS = []

# التطبيقات المثبتة
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # التطبيقات الخاصة بالمشروع
    'accounts',
    'products',
    'orders',
]

# الوسيطات (Middleware)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# مسار ملف URL الرئيسي
ROOT_URLCONF = 'test01.urls'

# إعدادات القوالب (templates)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# تطبيق WSGI
WSGI_APPLICATION = 'test01.wsgi.application'

# إعدادات قاعدة البيانات
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# التحقق من كلمات المرور
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# اللغة والتوقيت
LANGUAGE_CODE = 'ar'
TIME_ZONE = 'Asia/Riyadh'
USE_I18N = True
USE_TZ = True

# مسارات ملفات الترجمة
LOCALE_PATHS = [BASE_DIR / 'locale']

# الملفات الثابتة
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

# رفع الملفات
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# إعداد Cloudinary
cloudinary.config( 
  cloud_name = 'deq8mpu9f', 
  api_key = '272932535551661', 
  api_secret = '7blVhj-xhH8MYv4_NXmi3RU4xF4' 
)

# نوع المفتاح الافتراضي
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
