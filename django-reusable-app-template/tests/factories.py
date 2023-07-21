import factory


# test models factories

class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'auth.User'
        django_get_or_create = ('email', )

    username = factory.Faker('user_name')
    email = factory.Faker('email')
    password = factory.Faker('password')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')


class AuthorFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'myapp.Author'
        django_get_or_create = ('first_name', 'last_name', )

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')


class ArticleFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'myapp.Article'
        django_get_or_create = ('title', 'pub_date', )

    title = factory.Faker('sentence')
    pub_date = factory.Faker('date_time')
    author = factory.SubFactory(AuthorFactory)

    # Use: ArticleFactory.create(comments=(comment1, comment2))
    @factory.post_generation
    def comments(self, create, extracted, **kwargs):
        if not create or not extracted:
            # Simple build, or nothing to add, do nothing.
            return

        # Add the iterable of comments using bulk addition
        self.comments.add(*extracted)


class CommentFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'myapp.Comment'
        django_get_or_create = ('text', 'pub_date', )

    text = factory.Faker('text')
    pub_date = factory.Faker('date_time')
    article = factory.SubFactory(ArticleFactory)
    approval_date = factory.Faker('date_time')
