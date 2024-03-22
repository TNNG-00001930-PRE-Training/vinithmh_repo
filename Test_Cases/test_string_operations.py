import unittest
from string_operations import concatenate_strings, slice_string, format_string, upper_string, lower_string, strip_string, replace_string

class TestStringOperations(unittest.TestCase):
    def test_concatenate_strings(self):
        self.assertEqual(concatenate_strings("hello", "world"), "helloworld")
        self.assertEqual(concatenate_strings("abc", "123"), "abc123")
        self.assertEqual(concatenate_strings("", "test"), "test")
        self.assertEqual(concatenate_strings("empty", ""), "empty")

    def test_slice_string(self):
        self.assertEqual(slice_string("hello world", 0, 5), "hello")
        self.assertEqual(slice_string("python", 1, 4), "yth")
        self.assertEqual(slice_string("abcdef", 2, 5), "cde")
        self.assertEqual(slice_string("testing", 3, 7), "ting")

    def test_format_string(self):
        self.assertEqual(format_string("Alice", 30), "My name is Alice and I am 30 years old.")
        self.assertEqual(format_string("Bob", 25), "My name is Bob and I am 25 years old.")
        self.assertEqual(format_string("Charlie", 40), "My name is Charlie and I am 40 years old.")

    def test_upper_string(self):
        self.assertEqual(upper_string("hello"), "HELLO")
        self.assertEqual(upper_string("WORLD"), "WORLD")
        self.assertEqual(upper_string("HeLLo"), "HELLO")

    def test_lower_string(self):
        self.assertEqual(lower_string("HEllo"), "hello")
        self.assertEqual(lower_string("WORLD"), "world")
        self.assertEqual(lower_string("HeLLo"), "hello")

    def test_strip_string(self):
        self.assertEqual(strip_string("  hello  "), "hello")
        self.assertEqual(strip_string("\t\tworld\n"), "world")
        self.assertEqual(strip_string("  spaces  everywhere  "), "spaces  everywhere")
    
    def test_replace_string(self):
        self.assertEqual(replace_string("hello world", "world", "planet"), "hello planet")
        self.assertEqual(replace_string("hello hello hello", "hello", "hi"), "hi hi hi")
        self.assertEqual(replace_string("one two three", "two", "2"), "one 2 three")

if __name__ == '__main__':
    unittest.main()
