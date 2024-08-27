from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class URLMapping(db.Model):
    __tablename__ = 'url_mappings'

    id = db.Column(db.Integer, primary_key=True)
    long_url = db.Column(db.String(2048), nullable=False)
    short_url = db.Column(db.String(10), unique=True, nullable=False)

    def __repr__(self):
        return f"<URLMapping(long_url='{self.long_url}', short_url='{self.short_url}')>"

def save_url_mapping(long_url, short_url):
    from app import db
    existing = URLMapping.query.filter_by(long_url=long_url).first()
    if existing:
        return existing.short_url

    url_mapping = URLMapping(long_url=long_url, short_url=short_url)
    db.session.add(url_mapping)
    db.session.commit()
    return short_url

def get_long_url(short_url):
    mapping = URLMapping.query.filter_by(short_url=short_url).first()
    if mapping:
        return mapping.long_url
    return None
