from django.core.cache import cache

from apps.goods.models import Article



def article_cache(article_id, flag=False):
    # 缓存中获取数据
    alist = cache.get("alist")

    #  判断数据库是否更新,判断花奴你是否更新
    if alist is None or flag:
        # 查询数据库中的数据
        alist = Article.objects.get(id=article_id)

        # 同步到缓存
        cache.set("alist", alist)

    return alist
