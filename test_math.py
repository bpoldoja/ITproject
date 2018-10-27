import unittest
import mathematics

class TestMathematics(unittest.TestCase):
    def test_add(self):
        self.assertEqual(mathematics.add(10,5), 15)
        self.assertEqual(mathematics.add(-1,1), 0)
        self.assertEqual(mathematics.add(3.31,5), 8.31)
        
    def test_multiply(self):
        self.assertEqual(mathematics.multiply(10,5), 50)
        self.assertEqual(mathematics.multiply(-1,1), -1)
        self.assertEqual(mathematics.multiply(3.5,5), 17.5)
        self.assertEqual(mathematics.multiply(0,0), 0)
        self.assertEqual(mathematics.multiply(0,1), 0)
        self.assertEqual(mathematics.multiply(1,0), 0)
        
    def test_hashing(self):
        self.assertEqual(mathematics.hashing('Lore'), '730949e23ca46f310466fbf205ffb165aef1fd7b')
        self.assertEqual(mathematics.hashing('Lorem'), 'db6ff2ffe2df7b8cfc0d9542bdce27dc')
        self.assertEqual(mathematics.hashing('Lorem ipsum dolor sit ame'), '92c40e81b7724f813e95dfab7ee61108474eed86ab785bd62bb6f873ffa11d98')
        self.assertEqual(mathematics.hashing('Lorem ipsum dolor sit amet, ex ius ass'), 'd668f938bf678b6a5ce0f355ac1b8e11af70e9b44b8cefe01a383a38880f108e10f78965c3a2ec526987b19771c62db4')
        self.assertEqual(mathematics.hashing('Lorem ipsum dolor sit amet, ex ius assum nonumes. Iudico conceptam consequuntur pri ei, mei no vero velit, et prompta fabulas rationibus vel. Ex vim magna'), 'b00f28ffa5ea37497072474c7d66cd891253070b05cf1c030cb56168614e03c8cfa80f728b002b2a6fb05099a47d84e9005566b184f3d43f999d501216666d79')
        
    def test_fib(self):
        self.assertEqual(mathematics.fib(0), 0)
        self.assertEqual(mathematics.fib(1), 1)
        self.assertEqual(mathematics.fib(10), 55)
        self.assertEqual(mathematics.fib(15), 610)
        self.assertEqual(mathematics.fib(-10), None)
        
    def test_pie(self):
        self.assertEqual(mathematics.pie(0), 1)
        self.assertEqual(mathematics.pie(1), 2)
        self.assertEqual(mathematics.pie(2), 4)
        self.assertEqual(mathematics.pie(10), 56)
        self.assertEqual(mathematics.pie(-112313210), None)

    def test_powerof(self):
        # ei katnud self.assertEqual(mathematics.powerof(-3, -3), -1/27)
        self.assertEqual(mathematics.powerof(4, 2), 16)
        self.assertEqual(mathematics.powerof(7, 1), 7)
        self.assertEqual(mathematics.powerof(8, 0), 1)
        self.assertEqual(mathematics.powerof(0, 2), 0)

    def test_arrayof(self):
        self.assertEqual(mathematics.arrayof(2, 3), [1, 2, 4, 8])
        self.assertEqual(mathematics.arrayof(4, 4), [1, 4, 16, 64, 256])
        self.assertEqual(mathematics.arrayof(8, 0), [1])
        self.assertEqual(mathematics.arrayof(0, 2), [1, 0, 0])

    def factorial(self):
        self.assertEqual(mathematics.factorial(4, 24))
        self.assertEqual(mathematics.factorial(7, 5040))
        self.assertEqual(mathematics.factorial(8, 40320))
        self.assertEqual(mathematics.factorial(0, 1))
        
if __name__=='__main__':
    unittest.main()
    
