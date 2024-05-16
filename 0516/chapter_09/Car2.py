class Car2:
    """자동차 클래스"""

    def __init__(self, make, model, year, color):
        """생성자 초기화"""
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.odometer = 0

    def __str__(self):
        return f"[{self.make},{self.model}]"

    def fill_gas_tank(self):
        print(f"휘발류 차의 탱크")
    def get_descriptive_name(self):
        """자동차 객체 기술"""
        long_name = f"{self.year}식 {self.make}제조사 {self.model}\n 색상 {self.color}"
        return long_name
    
    def update_odometer(self, mileage):
        print(f"주행기록계")

class Battery():
    def __init__(self, battery_size=40):
        self.battery_size = battery_size

class ElectricCar(Car2):
    """슈퍼클래스의 subclass"""
    def __init__(self, make, model, year, color):
        """슈퍼클래스의 생성자 호출"""
        super().__init__(make, model, year, color)
    def fill_gas_tank(self):
        super().fill_gas_tank()
        print(f"전기차는 탱크 없음")
        self.battery = Battery() #클래스 Battery의 생성자

my_new_car = Car2('audi', 'a6', 2024, 'red')
print(my_new_car) #출력하기 위해서는 string 필요 > 객체를 str으로 변환이 필요 > __str__() 자동 호출
print(my_new_car.get_descriptive_name())
my_new_car.color = 'green' #클래스 객체의 attribute는 
print(my_new_car.get_descriptive_name())
my_ElectricCar = ElectricCar('kia','k3',2024,'red')
my_ElectricCar.fill_gas_tank()

# 파이썬 더블던더 메소드 참고 https://blog.naver.com/youndok/222566232550