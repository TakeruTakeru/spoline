import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DEBUG = True
SECRET_KEY = "q1shjhzv0@v_n_4sqi!6)n2j@s8c#(%_cd*(_5pesd@4*58)u%"
