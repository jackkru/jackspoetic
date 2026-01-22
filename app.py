from flask import Flask, render_template, abort, send_from_directory, redirect, url_for, request, session, jsonify
import os
import markdown
from datetime import datetime
import glob
import requests

# Get the base directory (where app.py is located)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__, static_folder=os.path.join(BASE_DIR, 'static'))

# Enable auto-reload for development
app.config['TEMPLATES_AUTO_RELOAD'] = True

# Blog posts directory
POSTS_DIR = os.path.join(BASE_DIR, 'posts')

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

@app.route("/api/subscribe", methods=["POST"])
def subscribe():
    """Handle email subscription requests via Buttondown API"""
    try:
        data = request.get_json()
        email = data.get('email', '').strip()

        if not email:
            return jsonify({'success': False, 'message': 'Email is required'}), 400

        # Get Buttondown API key from environment
        api_key = os.environ.get('BUTTONDOWN_API_KEY')
        if not api_key:
            return jsonify({'success': False, 'message': 'Subscription service not configured'}), 500

        # Send request to Buttondown API
        response = requests.post(
            'https://api.buttondown.email/v1/subscribers',
            json={'email_address': email},
            headers={
                'Authorization': f'Token {api_key}',
                'Content-Type': 'application/json'
            },
            timeout=10
        )

        if response.status_code == 201:
            return jsonify({'success': True, 'message': 'Successfully subscribed! Check your email to confirm.'})
        elif response.status_code == 409:
            return jsonify({'success': False, 'message': 'This email is already subscribed.'})
        else:
            return jsonify({'success': False, 'message': 'Unable to subscribe. Please try again later.'}), 500

    except requests.exceptions.Timeout:
        return jsonify({'success': False, 'message': 'Request timed out. Please try again.'}), 500
    except Exception as e:
        print(f"Subscription error: {e}")
        return jsonify({'success': False, 'message': 'An error occurred. Please try again later.'}), 500

# Flask automatically serves static files from static_folder at /static/
# But we'll keep explicit routes for better control and debugging
@app.route('/static/<path:filename>')
def static_files(filename):
    try:
        return send_from_directory(os.path.join(BASE_DIR, 'static'), filename)
    except Exception as e:
        # Log error for debugging
        print(f"Error serving static file {filename}: {e}")
        abort(404)

def get_posts():
    """Get all blog posts sorted by date"""
    posts = []
    if not os.path.exists(POSTS_DIR):
        return posts
    
    for filename in glob.glob(os.path.join(POSTS_DIR, "*.md")):
        post = parse_post(filename)
        if post:
            posts.append(post)
    
    # Sort by date (newest first) - convert string dates to datetime objects
    def parse_date(date_str):
        try:
            return datetime.strptime(date_str, '%Y-%m-%d')
        except (ValueError, TypeError):
            return datetime.min  # Fallback for invalid dates
    
    posts.sort(key=lambda x: parse_date(x['date']), reverse=True)
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
        html_content = markdown.markdown(markdown_content, extensions=['fenced_code', 'tables', 'codehilite', 'footnotes'])
        
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
    app.run(host="0.0.0.0", port=5000, debug=True)
