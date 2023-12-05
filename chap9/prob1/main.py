class Critter:
    """A virtual pet"""  # 클래스 정의
    def talk(self):  # 내부 함수는 self를 무조건 써야 메소드로 인정함
        print("Hi. I'm an instance of class Critter.")

# main
crit = Critter()
crit.talk()

n = input('Press the enter key to exit.')
