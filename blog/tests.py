from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Post, Category


# Create your tests here.
class Test_Creating_Post(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        test_category = Category.objects.create(name="django")
        testUser = User.objects.create_user(username="Roman", password="666999")
        test_post = Post.objects.create(
            category_id=1,
            title="Testing title",
            excerpt="Post excerpt",
            content="Test content",
            status="published",
            author=testUser,
        )

    def test_post_content(self):
        post = Post.postobjects.get(id=1)
        category = Category.objects.get(id=1)
        author = f"{post.author}"
        title = f"{post.title}"
        content = f"{post.content}"
