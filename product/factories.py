import factory
from product.models import Category, Product


class CategoryFactory(factory.django.DjangoModelFactory):
    title = factory.Faker("pystr")
    slug = factory.Faker("slug")
    description = factory.Faker("sentence")
    active = factory.Iterator([True, False])

    class Meta:
        model = Category


class ProductFactory(factory.django.DjangoModelFactory):
    title = factory.Faker("pystr")
    price = factory.Faker("pyint")

    @factory.post_generation
    def category(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for category in extracted:
                self.category.add(category)
        else:
            # Se nenhuma categoria for passada, cria e adiciona uma automaticamente
            self.category.add(CategoryFactory())

    class Meta:
        model = Product
