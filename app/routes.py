from datetime import datetime

from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import ReviewForm
from app.db import get_db

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/FAQ')
def FAQ():
    return render_template('FAQ.html')

@app.route('/my_reviews')
def my_reviews():
    return 'MY REVIEWS'

@app.route('/new_review', methods=['GET', 'POST'])
def new_review():
    conn = get_db()
    cur = conn.cursor()
    cur.execute(
        "SELECT id, name, part FROM Courses WHERE discontinued = 0 ORDER BY part, name"
    )
    courses = cur.fetchall()
    conn.close()

    form = ReviewForm()
    form.part.choices = [('', 'All parts')] + [
        (part, f'Part {part}') for part in sorted({course['part'] for course in courses})
    ]
    form.course_id.choices = [(course['id'], course['name']) for course in courses]

    if form.validate_on_submit():
        selected_course = next(
            (course for course in courses if course['id'] == form.course_id.data),
            None,
        )
        if selected_course is None or (
            form.part.data and selected_course['part'] != form.part.data
        ):
            form.course_id.errors = list(form.course_id.errors) + [
                'Select a course from the chosen part.'
            ]
        else:
            conn = get_db()
            cur = conn.cursor()
            cur.execute(
                """
                INSERT INTO Reviews
                    (course_id, year, crsid, fun, difficulty, content,
                     lecturer_content, hidden, likes, timestamp)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """,
                (
                    form.course_id.data,
                    form.year.data,
                    'anonymous',
                    form.fun.data,
                    form.difficulty.data,
                    form.content.data,
                    form.lecturer_content.data or '',
                    0,
                    0,
                    datetime.now(),
                ),
            )
            conn.commit()
            conn.close()
            flash('Your review was submitted.')
            return redirect(url_for('reviews', id=form.course_id.data))

    return render_template('new_review.html', form=form, courses=courses)

@app.route('/IA')
def IA():
    conn = get_db()
    cur = conn.cursor()

    cur.execute("""
        SELECT c.*, COALESCE(stats.review_count, 0) AS review_count,
               stats.avg_fun, stats.avg_difficulty
        FROM Courses AS c
        LEFT JOIN (
            SELECT course_id, COUNT(id) AS review_count,
                   AVG(fun) AS avg_fun, AVG(difficulty) AS avg_difficulty
            FROM Reviews
            WHERE hidden = 0
            GROUP BY course_id
        ) AS stats ON stats.course_id = c.id
        WHERE c.part = %s AND c.discontinued = 0
    """, ("IA",))
    courses = cur.fetchall()
    conn.close()
    return render_template('IA.html', courses=courses)

@app.route('/IB')
def IB():
    conn = get_db()
    cur = conn.cursor()

    cur.execute("""
        SELECT c.*, COALESCE(stats.review_count, 0) AS review_count,
               stats.avg_fun, stats.avg_difficulty
        FROM Courses AS c
        LEFT JOIN (
            SELECT course_id, COUNT(id) AS review_count,
                   AVG(fun) AS avg_fun, AVG(difficulty) AS avg_difficulty
            FROM Reviews
            WHERE hidden = 0
            GROUP BY course_id
        ) AS stats ON stats.course_id = c.id
        WHERE c.part = %s AND c.discontinued = 0
    """, ("IB",))
    courses = cur.fetchall()
    conn.close()
    return render_template('IB.html', courses=courses)


@app.route('/II')
def II():
    conn = get_db()
    cur = conn.cursor()

    cur.execute("""
        SELECT c.*, COALESCE(stats.review_count, 0) AS review_count,
               stats.avg_fun, stats.avg_difficulty
        FROM Courses AS c
        LEFT JOIN (
            SELECT course_id, COUNT(id) AS review_count,
                   AVG(fun) AS avg_fun, AVG(difficulty) AS avg_difficulty
            FROM Reviews
            WHERE hidden = 0
            GROUP BY course_id
        ) AS stats ON stats.course_id = c.id
        WHERE c.part = %s AND c.discontinued = 0
    """, ("II",))
    courses = cur.fetchall()
    conn.close()
    return render_template('II.html', courses=courses)

@app.route('/III')
def III():
    conn = get_db()
    cur = conn.cursor()

    cur.execute("""
        SELECT c.*, COALESCE(stats.review_count, 0) AS review_count,
               stats.avg_fun, stats.avg_difficulty
        FROM Courses AS c
        LEFT JOIN (
            SELECT course_id, COUNT(id) AS review_count,
                   AVG(fun) AS avg_fun, AVG(difficulty) AS avg_difficulty
            FROM Reviews
            WHERE hidden = 0
            GROUP BY course_id
        ) AS stats ON stats.course_id = c.id
        WHERE c.part = %s AND c.discontinued = 0
    """, ("III",))
    courses = cur.fetchall()
    conn.close()
    return render_template('III.html', courses=courses)

@app.route('/reviews/<id>')
def reviews(id):
    print("ROUTE CALLED")
    conn = get_db()
    cur = conn.cursor()

    cur.execute("SELECT * FROM Courses WHERE id = %s",(id,))
    course = cur.fetchone()

    cur.execute("SELECT * FROM Reviews WHERE course_id = %s AND hidden = 0 ORDER BY likes, timestamp",(id,))
    reviews = cur.fetchall()

    conn.close()

    for review in reviews:
        review["academic_year"] = (
            f"{review['year']}-{(int(review['year']) + 1) % 100:02d}"
        )

    return render_template("reviews.html", course = course, reviews = reviews)