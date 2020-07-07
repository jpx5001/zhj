
class Person_1:
    mind = '有思想'
    belif = '有信仰'
    animal = '高级动物'


    def tt():
        pass

print(Person_1.__dict__)  # 查询类Person中所有的内容,表现形式是字典.
print(Person_1.__dict__['belif'])  # 查询类Person中的变量'belif'


class Person_2:
    mind = '有思想'
    belif = '有信仰'
    animal = '高级动物'

    def work():
        print('666')

    def money():
        print('777')

print(Person_2.animal)  # 高级动物
print(Person_2.mind)  # 有思想
Person_2.mind = '没有思想'  # 修改变量'mind'的值,可以通过__dicy__查看修改后的内容
Person_2.pay = '货币交换'  # 增加变量'pay'和它的值,可以通过__dicy__查看增加后的内容
Person_2.say = '语言交流'
print(Person_2.work())  # 也可以调用类中的方法(函数),工作中不用类名去操作
print(Person_2.__dict__)  # 查看类中所有的内容
