from math import modf
from flask import Flask
from webargs import fields
from webargs.flaskparser import use_kwargs

from hw_4.db_connection import execute_query
from hw_4.utils import format_records, format_tracks

app = Flask(__name__)


@app.route('/order_price')
@use_kwargs(
    {
        "country": fields.Str(required=False,
                              missing=''),
    },
    location="query"
)
def order_price(country):
    """
    This function is used to get the price of the product in the given country.
    :param country:
    :return: the price of the product in the given country.
    """
    if country:
        get_sum_of_sales_by_country = f"""
        SELECT (UnitPrice * sum(Quantity)) AS TotalSales
        FROM invoice_items
        INNER JOIN invoices ON invoice_items.InvoiceId = invoices.InvoiceId
        WHERE invoices.BillingCountry = '{country}'
        GROUP BY invoices.BillingCountry"""

        price_by_country = execute_query(get_sum_of_sales_by_country)
        return format_records(price_by_country, [country])

    else:
        query_for_new_price = """
        SELECT (UnitPrice * sum(Quantity)) AS TotalSales, invoices.BillingCountry AS Country
        FROM invoice_items
        INNER JOIN invoices ON invoice_items.InvoiceId = invoices.InvoiceId
        GROUP BY invoices.BillingCountry
        """
        new_price = execute_query(query_for_new_price)
        country = [country[1] for country in new_price]
        print(country)
        return format_records(new_price, country)


@app.route('/get_all_info_about_track')
@use_kwargs(
    {
        'track': fields.Int(required=False, missing=1),
    },
    location="query"
)
def get_all_info_about_track(track):
    """
    This function is used to get all info about the track.
    :param track:
    :return: all info about the track.
    """
    query = f"""
    SELECT tracks.Name, COMPOSER, 
    albums.Title AS AlbumTitle, 
    artists.Name AS Artist, 
    genres.Name AS Genre, 
    Milliseconds, 
    media_types.Name AS MediaType, 
    UnitPrice
    FROM tracks
    INNER JOIN albums
    ON tracks.AlbumId = albums.AlbumId
    INNER JOIN genres
    ON tracks.GenreId = genres.GenreId
    INNER JOIN media_types
    ON tracks.MediaTypeId = media_types.MediaTypeId
    INNER JOIN artists
    ON albums.ArtistId = artists.ArtistId
    WHERE TrackId = '{track}'"""

    track_info = execute_query(query)
    return format_tracks(track_info)


@app.route("/total_tracks_time")
def get_total_track_time():
    """
    This function is used to get the total time of all tracks.
    :return: the total time of all tracks.
    """
    query = 'SELECT sum(Milliseconds) FROM tracks;'
    time_of_tracks = execute_query(query)
    hours = round(int(time_of_tracks[0][0]) / 3600000)
    minutes = round(modf(hours)[0] * 60)

    return f"<h1>Total tracks time: {hours} hours {minutes} minutes</h1>"


if __name__ == '__main__':
    app.run(debug=True)
