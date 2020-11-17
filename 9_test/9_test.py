def get_formatted_name(first,last):
    '''gnerate a neatly formatted full name'''
    full_name = first+" " +last
    return full_name.title();

import unittest
class NameTestCase(unittest.TestCase):
    '''测试 get_formatted_name'''

    def test_first_last_name(self):
        formatted_name = get_formatted_name("andy","yang")
        self.assertEqual(formatted_name,"andy yang");

unittest.main()