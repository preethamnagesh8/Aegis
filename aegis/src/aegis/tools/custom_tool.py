from crewai_tools import BaseTool
from pydantic import BaseModel, Field
from typing import Any, Optional, Type
import requests
import os
import configparser

config = configparser.ConfigParser()
config_path = os.path.join(os.path.dirname(__file__), "..", "settings", "aegis_config.local")
config.read(config_path)

class WordPressCreateBlogSchema(BaseModel):
    """Input for WordPressCreateBlog"""
    title: str = Field(..., description = "Mandatory title field for blog")
    content: str = Field(..., description = "Mandatory body with text data for blog")


class WordPressCreateBlog(BaseTool):
    name: str = "Post a blog in wordpress"
    description: str = (
        "A tool that can post a blog to wordpress. This is an API call that makes a POST request to post data to wordpress site."
    )
    args_schema: Type[BaseModel] = WordPressCreateBlogSchema

    def _run(self, title: str, content: str) -> str:
        
        data = {
            "title": title,
            "content": content
        }

        wordpress_api_token = config.get("wordpress", "wordpress_api_key")
        blog_post_url = config.get("wordpress", "wordpress_blog_post_url")

        headers = {
            "Authorization": f"Bearer {wordpress_api_token}",
            "Content-Type": "application/json"
        }

        response = requests.post(blog_post_url, json=data, headers=headers)
        return response.text