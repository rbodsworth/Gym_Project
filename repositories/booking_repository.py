from db.run_sql import run_sql

from models.booking import Booking
from models.session import Session
from models.member import Member
import repositories.member_repository as member_repository
import repositories.session_repository as session_repository

def save(booking):
    sql = "INSERT INTO bookings ( member_id, session_id ) VALUES ( %s, %s) RETURNING id"
    values = [booking.member.id, booking.session.id]
    results = run_sql(sql, values)
    booking.id = results[0]['id']
    return booking


def select_all():
    bookings = []

    sql = "SELECT * FROM bookings"
    results = run_sql(sql)

    for row in results:
        member = member_repository.select(row['member_id'])
        session = session_repository.select(row['session_id'])
        booking = Booking(member, session, row['id'])
        bookings.append(booking)
    return bookings


def session(booking):
    sql = "SELECT * FROM sessions WHERE id = %s"
    values = [booking.session.id]
    results = run_sql(sql, values)[0]
    session = Session(results['name'], results['category'], results['id'])
    return session


def member(booking):
    sql = "SELECT * FROM members WHERE id = %s"
    values = [booking.member.id]
    results = run_sql(sql, values)[0]
    member = Member(results['name'], results['id'])
    return member


def delete_all():
    sql = "DELETE FROM bookings"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM bookings WHERE id = %s"
    values = [id]
    run_sql(sql, values)
