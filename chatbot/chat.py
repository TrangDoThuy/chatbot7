from datetime import datetime

from flask import render_template, url_for, redirect, Blueprint, abort, request

from flask_login import login_required, current_user

from chatbot.models import db, Chat

bp = Blueprint('chat', __name__)

@bp.route('/health')
def heath():
    return "Healthy"

@bp.route('/')
@login_required
def index():
   
    chats = []
    for chat in current_user.chats:
        chats.append(chat)
    
    return render_template('chat/index.html', chats=chats)

@bp.route('/chat', methods=('POST',))
@login_required
def create_chat():
    text = request.form['text']
    
    if not text:
        flash('Chat cannot be empty')
        return redirect(url_for('.index'))
    
    chat = Chat(content=text, user=current_user, message_from_bot=False)
    db.session.add(chat)
    db.session.commit()

    chat_ans = Chat(content="Good question, I don't know", user=current_user, message_from_bot=True)
    db.session.add(chat_ans)
    db.session.commit()
    
    return redirect(url_for('.index'))