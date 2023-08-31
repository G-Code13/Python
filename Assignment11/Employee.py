class Employee:
    def __init__(self, eName, eNumber, hireDate):
        self.__eName = eName
        self.__eNumber = eNumber
        self.__hireDate = hireDate
        
    def set_eName(self, eName):
        self.__eName = eName
        
    def set_eNumber(self, eNumber):
        self.__eNumber = eNumber
        
    def set_hireDate(self, hireDate):
        self.__hireDate = hireDate
        
    def get_eName(self):
        return self.__eName
    
    def get_eNumber(self):
        return self.__eNumber
        
    def get_hireDate(self):
        return self.__hireDate
    
    def tostring(self):
        return self.get_eName() + str(self.get_eNumber()) + self.get_hireDate()

#4% raise for employees
#10% raise for managers
#7.5% raise for shift supervisors
class RateAdjust(Employee):
    def __init__(self, adjustRate):
        self.__adjustRate = adjustRate
     
    def set_adjustRate(self, adjustRate):
        self.__adjustRate = adjustRate
        
    def get__adjustRate(self):
        return self.__adjustRate
     
class ProductionWorker(Employee):
    def __init__(self, eName, eNumber, hireDate, shiftNumber: int, payRate: float):
        super().__init__(eName, eNumber, hireDate)
        self.__shiftNumber = shiftNumber
        self.__payRate = payRate
        
        if self.__shiftNumber == 1:
            self.__shiftNumber == "Day Shift"
        elif self.__shiftNumber == 2:
            self.__shiftNumber == "Night Shift"
        else:
            print("Not a valid shift")
        return self.__shiftNumber
        
    def set_shiftNumber(self, shiftNumber):
        self.__shiftNumber = shiftNumber
            
    def set_payRate(self, payRate):
        self.__payRate = payRate
        
    def get_shiftNumber(self):
        return self.__shiftNumber
    
    def get_payRate(self):
        return self.__payRate
    
    def tostring(self):
        return self.get_eName() + str(self.get_eNumber()) + self.get_hireDate() + str(self.get_shiftNumber()) + str(self.get_payRate())

class ShiftSupervisor(Employee):
    def __init__(self, eName, eNumber, hireDate, shiftNumber: int, payRate: float):
        super().__init__(eName, eNumber, hireDate)
        self.__shiftNumber = shiftNumber
        self.__payRate = payRate
        
        if self.__shiftNumber == 1:
            self.__shiftNumber == "Day Shift"
        elif self.__shiftNumber == 2:
            self.__shiftNumber == "Night Shift"
        else:
            print("Not a valid shift")
        return self.__shiftNumber
    
    def set_shiftNumber(self, shiftNumber):
        self.__shiftNumber = shiftNumber
            
    def set_payRate(self, payRate):
        self.__payRate = payRate
        
    def get_shiftNumber(self):
        return self.__shiftNumber
    
    def get_payRate(self):
        return self.__payRate
        
    def toString(self):
        return  self.get_eName() + str(self.get_eNumber()) + self.get_hireDate() + str(self.get_shiftNumber()) + str(self.get_payRate())    

class Manager(Employee):
    def __init__(self, eName, eNumber, hireDate, salary: float, department):
        super().__init__(eName, eNumber, hireDate)
        self.__salary = salary
        self.__department = department

        if self.__department == 1:
            self.__department == "Front of Store"
        elif self.__department == 2:
            self.__department == "Back of Store"
        else:
            print("Floater")
        return self.__department
        
    def set_salary(self, salary):
        self.__salary = salary
        
    def set_department(self, department):
        self.__department = department
    
    def get_salary(self):
        return self.__salary
    
    def set_department(self):
        return self.__department
        
       

       
def main():
    pass
if __name__ == "__main__":
    main()           

