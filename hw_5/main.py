from flask import Flask
from webargs import fields
from webargs.flaskparser import use_kwargs

from hw_5.db_connection import execute_query
from hw_5.utils import format_records

app = Flask(__name__)


@app.route('/stats_by_city')
@use_kwargs(
    {
        'genre': fields.Str(required=True)
    },
    location='query'
)
def stats_by_city(genre):
    """
    Return the city where most listen to this genre of music
    return: str with information about the city
    """
    query_for_genre = "SELECT NAME FROM genres"
    query_for_city = """
    SELECT BillingCity FROM invoices
    INNER JOIN invoice_items ON invoices.InvoiceID = invoice_items.InvoiceID
    INNER JOIN tracks ON invoice_items.TrackID = tracks.TrackID
    INNER JOIN genres ON tracks.GenreID = genres.GenreID
    """
    _fields = {}

    if genre:
        _fields['genres.Name'] = genre

    if _fields:
        query_for_city += "WHERE " + " AND ".join(f"{k} = ?" for k in _fields) + \
                          " GROUP BY BillingCity" + \
                          " ORDER BY count(BillingCity) DESC"

    genres = execute_query(query_for_genre)
    genre_overreach = [genre[0] for genre in genres]

    if genre not in genre_overreach:
        return 'Please provide a valid genre, here the list of available genres: <br>' + '<br>'.join(
            genre_overreach
        )

    records = execute_query(query_for_city, args=tuple(_fields.values()))
    return format_records(records)


if __name__ == '__main__':
    app.run(debug=True)
