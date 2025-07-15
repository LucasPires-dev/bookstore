import factory
from django.contrib.auth.models import User
from core.models import Product, Category


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f"user{n}")
    is_superuser = False
    is_staff = False

    @factory.post_generation
    def set_password(obj, create, extracted, **kwargs):
        obj.set_password("testpass")
        if create:
            obj.save()


class SuperUserFactory(UserFactory):
    is_superuser = True
    is_staff = True


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    title = factory.Sequence(lambda n: f"Category {n}")
    slug = factory.Sequence(lambda n: f"category-{n}")
    description = factory.Faker("sentence")
    active = True

class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    title = factory.Sequence(lambda n: f"Product {n}")
    price = factory.Faker("pydecimal", left_digits=3, right_digits=2, positive=True)
    active = True
    category = factory.SubFactory(CategoryFactory)
