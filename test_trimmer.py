import secondary_functions as sf
import unittest
class Test_trimmer(unittest.TestCase):
    def test_read_phread_encoding(self):
        result = sf._phread_encoding()
        self.assertEqual(len(result),41)
    def test_check_gc_content(self):
        test_list = [['dasdadsa'],["AAATTTA"],["+"],["#######"]]
        result = sf._check_gc_content(test_list,100,100)
        self.assertFalse(result)
    def test_check_length(self):
        test_list = [['dasdadsa'], ["AAATTTA"], ["+"], ["#######"]]
        result = sf._check_length(test_list,100)
        self.assertFalse(result)
    def test_recode_quality(self):
        result = sf._recode_quality(['#'])
        self.assertEqual(result,[2])



if __name__ == '__main__':
    unittest.main()