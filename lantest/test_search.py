# 被测的方法
import unittest


class Search:
    def search_fun(self) :
        print("search")
        return True


class Testsearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("setUpClass")
        cls.search =Search()



    def test_search1(self):
        print("test_search1")
        #search = Search()
        assert True == self.search.search_fun()
    def test_search2(self):
        print("test_search2")
        #search = Search()
        assert True == self.search.search_fun()
    def test_search3(self):
        print("test_search3")
        #search = Search()
        assert True == self.search.search_fun()
    def test_search4(self):
        print("test_search4")
        #earch = Search()
        assert True == self.search.search_fun()


    def test_equal(self):
        print("断言相等")
        self.assertEqual(1,1,"判断1==1")
    def test_notequal(self):
        #print("断言不等")
        #self.assertNotEqual(1,2,"判断1!=2")
        #断言表达式是不是真
        self.assertTrue(3==3,"verify")

    @classmethod
    def tearDownClass(cls) -> None:
        print("tearDownClass")

if __name__ == '__main__':
    #方法一：执行所有测试用例
    # unittest.main()
    #方法二：执行指定的测试用例，将要执行的测试用例添加到测试套件里面，批量执行
    #创建一个测试套件
    # suite = unittest.TestSuite()
    # suite.addTest(Testsearch("test_search1"))
    # unittest.TextTestRunner().run(suite)

    #方法三：执行某个测试类
    suite1 = unittest.TestLoader().loadTestsFromTestCase(Testsearch)
    suite = unittest.TestSuite([suite1])
    unittest.TextTestRunner(verbosity=2).run(suite1)