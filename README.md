# 📇 Contact Book

A modern, beautiful web-based contact management application built with Flask. Manage your contacts with style using this feature-rich application with a stunning UI.

## ✨ Features

- 📝 **Create Contacts** - Add new contacts with name, email, phone, and address
- 👀 **View Contacts** - Beautiful contact details page with avatar and organized information
- ✏️ **Edit Contacts** - Update contact information with an intuitive form
- 🗑️ **Delete Contacts** - Remove contacts with confirmation dialog
- 📱 **Responsive Design** - Works seamlessly on desktop, tablet, and mobile devices
- 🎨 **Modern UI** - Gradient backgrounds, smooth animations, and polished interface
- 💾 **Persistent Storage** - All contacts saved in SQLite database
- ⚡ **Fast & Lightweight** - Built with Flask for optimal performance

## 🎬 Demo

![Contact List](screenshot-list.png)
*Modern contact list with gradient design and hover effects*

![Contact Details](screenshot-view.png)
*Beautiful contact view with avatar and organized fields*

![Edit Form](screenshot-edit.png)
*Intuitive form with animated fields and helper text*

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/contact-book.git
   cd contact-book
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize the database**
   ```bash
   python app.py
   ```
   The database will be created automatically on first run.

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Open your browser**
   Navigate to `http://localhost:5000`

## 📦 Project Structure

```
contact-book/
│
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
│
├── templates/
│   ├── base.html         # Base template with modern styling
│   ├── index.html        # Contact list page
│   ├── view_contact.html # Contact details page
│   ├── edit_contact.html # Edit contact form
│   └── add_contact.html  # Add new contact form
│
├── static/               # Static files (if any)
│   ├── css/
│   └── js/
│
└── instance/
    └── contacts.db       # SQLite database (created automatically)
```

## 🛠️ Technologies Used

- **Backend**: Flask 3.0+
- **Database**: SQLite with Flask-SQLAlchemy
- **Frontend**: HTML5, CSS3, Jinja2 Templates
- **Design**: Modern gradient UI with animations
- **Icons**: Unicode emoji icons

## 📋 Requirements

```txt
Flask==3.0.0
Flask-SQLAlchemy==3.1.1
```

## 🎨 Features Breakdown

### Home Page (Contact List)
- Beautiful gradient header
- Card-based table design
- Hover effects on rows
- Color-coded action buttons
- Empty state with helpful message
- Animated page load

### View Contact
- Avatar with first letter of name
- Organized field layout with icons
- Clickable email and phone links
- Timestamp of when contact was added
- Smooth animations for each field
- Action buttons for edit/delete

### Edit/Add Contact
- Modern form design with gradient card
- Icon-based labels
- Focus effects with color changes
- Helper text for guidance
- Required field indicators
- Placeholder text in inputs
- Smooth submit/cancel buttons

### Base Template
- Animated background pattern
- Flash message system with icons
- Responsive container
- Custom gradient scrollbar
- Modern gradient buttons
- Fade-in page animations

## 🔧 Configuration

Edit the `app.py` file to configure:

```python
# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contacts.db'

# Secret key for sessions
app.config['SECRET_KEY'] = 'your-secret-key-here'

# Debug mode
app.run(debug=True)
```

## 📱 Responsive Design

The application is fully responsive and works on:
- 📱 Mobile phones (320px and up)
- 📱 Tablets (768px and up)
- 💻 Laptops (1024px and up)
- 🖥️ Desktops (1200px and up)

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Your Name**
- GitHub: [@yourusername](https://github.com/yourusername)
- Email: your.email@example.com

## 🙏 Acknowledgments

- Flask documentation and community
- Modern UI/UX design principles
- Open source community

## 📞 Support

If you have any questions or run into issues, please:
- Open an issue on GitHub
- Contact me via email
- Check the documentation

## 🗺️ Roadmap

Future features planned:
- [ ] Search and filter contacts
- [ ] Import/Export contacts (CSV, vCard)
- [ ] Contact groups/categories
- [ ] Profile pictures upload
- [ ] Dark mode toggle
- [ ] Contact notes/comments
- [ ] Birthday reminders
- [ ] Social media links

---

⭐ If you found this project helpful, please give it a star!

Made with ❤️ and Flask 