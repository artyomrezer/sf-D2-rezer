'''
(venv) E:\Образование\Учеба SkillFactory\Раздел D NewsPaper_PROJECT\NewsPaper>
python manage.py shell 
from news.models import *

user1 = User.objects.create(username='user_1', first_name='user_1_FirstName')
Author.objects.create(authorUser=user1)
user2 = User.objects.create(username='user_2', first_name='user_2_FirstName')
Author.objects.create(authorUser=user2)

Category.objects.create(name='Образование')
Category.objects.create(name='Машиностроение')
Category.objects.create(name='Информационные технологии')
Category.objects.create(name='Медицина')

Post.objects.create(author=Author.objects.get(authorUser=User.objects.get(username='Veralt')), categoryType='NW', title='tratata title', text='tratata text')
Post.objects.create(author=Author.objects.get(authorUser=User.objects.get(username='user_2')), categoryType='AR', title='Новый язык программирования', text='Текст статьи про новый язык программирования')
Post.objects.create(author=Author.objects.get(authorUser=User.objects.get(username='user_1')), categoryType='NW', title='Налажен выпуск новых станков', text='На предприятии налажен выпуск новых станков')

article1 = Post.objects.get(pk=1)
article2 = Post.objects.get(pk=2)
news1 = Post.objects.get(pk=3)
article1_cat1 = Category.objects.get(name='Образование')
article1_cat2 = Category.objects.get(name='Медицина')
article2_cat1 = Category.objects.get(name='Информационные технологии')
article2_cat2 = Category.objects.get(name='Образование')
news1_cat1 = Category.objects.get(name='Машиностроение')
news1_cat2 = Category.objects.get(name='Информационные технологии')

article1.postCategory.add(article1_cat1, article1_cat2)
article2.postCategory.add(article2_cat1, article2_cat2)
news1.postCategory.add(news1_cat1, news1_cat2)

Comment.objects.create(commentUser=User.objects.get(username='user_1'), commentPost = Post.objects.get(pk=1), text='коммент к статье 1')
Comment.objects.create(commentUser=User.objects.get(username='user_2'), commentPost = Post.objects.get(pk=2), text='коммент к статье 2')
Comment.objects.create(commentUser=User.objects.get(username='user_1'), commentPost = Post.objects.get(pk=3), text='коммент к новости 1')
Comment.objects.create(commentUser=User.objects.get(username='user_2'), commentPost = Post.objects.get(pk=3), text='еще один коммент к новости 1')

Post.objects.get(pk=1).like()
Post.objects.get(pk=1).like()
Post.objects.get(pk=1).like()
Post.objects.get(pk=1).like()
Post.objects.get(pk=2).like()
Post.objects.get(pk=2).like()
Post.objects.get(pk=2).like()
Post.objects.get(pk=2).like()
Post.objects.get(pk=3).like()
Post.objects.get(pk=3).like()
Post.objects.get(pk=3).like()
Post.objects.get(pk=3).like()
Post.objects.get(pk=2).dislike()
Post.objects.get(pk=1).dislike()
Comment.objects.get(pk=1).like()
Comment.objects.get(pk=1).like()
Comment.objects.get(pk=1).dislike()
Comment.objects.get(pk=2).like()
Comment.objects.get(pk=2).like()
Comment.objects.get(pk=2).like()
Comment.objects.get(pk=2).dislike()
Comment.objects.get(pk=3).like()
Comment.objects.get(pk=1).dislike()
Comment.objects.get(pk=2).dislike()
Comment.objects.get(pk=3).dislike()
Comment.objects.get(pk=1).like()
Comment.objects.get(pk=2).like()
Comment.objects.get(pk=3).like()

Author.objects.get(authorUser = User.objects.get(username="user_1")).update_rating()
Author.objects.get(authorUser = User.objects.get(username="user_2")).update_rating()

Author.objects.get(authorUser = User.objects.get(username="user_1")).ratingAuthor
Author.objects.get(authorUser = User.objects.get(username="user_2")).ratingAuthor

# вывод имя и рейтинг лучшего пользователя
best_authot_rating = Author.objects.all().order_by('-ratingAuthor').values('authorUser', 'ratingAuthor')[0]
# pk лучшего автора
best_author_pk = list(Author.objects.all().order_by('-ratingAuthor').values('authorUser')[0].values())[0]
#вывод имени лучшего пользователя
print(Author.objects.all().order_by('-ratingAuthor')[0].authorUser.username)) 

# вывод информации о лучшей статье
best_article = Post.objects.all().order_by('-rating').values('dateCreation','author', 'rating', 'text')[0]
print(best_article)

# вывод всех комментариев к лучшей статье
Comment.objects.filter(commentPost=Post.objects.all().order_by('-rating')[0])

''' 