from armstrong.dev.tests.utils import ArmstrongTestCase
from armstrong.dev.tests.utils.users import generate_random_staff_users


class ArmContentTestCase(ArmstrongTestCase):
    pass


def add_profile_to(profile_class, *users):
    for user in users:
        profile = profile_class.objects.create(user=user)
        user._profile_cache = profile


def add_authors_to(model, *authors):
    for author in authors:
        model.authors.add(author)


def random_authored_model(klass, *authors):
    article = klass.objects.create()
    add_authors_to(article, *authors)
    return article
