# Jack's Poetic Blog

A Flask-based blog application with image handling capabilities, designed for sharing poetry and creative content.

## 🚀 Features

- **Blog Post Management**: Create, edit, and manage blog posts with markdown support
- **Image Upload & Processing**: Upload images with automatic HEIC to JPEG conversion
- **Responsive Design**: Modern, mobile-friendly interface
- **Docker Support**: Containerized deployment ready
- **Nginx Integration**: Production-ready web server configuration

## 📁 Project Structure

```
jackspoetic/
├── app.py                 # Main Flask application
├── new_post.py           # Blog post creation utility
├── upload_image.py       # Image upload and processing utility
├── convert_heic.py       # HEIC to JPEG conversion utility
├── requirements.txt      # Python dependencies
├── Dockerfile           # Docker container configuration
├── .dockerignore        # Docker ignore file
├── jackspoetic.com.conf # Nginx configuration
├── setup.sh             # Initial setup script
├── static/              # Static assets (CSS, JS, images)
├── templates/           # HTML templates
├── posts/               # Blog post markdown files
├── venv/                # Python virtual environment
└── .gitignore          # Git ignore rules
```

## 🛠️ Setup Instructions

### Prerequisites

- Python 3.8+
- pip (Python package manager)
- Git
- Docker (optional, for containerized deployment)

### Local Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/jackkru/jackspoetic.git
   cd jackspoetic
   ```

2. **Create and activate virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Access the blog**
   - Open your browser and go to `http://localhost:5000`

### Docker Deployment

1. **Build the Docker image**
   ```bash
   docker build -t jackspoetic .
   ```

2. **Run the container**
   ```bash
   docker run -p 5000:5000 jackspoetic
   ```

### Production Deployment with Nginx

1. **Copy Nginx configuration**
   ```bash
   sudo cp jackspoetic.com.conf /etc/nginx/sites-available/
   sudo ln -s /etc/nginx/sites-available/jackspoetic.com.conf /etc/nginx/sites-enabled/
   ```

2. **Test and reload Nginx**
   ```bash
   sudo nginx -t
   sudo systemctl reload nginx
   ```

## 📝 Usage Guide

### Creating New Blog Posts

Use the `new_post.py` utility to create new blog posts:

```bash
python new_post.py "Your Post Title"
```

This will:
- Create a new markdown file in the `posts/` directory
- Generate a unique filename based on the title
- Add frontmatter with title, date, and author information

### Uploading Images

Use the `upload_image.py` utility to upload and process images:

```bash
python upload_image.py path/to/your/image.jpg
```

Features:
- Automatic HEIC to JPEG conversion
- Image optimization
- Organized storage in `static/images/`

### HEIC Image Conversion

For bulk HEIC conversion, use the dedicated utility:

```bash
python convert_heic.py input_directory output_directory
```

## 🔧 Development Process

### Initial Setup (Completed)

1. **Project Structure**: Created organized directory structure for Flask application
2. **Virtual Environment**: Set up Python virtual environment for dependency isolation
3. **Dependencies**: Installed required packages (Flask, Pillow, etc.)
4. **Git Repository**: Initialized Git repository with proper `.gitignore`
5. **GitHub Integration**: Connected local repository to GitHub remote

### Key Features Implemented

1. **Flask Application** (`app.py`)
   - Main application with routing
   - Blog post rendering from markdown
   - Image serving capabilities

2. **Blog Post Management** (`new_post.py`)
   - Automated post creation
   - Markdown frontmatter generation
   - Consistent file naming

3. **Image Processing** (`upload_image.py`, `convert_heic.py`)
   - HEIC to JPEG conversion
   - Image upload handling
   - File organization

4. **Deployment Configuration**
   - Docker containerization
   - Nginx production configuration
   - Environment setup scripts

## 🌐 Web Interface

The blog features a clean, responsive design with:
- **Homepage**: Displays all blog posts with excerpts
- **Individual Posts**: Full post view with markdown rendering
- **Image Gallery**: Organized image display
- **Mobile-Friendly**: Responsive design for all devices

## 📦 Dependencies

- **Flask**: Web framework
- **Pillow**: Image processing
- **Markdown**: Markdown rendering
- **python-dateutil**: Date parsing and formatting

## 🔒 Security Considerations

- Virtual environment isolation
- Proper file permissions
- Input validation for uploads
- Secure Nginx configuration

## 🚀 Deployment Checklist

- [x] Local development environment
- [x] Git repository setup
- [x] GitHub remote configuration
- [x] Docker containerization
- [x] Nginx production configuration
- [x] Documentation

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

**Jack Kru** - [GitHub Profile](https://github.com/jackkru)

---

*Built with ❤️ using Flask and modern web technologies* 