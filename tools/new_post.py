#!/usr/bin/env python3
"""
Simple script to create new blog posts
Usage: python3 new_post.py "Post Title"
"""

import sys
import os
from datetime import datetime
import re

def slugify(title):
    """Convert title to URL-friendly slug"""
    slug = re.sub(r'[^\w\s-]', '', title.lower())
    slug = re.sub(r'[-\s]+', '-', slug)
    return slug.strip('-')

def create_post(title):
    """Create a new blog post with the given title"""
    if not title:
        print("Please provide a title for the post")
        print("Usage: python3 new_post.py \"Post Title\"")
        return
    
    # Create slug from title
    slug = slugify(title)
    filename = f"posts/{slug}.md"
    
    # Check if file already exists
    if os.path.exists(filename):
        print(f"Error: Post '{filename}' already exists!")
        return
    
    # Get current date
    date = datetime.now().strftime("%Y-%m-%d")
    
    # Create frontmatter
    frontmatter = f"""---
title: {title}
date: {date}
author: Jack
excerpt: Add a brief excerpt of your post here.
---

# {title}

Write your blog post content here using Markdown.

## Subheading

You can use:
- **Bold text**
- *Italic text*
- `Code snippets`
- [Links](https://example.com)

> Blockquotes for important quotes

### Code blocks

```python
def hello_world():
    print("Hello, World!")
```

---

*Thanks for reading!*
"""
    
    # Write the file
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(frontmatter)
    
    print(f"✅ Created new blog post: {filename}")
    print(f"📝 Edit the file to add your content")
    print(f"🌐 Your post will be available at: /blog/{slug}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a title for the post")
        print("Usage: python3 new_post.py \"Post Title\"")
    else:
        title = sys.argv[1]
        create_post(title) 