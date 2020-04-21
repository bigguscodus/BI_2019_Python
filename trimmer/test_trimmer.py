from trimmer import sf
import unittest
class Test_trimmer(unittest.TestCase):
    def test_read_phread_encoding(self):
        result = sf._phread_encoding()
        self.assertEqual(len(result),41)
    def test_check_gc_content(self):
        test_list = [['test'],["AAATTTA"],["+"],["#######"]]
        result = sf._check_gc_content(test_list,100,100)
        self.assertFalse(result)
    def test_check_length(self):
        test_list = [['test'], ["AAATTTA"], ["+"], ["#######"]]
        result = sf._check_length(test_list,100)
        self.assertFalse(result)
    def test_recode_quality(self):
        result = sf._recode_quality(list('!#$%&+I'))
        self.assertEqual(result,[0,2,3,4,5,10,40])
    def test_crop(self):
        test_list = ['test', "AAATTTA", "+", "#######"]
        result = sf._crop(test_list,2)
        self.assertEqual(['test', "AA", "+", "##"], result)
    def test_headcrop(self):
        test_list = ['test', "AAATTTA", "+", "#######"]
        result = sf._headcrop(test_list, 2)
        self.assertEqual(['test', "ATTTA", "+", "#####"], result)
    def test_trailing(self):
        test_list = ['test', "AAATTTA", "+", "IIII###"]
        result = sf._trailing(test_list,20)
        self.assertEqual(['test', "AAAT", "+", "IIII"], result)
if __name__ == '__main__':
    unittest.main()
