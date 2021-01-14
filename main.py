import unittest

class Test_Math(unittest.TestCase):

    def setupclass(self):
        print("start")

    def teardownclass(self):
        print("finish")


    def test_addTwoNum_01(self):
        self.assertEqual(1, 3-2)

    def test_subTwoNum_02(self):
        self.assertEqual(5, 3-1)


unittest.main()

