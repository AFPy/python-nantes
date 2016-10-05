"""Module de test celery."""

from celery import Celery

app = Celery('tasks', broker='redis://', backend='redis://')
app.conf.update(
    CELERY_TASK_SERIALIZER='json',
    CELERY_ACCEPT_CONTENT=['json'],  # Ignore other content
    CELERY_RESULT_SERIALIZER='json',
    CELERY_TIMEZONE='Europe/Paris',
    CELERY_ENABLE_UTC=True,
)


@app.task
def palindrome(chaine):
    """Verifie que la chaine est un palindrome."""
    return chaine == chaine[::-1]


@app.task
def add(x, y):
    """Additionne deux nombres."""
    return x + y


@app.task
def total(chiffres):
    """Retourne la somme des chiffres."""
    return sum(chiffres)
