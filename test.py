from unittest import TestCase
from MemList import MemoryList
import os


class TestMemList(TestCase):
    def setUp(self) -> None:
        with open("test_file.dat", "w") as f:
            f.write("abcde\n")
        self.mem_list = MemoryList("test_file")
        self.mem_list2 = MemoryList("test_file2")

    def test_init(self):
        self.assertIn("abcde", self.mem_list)

    def test_add(self):
        self.mem_list.append("1")
        test = MemoryList("test_file")
        self.assertIn("1", test)

    def tearDown(self) -> None:
        os.remove(os.path.join(os.path.abspath(os.path.dirname(__file__)), "test_file.dat"))
        os.remove(os.path.join(os.path.abspath(os.path.dirname(__file__)), "test_file2.dat"))