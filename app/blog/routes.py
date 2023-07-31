from flask import render_template, request, g, flash, abort, redirect, url_for
from app.blog import bp
from app.extensions import db
from app.models import Category, Post, User
from app.auth import login_required
from app.helpers import row_to_dict

from datetime import datetime

@bp.route('/home')
def home():
    return render_template('blog/home.html')

@bp.route('/categories/<int:category_id>')
def show_category(category_id):
    category = Category.query.get_or_404(category_id)
    posts = Post.query.filter_by(category_id=category_id)
    return render_template('blog/category.html', category=category, posts=posts)

@bp.route('/new_post', methods=['GET', 'POST'])
@login_required
def new_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        category = int(request.form['category'])

        post = Post(
            title = title,
            content = content,
            author_id = g.user.id,
            category_id = category
        )

        db.session.add(post)
        db.session.commit()

        flash('The post was created successfully.')

        return redirect(url_for('blog.show_user_posts', username=g.user.username))

    return render_template('blog/new_post.html')

@bp.route('/users/<string:username>')
def show_user_posts(username):
    user = User.query.filter_by(username=username).first()
    if not user:
        abort(404)

    user_posts = Post.query.filter_by(author_id=user.id)
    user_posts_dicts = []
    for user_post in user_posts:
        user_post = row_to_dict(user_post)
        category = Category.query.get_or_404(user_post['category_id'])
        user_post['category'] = category.name
        user_posts_dicts.append(user_post)

    return render_template('blog/user_posts.html', user_posts=user_posts_dicts)

@bp.route('/post/<int:post_id>')
def show_post(post_id):
    post = Post.query.get_or_404(post_id)
    author = User.query.get_or_404(post.author_id)
    return render_template('blog/post.html', post=post, author=author)

@bp.route('/edit_post/<int:post_id>', methods=['GET', 'POST'])
@login_required
def edit_post(post_id):
    post = Post.query.get_or_404(post_id)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        category = int(request.form['category'])

        post.title = title
        post.content = content
        post.category_id = category
        post.updated_at = datetime.utcnow()

        db.session.commit()

        flash('The post has been successfully updated.')

    return render_template('blog/edit_post.html', post=post)

@bp.route('/delete_post/<int:post_id>')
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)

    db.session.delete(post)
    db.session.commit()

    flash('The post has been successfully deleted.')

    return redirect(url_for('blog.show_user_posts', username=g.user.username))
