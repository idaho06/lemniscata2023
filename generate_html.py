#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from markdown import markdown
from bs4 import BeautifulSoup
from jinja2 import Environment, FileSystemLoader
from data import cv, posts, feed
from feedgen.feed import FeedGenerator
from datetime import datetime
import pytz


def main():
    env = Environment(loader=FileSystemLoader("templates"))
    # base_template = env.get_template("base.html")
    cv_template = env.get_template("cv.html")
    blog_post_template = env.get_template("blog_post.html")
    fg = FeedGenerator()
    fg.id(feed.get('id', 'no id'))
    fg.title(feed.get('title', 'no title'))
    fg.author(
        feed.get('author', {'name': 'John Doe', 'email': 'john@example.de'}))
    fg.subtitle(feed.get('subtitle', 'No Subtitle'))
    fg.description(feed.get('description', 'No description'))
    fg.link(href=feed.get('link', 'no Link'), rel='self')
    fg.language(feed.get('language', 'en-us'))

    # If output doesn't exist, create it
    if not os.path.exists("output"):
        os.makedirs("output")

    # Generate CV
    with open("input/cv.md", "r") as f:
        cv_md = f.read()
    cv_html = markdown(cv_md)
    cv_output = cv_template.render(cv=cv_html, title=cv["title"])
    with open("output/cv.html", "w") as f:
        f.write(cv_output)

    # If output/blog doesn't exist, create it
    if not os.path.exists("output/blog"):
        os.makedirs("output/blog")

    # Generate Blog Posts
    for post in posts:
        with open(post["filename"], "r") as f:
            blog_post_md = f.read()
        blog_post_html = markdown(blog_post_md)
        blog_post_output = blog_post_template.render(
            # post={"title": post["title"], "date": post["date"], "content": blog_post_html}, title=post["title"]
            post={
                "content": blog_post_html,
                "date": post["date"],
                "title": post["title"],
            },
            title=post["title"]
        )
        post_name = os.path.splitext(os.path.basename(post["filename"]))[0]
        with open(f"output/blog/{post_name}.html", "w") as f:
            f.write(blog_post_output)
        post["url"] = f"blog/{post_name}.html"

        fe = fg.add_entry()
        fe.id(f"{feed['link']}{post['url']}")
        fe.title(post["title"])
        fe.link(href=f"{feed['link']}{post['url']}")
        date_str = post["date"]
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        tz = pytz.timezone('UTC')
        date_obj = tz.localize(date_obj)
        fe.pubDate(date_obj)
        soup = BeautifulSoup(blog_post_html, 'html.parser')
        first_p_text = soup.find('p').text
        fe.description(first_p_text)
        fe.summary(first_p_text)

    # Generate Index
    index_template = env.get_template("index.html")
    index_output = index_template.render(posts=posts, title="Lemniscata 2023")
    with open("output/index.html", "w") as f:
        f.write(index_output)

    # Create Atom and Rss feeds
    atomfeed = fg.atom_str(pretty=True)  # Get the ATOM feed as string
    rssfeed = fg.rss_str(pretty=True)  # Get the RSS feed as string
    fg.atom_file('output/atom.xml')  # Write the ATOM feed to a file
    fg.rss_file('output/rss.xml')  # Write the RSS feed to a file


if __name__ == "__main__":
    main()
