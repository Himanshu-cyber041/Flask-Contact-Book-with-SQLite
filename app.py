from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contacts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Contact Model
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Contact {self.name}>'

# Create database tables
with app.app_context():
    db.create_all()

# Routes
@app.route('/')
def index():
    contacts = Contact.query.order_by(Contact.name).all()
    return render_template('index.html', contacts=contacts)

@app.route('/add', methods=['GET', 'POST'])
def add_contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        address = request.form.get('address')
        
        # Validation
        if not name or not email or not phone:
            flash('Name, Email, and Phone are required!', 'error')
            return redirect(url_for('add_contact'))
        
        # Create new contact
        new_contact = Contact(
            name=name,
            email=email,
            phone=phone,
            address=address
        )
        
        try:
            db.session.add(new_contact)
            db.session.commit()
            flash('Contact added successfully!', 'success')
            return redirect(url_for('index'))
        except:
            flash('Error adding contact. Please try again.', 'error')
            return redirect(url_for('add_contact'))
    
    return render_template('add.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_contact(id):
    contact = Contact.query.get_or_404(id)
    
    if request.method == 'POST':
        contact.name = request.form.get('name')
        contact.email = request.form.get('email')
        contact.phone = request.form.get('phone')
        contact.address = request.form.get('address')
        
        # Validation
        if not contact.name or not contact.email or not contact.phone:
            flash('Name, Email, and Phone are required!', 'error')
            return redirect(url_for('edit_contact', id=id))
        
        try:
            db.session.commit()
            flash('Contact updated successfully!', 'success')
            return redirect(url_for('index'))
        except:
            flash('Error updating contact. Please try again.', 'error')
            return redirect(url_for('edit_contact', id=id))
    
    return render_template('edit.html', contact=contact)

@app.route('/delete/<int:id>')
def delete_contact(id):
    contact = Contact.query.get_or_404(id)
    
    try:
        db.session.delete(contact)
        db.session.commit()
        flash('Contact deleted successfully!', 'success')
    except:
        flash('Error deleting contact. Please try again.', 'error')
    
    return redirect(url_for('index'))

@app.route('/view/<int:id>')
def view_contact(id):
    contact = Contact.query.get_or_404(id)
    return render_template('view.html', contact=contact)

if __name__ == '__main__':
    app.run(debug=True) 
    