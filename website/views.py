from flask import Blueprint, render_template, request, flash, redirect, jsonify, url_for
from flask_login import login_required, current_user, LoginManager
from .models import Note
from website import db
import json
import pyttsx3


views = Blueprint('views', __name__)

@views.route('/', methods=["POST", "GET"])
@login_required
def home():
    if request.method == "GET":
      return render_template("home.html", user = current_user)
    if request.method == "POST":
      note = request.form.get("note")
      if len(note) < 1:
         flash("Note is too short!", category="error")
      else:
         new_data = Note(data = note, user_id = current_user.id)
         db.session.add(new_data)
         db.session.commit()
         flash("Note added.", category="success")
         return redirect('/')

@views.route('/delete-note', methods = ["POST"])
def delete_note():
   note = json.loads(request.data)
   noteId = note['noteId']
   note = Note.query.get(noteId)
   if note:
      if note.user_id == current_user.id:
         db.session.delete(note)
         db.session.commit()
         return jsonify({})