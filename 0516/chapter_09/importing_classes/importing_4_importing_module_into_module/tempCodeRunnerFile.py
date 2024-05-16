        class ElectricCar(Car2):
            """슈퍼클래스의 subclass"""
            def __init__(self, make, model, year, color):
                """슈퍼클래스의 생성자 호출"""
                super().__init__(make, model, year, color)
