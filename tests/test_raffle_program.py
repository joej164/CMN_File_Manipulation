import raffle_program
import pytest

TEST_DONATION_TICKET_DEF = {
        3: 1,
        6: 5,
        }


def test_create_ticket_lookup_dict_returns_expected_data():
    expected_out = {0: 0, 1: 0, 2: 0, 3: 1, 4: 1, 5: 1}

    output = raffle_program.create_ticket_lookup_dict(TEST_DONATION_TICKET_DEF)
    assert output == expected_out


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
