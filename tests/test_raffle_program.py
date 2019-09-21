import raffle_program
import pytest
from unittest.mock import patch
from unittest.mock import mock_open

TEST_DONATION_TICKET_DEF = {
        3: 1,
        6: 5,
        }


def test_create_ticket_lookup_dict_returns_expected_data():
    expected_out = {0: 0, 1: 0, 2: 0, 3: 1, 4: 1, 5: 1}

    output = raffle_program.create_ticket_lookup_dict(TEST_DONATION_TICKET_DEF)
    assert output == expected_out


def test_create_ticket_lookup_dict_invalid_key_type():
    with pytest.raises(TypeError) as e:
        raffle_program.create_ticket_lookup_dict({"1": 2})

    assert str(e.value) == "All the keys in the donation dict must be integers"


def test_create_ticket_lookup_dict_invalid_value_type():
    with pytest.raises(TypeError) as e:
        raffle_program.create_ticket_lookup_dict({1: "2"})

    assert str(e.value) == "All the values in the donation dict must be integers"


def test_create_ticket_lookup_dict_pass_in_list():
    with pytest.raises(TypeError) as e:
        raffle_program.create_ticket_lookup_dict([1, 2, 3])

    assert str(e.value) == "Must pass a dictionary to this function"


def test_create_ticket_lookup_dict_pass_in_string():
    with pytest.raises(TypeError) as e:
        raffle_program.create_ticket_lookup_dict("1,2,3")

    assert str(e.value) == "Must pass a dictionary to this function"


def test_create_ticket_lookup_dict_pass_in_empty_dict():
    output = raffle_program.create_ticket_lookup_dict({})
    assert output == {}


def test_create_raffle_list_returns_expected_data():
    expected_out = [{'Email': 'valid@email.com', 'is_winner': False, 'tickets': 2},
                    {'Email': 'valid@email.com', 'is_winner': False, 'tickets': 2}]
    test_data = [
            {"Email": "valid@email.com", "tickets": 2},
            {"Email": "valid2@email.com", "tickets": 0},
            {"Email": "non_email_address"},
            {"Email": "bad.email_at_google.com"},
            {"Email": "bademail@google_dot_com"},
            ]

    output = raffle_program.create_raffle_list(test_data)
    assert output == expected_out


def test_create_raffle_list_pass_in_dict():
    with pytest.raises(TypeError) as e:
        raffle_program.create_raffle_list({})

    assert str(e.value) == "Must pass a list to this function"


def test_create_raffle_list_pass_in_string():
    with pytest.raises(TypeError) as e:
        raffle_program.create_raffle_list("bad_input")

    assert str(e.value) == "Must pass a list to this function"


def test_create_raffle_list_pass_in_list_of_ints():
    with pytest.raises(ValueError) as e:
        raffle_program.create_raffle_list([1, 2, 3])

    assert str(e.value) == "All items in the data structure must be dictionaries"


def test_pick_raffle_winners_pass_in_string():
    with pytest.raises(TypeError) as e:
        raffle_program.pick_raffle_winners("bad_input", 1)

    assert str(e.value) == "`raffle_list` must be a list"


def test_pick_raffle_winners_pass_in_dict():
    with pytest.raises(TypeError) as e:
        raffle_program.pick_raffle_winners({"key1": "value1", "key2": "value2"}, 1)

    assert str(e.value) == "`raffle_list` must be a list"


def test_pick_raffle_winners_pass_in_string_winners():
    with pytest.raises(TypeError) as e:
        raffle_program.pick_raffle_winners(["empty", "list"], "1")

    assert str(e.value) == "`qty_winners` must be an integer"


def test_pick_raffle_winners_pass_assert_expected_output():
    test_list = [
            {"name": "John Doe", "is_winner": False},
            {"name": "Jane Doe", "is_winner": False},
            {"name": "Doe Ray Mi", "is_winner": False},
            {"name": "Jimme Dough", "is_winner": False}
            ]

    winners = 2

    winner_list = raffle_program.pick_raffle_winners(test_list, winners)

    assert len(winner_list) == len(test_list)

    # Check the output and verify that the number of winners in the file
    # match the number of winners passed into the function
    qty_winners = [True for x in winner_list if x["is_winner"]]

    assert len(qty_winners) == winners


def test_pick_raffle_winners_too_many_winners():
    test_list = [
            {"name": "John Doe", "is_winner": False},
            {"name": "Jane Doe", "is_winner": False},
            {"name": "Doe Ray Mi", "is_winner": False},
            {"name": "Jimme Dough", "is_winner": False}
            ]

    winners = 6

    with pytest.raises(ValueError) as e:
        raffle_program.pick_raffle_winners(test_list, winners)

    assert str(e.value) == "You selected more winners than tickets"


def test_calculate_raffle_entries_invalid_csv_data():
    with pytest.raises(TypeError) as e:
        raffle_program.calculate_raffle_entries("not a list", {})

    assert str(e.value) == "`csv_data` must be a list"


def test_calculate_raffle_entries_invalid_donation_dict():
    with pytest.raises(TypeError) as e:
        raffle_program.calculate_raffle_entries([], "not a dict")

    assert str(e.value) == "`donation_dict` must be a dictionary"


