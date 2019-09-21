doctest library - The built-in Python library for running doctests.

#Running doctests

#From the command line
#python -m doctest your_script.py

#From inside a script
#import doctest
#doctest.testmod()


unittest - Python's library for writing tests

#TestCase - A collection of tests

#Running tests

#Command line
python -m unittest tests.py

#In a script
unittest.main()

#Remember, all tests in a TestCase have to start with the word test_ to be run. You can have methods that don't start with test_ for other purposes if you need them.

setUp() - #Method that is run before each test. Use this to set up state for the tests

assertEqual(x, y) - #Make sure x and y are equal

assertNotEqual(x, y) - #Make sure x and y are not equal

assertGreater(x, y) - #Make sure x is greater than y

assertLess(x, y) - #Make sure x is less than y

assertIn(x, y) - #Make sure x is a member of y (this is like the in keyword)

assertIsInstance(x, y) - #Make sure x is an instance of the y class

assertGreaterEqual(x, y) - #Make sure x is greater than or equal to y

assertLessEqual(x, y) - #Make sure x is less than or equal to y

assertRaises(x) - #Make sure the following code raises the x exception

#You can use @unittest.expectedFailure on tests that you know will fail

#Installing coverage.py
pip install coverage

#Using coverage.py
Make sure you test file can be run from the command line without the -m unittest argument.
coverage run tests.py

#Generate a report
coverage report or coverage report -m if you want the missed lines.

