from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
from flask import session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import app, db
from models.picture import Picture


@app.route("/")
def open_site():
    """стартовая страница, возвращает все объекты в db"""
    pictures = Picture.query.all()
    pictures = [
        {
            "id": picture.id,
            "name": picture.name,
            "tag": picture.tag,
            "likes": picture.likes,
            "path": picture.path,
        } for picture in pictures]
    # return jsonify(pictures)
    return render_template('index.html', pictures=pictures)


@app.route('/picture/<int:picture_id>', methods=['GET'])
def get_all_picture(picture_id):
    """возвращает объект по id (здесь будет поп-ап)"""
    try:
        picture_by_id = Picture.query.filter_by(id=picture_id).first_or_404()
        return jsonify([picture_by_id.serialize])
    except Exception:
        return f'This page does not exist'


@app.route('/tag/<tagname>', methods=['GET'])
def get_by_tag(tagname):
    """возвращает все объекты по tagname"""
    try:
        pictures_by_tag = Picture.query.filter_by(tag=tagname).all()
        return jsonify([pictures_by_tag.serialize])
    except Exception:
        return f'This page does not exist'


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
