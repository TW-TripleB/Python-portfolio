import unittest

class TestStringMethods(unittest.TestCase):

    # def setUp(self):
    #     # 單測啟動前的準備工作，比如初始化一個mysql連線物件
    #     # 為了說明函式功能，測試的時候沒有CMysql模組註釋掉或者換做print學習
    #     self.conn = CMysql()

    # def tearDown(self):
    #     # 單測結束的收尾工作，比如資料庫斷開連接回收資源
    #     self.conn.disconnect()

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()