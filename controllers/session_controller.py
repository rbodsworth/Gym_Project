from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.session import Session
import repositories.session_repository as session_repository

sessions_blueprint = Blueprint("sessions", __name__)

@sessions_blueprint.route("/sessions")
def sessions():
    sessions = session_repository.select_all()
    return render_template("sessions/index.html", sessions = sessions)

@sessions_blueprint.route("/sessions/<id>")
def show(id):
    session = session_repository.select(id)
    members = session_repository.members(session)
    return render_template("sessions/show.html", session=session, members=members)

    
@sessions_blueprint.route("/sessions/new")
def new_session():
    return render_template("sessions/new.html")

@sessions_blueprint.route("/sessions", methods=["POST"])
def create_session():
    name = request.form["name"]
    category = request.form["category"]
    new_session = Session(name, category)
    session_repository.save(new_session)
    return redirect("/sessions")

@sessions_blueprint.route("/sessions/<id>/delete", methods=["POST"])
def delete_session(id):
    session_repository.delete(id)
    return redirect("/sessions")