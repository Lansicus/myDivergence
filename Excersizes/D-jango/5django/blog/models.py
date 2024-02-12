# blog/models.py
from django.db import models
from django.urls import reverse #

# Our table will be called "appname_modelname"
class Post(models.Model): # A Blog has a title, author, and body. 
    
    # Title Column -> CharField()
    title = models.CharField(max_length=200) 
    # this will be our column in our table `Post`

    # Author will be the user that logs-in and creates/modifies the Blog
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE, 
        # When the user is deleted in auth_user table all the blogs in the 
        # Post table assocaited with this author wil also be deleted.
    )

    # Body Column -> TextField()
    body = models.TextField()


    def __str__(self):
        return self.title[:75]
    # this will display 75 character of the text field in the 
    # Admin UI, you can store more characters in the database 
    # but in the Admin UI only the first 75 will show up.

    def get_absolute_url(self):
# Reverse is a very handy utility function Django provides us to reference 
# an object by its URL template name, in this case post_detail.
        return reverse('post_detail', args=[str(self.id)])
# path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
# pk and id are interchangeable
# redirects to URL path: posts/pk or posts/id
    