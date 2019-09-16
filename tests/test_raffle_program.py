import raffle_program

TEST_DONATION_TICKET_DEF = {
        3: 1,
        6: 5,
        }

def test_assert_create_ticket_lookup_dict_returns_expected_data():
    expected_out = {0: 0, 1: 0, 2: 0, 3: 1, 4: 1, 5: 1}

    output = raffle_program.create_ticket_lookup_dict(TEST_DONATION_TICKET_DEF)
    assert output == expected_out


