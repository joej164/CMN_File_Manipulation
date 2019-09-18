This doc covers useful info and commands for testing this project.

Test were run using `pytest` and coverage was done using `pytest-cov`.

To run tests just type `pytest` from the root of the project.

NOTE: In Windows I had to run it in a command prompt that was running as Administrator

To get the coverage report with any code that is uncovered, run as follows:
`pytest --cov=raffle_program --cov-report=term-missing`


