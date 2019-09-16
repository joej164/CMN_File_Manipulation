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
