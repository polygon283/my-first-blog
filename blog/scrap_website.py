import requests
from bs4 import BeautifulSoup

import os
import sys
import django

sys.path.append('/Users/akaunntomei/Desktop/djangogirls')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangogirls.settings')
django.setup()


from blog.models import Post

#スクレイピングのメソッドを作成
def scrap_recipe():
    
    url = 'https://www.orangepage.net/recipes/search/421?page={}'
    target_url = url.format(1)
    res = requests.get(target_url)

    soup = BeautifulSoup(res.text)
    recipe_list = soup.find('div',class_='recipesList recipesList--list active' )
    recipes = recipe_list.find_all('li')
#取ってきたレシピの最初をレシピに格納    
    recipe = recipes[0]

#レシピからタイトルを取り出す
    recipe_title = recipe.find('h2',class_='tit').text

#レシピからレシピのテキストを取り出す
    recipe_text = recipe.find('p',class_='txt').text

    post = Post(title=recipe_title,text=recipe_text)
    post.save()

    


