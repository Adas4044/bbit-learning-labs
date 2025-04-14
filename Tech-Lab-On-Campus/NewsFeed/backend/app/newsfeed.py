"""Module for retrieving newsfeed information."""

from dataclasses import dataclass
from datetime import datetime


@dataclass
class Article:
    """Dataclass for an article."""

    author: str
    title: str
    body: str
    publish_date: datetime
    image_url: str
    url: str


def get_all_news() -> list[Article]:
    """Get all news articles from the datastore."""

        # FROM REDIS CLIENT:
        # def get_entry(self, key: str) -> Optional[Any]:
        # """
        # Retrieve an entry from Redis using a connection from the pool.

        # Args:
        #     key (str): Key to retrieve

        # Returns   
        # -------
        #     Optional[Any]: Retrieved value (JSON deserialized) or None if not found
        # """
    # 1. Use Redis client to fetch all articles
    raw_articles = REDIS_CLIENT.get_entry("all_articles")
    if not raw_articles:
        return []

    # 2. Format the data into articles
    articles: list[Article] = []
    for data in raw_articles:
        try:
            published = data.get("thread", {}).get("published")
            if published:
                # Adding published field to top level if we need
                data["published"] = published
            article = Article(**data)
            articles.append(article)
        except Exception as e:
            print(f"Skipping invalid article: {e}")

    # 3. Return a list of the articles formatted 
    articles.sort(
        key=lambda a: datetime.fromisoformat(a.published),
        reverse=True
    )

    return articles

def _get_connection(self) -> redis.Redis:
    
    #redis = RedisClient()
    #return []
    return []


def get_featured_news() -> Article | None:
    """Get the featured news article from the datastore."""
    # 1. Get all the articles
    # 2. Return as a list of articles sorted by most recent date

    articles = get_all_news()

    if articles:
        return articles[0]