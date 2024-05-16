class Dog2:
    """클래스 Dog 정의"""

    def __init__(self, name, age): #속성정의 / __ : 자동호출
        """클래스 Dog의 생성자"""
        self.name = name #self.속성 = 값 /속성에 값 할당
        self.age = age
        self.city = "busan"

    def sit(self):
        """개가 앉기 동작"""
        print(f"개가 앉기 {self.name}")

myDog = Dog2("hong", 10) #Dog2 인스턴스를 만들때 생성자(__init__)자동 호출함
myDog.sit() #myDog는 sit를 제공할 객체. sit는 self를 가리키는 함수호출

#til.31 클래스의 속성 참고 https://codermun-log.tistory.com/73