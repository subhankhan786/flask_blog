from datetime import datetime
from time import time
import re

from app import db

def slugify(s):
    pattern = r'[^\w+]'
    return re.sub(pattern, '-', s)    

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    slug = db.Column(db.String(50), unique=True)
    content = db.Column(db.String(200))
    author = db.Column(db.String(25))
    date = db.Column(db.DateTime, default=datetime.now())
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.generate_slug()
        
    def generate_slug(self):
        if self.title:
            self.slug = slugify(self.title)
        else:
            self.slug = str(int(time()))
        
    def __repr__(self) -> str:
        return f"<Post id: {self.id}, title: {self.title}, author: {self.author}, content: {self.content}>"