def test_calculate_raffle_entries_verify_output():
    test_list = [
            {"name": "John Doe", "Amount": 0},
            {"name": "Jane Doe", "Amount": 9},
            {"name": "Doe Ray Mi", "Amount": 15},
            {"name": "Jake Doe", "Amount": 199},
            {"name": "Jimme Dough", "Amount": 1000}
            ]

    test_conversion_dict = {
        10: 1,
        25: 5,
        50: 10,
        75: 18,
        100: 30,
        125: 45,
        150: 65,
        200: 100
        }

    results = raffle_program.calculate_raffle_entries(test_list, test_conversion_dict)

    assert len(results) == 5
    assert results[0]["tickets"] == 0
    assert results[1]["tickets"] == 0
    assert results[2]["tickets"] == 1
    assert results[3]["tickets"] == 65
    assert results[4]["tickets"] == 100


def test_merge_donations_invalid_csv_data():
    with pytest.raises(TypeError) as e:
        raffle_program.merge_donations("bad_input", "id", "contrib", "date")

    assert str(e.value) == "`csv_data` must be a list"


def test_merge_donations_invalid_id_header():
    with pytest.raises(TypeError) as e:
        raffle_program.merge_donations(["non", "empty", "list"], 10, "contrib", "date")

    assert str(e.value) == "All headers must be strings"


def test_merge_donations_invalid_contribution_header():
    with pytest.raises(TypeError) as e:
        raffle_program.merge_donations(["non", "empty", "list"], "id", 10, "date")

    assert str(e.value) == "All headers must be strings"


def test_merge_donations_invalid_date_header():
    with pytest.raises(TypeError) as e:
        raffle_program.merge_donations(["non", "empty", "list"], "id", "contrib", 10)

    assert str(e.value) == "All headers must be strings"


def test_merge_donations_invalid_money_data():
    test_list = [
            {"name": "John Doe", "money": "0.99", "id": "john_doe@fake.com", "date": "01/02/03", "file_name": "a"},
            {"name": "Jane Doe", "money": "9.O1", "id": "jdoe@fake.com", "date": "04/05/06", "file_name": "b"},
            {"name": "Doe Ray Mi", "money": "15.000", "id": "di_mi@fake.com", "date": "04/02/04", "file_name": "c"},
            {"name": "Jake Doe", "money": "199.99", "id": "jdoe@fake.com", "date": "01/02/03", "file_name": "d"},
            {"name": "Jimme Dough", "money": "1000.O0", "id": "ji_doe@fake.com", "date": "01/02/03", "file_name": "e"}
            ]

    results = raffle_program.merge_donations(test_list, "id", "money", "date")

    assert results[2]["money"] == 199
    assert "ji_doe@fake.com" not in [x["id"] for x in results]


def test_merge_donations_valid_data():
    test_list = [
            {"name": "John Doe", "money": "0.99", "id": "john_doe@fake.com", "date": "01/02/03", "file_name": "a"},
            {"name": "Jane Doe", "money": "9.01", "id": "jdoe@fake.com", "date": "04/05/06", "file_name": "b"},
            {"name": "Doe Ray Mi", "money": "15.000", "id": "di_mi@fake.com", "date": "04/02/04", "file_name": "c"},
            {"name": "Jake Doe", "money": "199.99", "id": "jdoe@fake.com", "date": "01/02/03", "file_name": "d"},
            {"name": "Jimme Dough", "money": "1000.00", "id": "ji_doe@fake.com", "date": "01/02/03", "file_name": "e"}
            ]

    results = raffle_program.merge_donations(test_list, "id", "money", "date")

    assert len(results) == 4
    assert results[1]["money"] == 208
    assert results[3]["money"] == 1000
    assert "04/05/06" in results[1]["date"]
    assert "01/02/03" in results[1]["date"]
    assert "b" in results[1]["file_name"]
    assert "d" in results[1]["file_name"]


def test_write_out_to_csv_with_custom_file_prefix():
    test_list = [
            {"name": "John Doe", "Amount": 0},
            {"name": "Jane Doe", "Amount": 9},
            {"name": "Doe Ray Mi", "Amount": 15},
            {"name": "Jake Doe", "Amount": 199},
            {"name": "Jimme Dough", "Amount": 1000}
            ]
    m = mock_open()
    with patch("builtins.open", m, create=True):
        raffle_program.write_out_csv_file(test_list, "test_prefix")

    m.assert_called_once()
    calls = str(m.mock_calls)

    assert calls.count("write") == 6
    assert "test_prefix" in calls
    assert m.call_count == 1


@patch("builtins.open", new_callable=mock_open, create=True)
def test_write_out_to_csv_with_default_file_prefix(mock_file):
    test_list = [
            {"name": "John Doe", "Amount": 0},
            {"name": "Jane Doe", "Amount": 9},
            {"name": "Doe Ray Mi", "Amount": 15},
            {"name": "Jake Doe", "Amount": 199},
            {"name": "Jimme Dough", "Amount": 1000}
            ]

    raffle_program.write_out_csv_file(test_list)

    mock_file.assert_called_once()
    calls = str(mock_file.mock_calls)

    assert calls.count("write") == 6
    assert "default_output" in calls
    assert mock_file.call_count == 1


@patch("builtins.open", new_callable=mock_open, read_data='1,2,3')
def test_read_in_invalid_csv_files(mock_file):
    with pytest.raises(ValueError) as e:
        raffle_program.read_in_csv_files(['file1', 'file2', 'file3'])

    assert str(e.value) == "The CSV files were blank, there must be at least one entry"


@patch("builtins.open", new_callable=mock_open, read_data='Amount\n10\n20')
def test_read_in_valid_csv_files(mock_file):
    expected_out = [
            {'Amount': '10', 'file_name': 'file1'},
            {'Amount': '20', 'file_name': 'file1'},
            {'Amount': '10', 'file_name': 'file2'},
            {'Amount': '20', 'file_name': 'file2'}
            ]

    out = raffle_program.read_in_csv_files(['file1', 'file2'])

    assert expected_out == out
