import unittest
from Employee import *

class TestAssignment11(unittest.TestCase):
    
    def test_Employee(self):
        self.greg = Employee("Greg", "1234", "2/3/2023")
        
    def test_ProductionWorker(self):
        self.jody = ProductionWorker("jody", "7890", "1/21/22", "2", 34)
        
    def test_ShiftSupervisor(self):
        self.mckenzie= ShiftSupervisor("mckenzie", "4321", "3/7/22", "2", 44)
        
    def test_Manager(self):
        self.brittany = Manager("brittany", "1029", "4/20/2006", 90000, "3")

    # def test_RateAdjust(self):
    #     # self.greg.RateAdjust(Employee)
    #     self.assertEqual(self.greg.salary, 70000)

    # def test_give_custom_raise(self):
    #     ""Test that a custom raise works correctly.""
    #     self.eric.RateAdjust(10000)
    #     self.assertEqual(self.eric.salary, 75000)

if __name__ == '__main__':
    unittest.main()