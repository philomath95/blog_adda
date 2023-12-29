from blog_app import db
import datetime 


class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    posts = db.relationship('Post', backref='category', lazy=True)
    
    def __repr__(self):
        return f'<Category {self.name}>'

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False, unique=True)
    desc = db.Column(db.Text, nullable=True)
    # Add an image column
    image_data = db.Column(db.LargeBinary)
    image_filename = db.Column(db.String(255))
    image_mimetype = db.Column(db.String(255))

    date_created = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    date_updated = db.Column(db.DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)

    def __repr__(self):
        return f'<Post {self.id}>'
    

# *********************** Authentication ****************************
    
class Register(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), unique=True, nullable=False)
    confirm_password = db.Column(db.String(100), unique=True, nullable=False)

class LogIn(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), unique=True, nullable=False)

