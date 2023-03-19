import os
from markdown import markdown
from jinja2 import Environment, FileSystemLoader
from data import cv, posts


def main():
    env = Environment(loader=FileSystemLoader("templates"))
    # base_template = env.get_template("base.html")
    cv_template = env.get_template("cv.html")
    blog_post_template = env.get_template("blog_post.html")

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

    # Generate Index
    index_template = env.get_template("index.html")
    index_output = index_template.render(posts=posts, title="Lemniscata 2023")
    with open("output/index.html", "w") as f:
        f.write(index_output)


if __name__ == "__main__":
    main()
