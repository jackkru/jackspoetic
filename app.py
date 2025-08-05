from flask import Flask, render_template, abort, send_from_directory, redirect, url_for
import os
import markdown
from datetime import datetime
import glob

app = Flask(__name__, static_folder='static')

# Blog posts directory
POSTS_DIR = 'posts'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/blog")
def blog():
    posts = get_posts()
    return render_template("blog.html", posts=posts)

@app.route("/blog/<slug>")
def post(slug):
    post = get_post(slug)
    if not post:
        abort(404)
    return render_template("post.html", post=post)

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)

def get_posts():
    """Get all blog posts sorted by date"""
    posts = []
    if not os.path.exists(POSTS_DIR):
        return posts
    
    for filename in glob.glob(os.path.join(POSTS_DIR, "*.md")):
        post = parse_post(filename)
        if post:
            posts.append(post)
    
    # Sort by date (newest first)
    posts.sort(key=lambda x: x['date'], reverse=True)
    return posts

def get_post(slug):
    """Get a specific blog post by slug"""
    filename = os.path.join(POSTS_DIR, f"{slug}.md")
    if os.path.exists(filename):
        return parse_post(filename)
    return None

def parse_post(filename):
    """Parse a markdown file into a post dictionary"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Split frontmatter and content
        parts = content.split('---', 2)
        if len(parts) >= 3:
            frontmatter = parts[1].strip()
            markdown_content = parts[2].strip()
        else:
            # No frontmatter, treat entire file as content
            frontmatter = ""
            markdown_content = content
        
        # Parse frontmatter
        metadata = {}
        for line in frontmatter.split('\n'):
            if ':' in line:
                key, value = line.split(':', 1)
                metadata[key.strip()] = value.strip()
        
        # Get slug from filename
        slug = os.path.splitext(os.path.basename(filename))[0]
        
        # Convert markdown to HTML
        html_content = markdown.markdown(markdown_content, extensions=['fenced_code', 'tables', 'codehilite'])
        
        return {
            'title': metadata.get('title', 'Untitled'),
            'date': metadata.get('date', ''),
            'author': metadata.get('author', 'Unknown'),
            'excerpt': metadata.get('excerpt', ''),
            'content': html_content,
            'slug': slug
        }
    except Exception as e:
        print(f"Error parsing {filename}: {e}")
        return None

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
