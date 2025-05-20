class test:
    name="weizhi"
    age=18
    def __init__(self,name,age):
        self.name1=name
        self.age1=age
        print("构造函数====")
    def __del__(self):
        print("析构函数=====")
    def __str__(self):
        print("直接输出实例化对象时调用")
    def _pro(self):
        print("这是一个保护方法")#事实上这个保护方法只是道德上的约束，依旧可以在类外调用
    def __pri(self):
        print("这是一个私有方法")
    @classmethod
    def test(cls1,name,age):
        print(f"{cls1.name},{cls1.age}")
        #print(f"{cls1.name1},{cls1.age1}")error 类方法通过关键字只能使用类属性
    @staticmethod
    def test1(cls1,name,age):
        print(f"{name},{age}")#没有关键字
class zi(test):
    def _pro(self):
        print("该方法已重写")
if __name__=="__main__":
    nb=test("lisi",40)
    nb._pro()#类外调用保护方法
    nb.test("lisi1111111",40)
    nb.test1("gg","lisi22222222",40)