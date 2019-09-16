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
    with pytest.raises(TypeError):
        raffle_program.create_ticket_lookup_dict([1, 2, 3])


def test_create_ticket_lookup_dict_pass_in_string():
    with pytest.raises(TypeError):
        raffle_program.create_ticket_lookup_dict("1,2,3")


def test_create_ticket_lookup_dict_pass_in_empty_dict():
    output = raffle_program.create_ticket_lookup_dict({})
    assert output == {}
