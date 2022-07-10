styles = """
<style>
    table {
        width: 100%;
    }
    table, tr, th, td {
        text-align: center;
        border: 1px solid black;
        border-collapse: collapse;
    }
</style>
"""


def format_records(price: list, country) -> str:
    """
    This function is used to format the price of the product in the given country.
    :param price:
    :param country:
    :return: the price of the product in the given country.
    """
    string_to_return = ""
    for i in range(len(price)):
        string_to_return += f"""
            <tr>
                <td>{price[i][0]}</td>
                <td>{country}</td>
            </tr>
        """
    return f"""
    {styles}
    <table>
          <tr>
            <th>NewPrice</th>
            <th>Country</th>
          </tr>
            {string_to_return}
    </table>
        """


def format_tracks(track_info) -> str:
    """
    This function is used to format the track info.
    :param track_info:
    :return: the track info.
    """

    string_to_return = f"""
            <tr>
                {''.join([f'<td>{info}</td>' for info in track_info[0]])}
            </tr>
        """
    return f"""
    {styles}
    <table>
          <tr>
            <th>Name</th>
            <th>Composer</th>
            <th>Title</th>
            <th>Artist</th>
            <th>Genre</th>
            <th>Milliseconds</th>
            <th>MediaType</th>
            <th>UnitPrice</th>
          </tr>
            {string_to_return}
    </table>
        """
