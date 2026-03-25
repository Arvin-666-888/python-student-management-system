"""
面向对象进阶 - 学生管理系统类封装
        要求:
            1.将学生管理所有功能封装成一个类
            2.类包含：数据属性、增删改查、文件持久化方法
            3.主程序仅创建对象、调用方法
            4.彻底理解面向对象编程（OOP） 的优势
"""
import os

# 完整封装：学生管理系统类
class StudentManager:
    # 初始化方法:程序启动自动加载数据
    def __init__(self):
        self.FILE_PATH = "student.txt"  # 文件路径
        self.students = []  # 存储学生数据
        self.load_data()    # 启动加载历史数据

    # 1. 从文件加载数据
    def load_data(self):
        # 判断:如果存放学生数据的文件不存在
        if not os.path.exists(self.FILE_PATH):
            self.students = []  # 没有数据文件，就从零开始创建学生列表
            return # 直接结束当前函数,不再执行后续代码
        try:
            with open(self.FILE_PATH,"r",encoding="utf-8") as f:
                # 每次读文件前先重置,避免旧数据重复叠加,马上要从新文件加载新数据
                self.students = []
                for line in f.readlines():
                    line = line.strip() # 去除首尾空白
                    if line:
                        name,age,sid = line.split(",")
                        self.students.append({"name":name,"age":age,"id":sid})
            print("✅ 历史数据加载成功!")
        except  Exception as e:
            print(f"❌ 数据加载失败:{e}")

    # 2. 保存数据到文件
    def save_data(self):
        try:
            with open(self.FILE_PATH,"w",encoding="utf-8") as f:
                for stu in self.students:   # 把学生数据一个个传进去
                    f.write(f"{stu['name']},{stu['age']},{stu['id']}\n")
            print("✅ 数据保存成功!")
        except Exception as e:
            print(f"❌ 数据保存失败:{e}")

    # 3. 添加学生（年龄强制输入整数，带异常处理）
    def add_student(self):
        name = input("请输入学生姓名:")
        # 循环强制输入数字年龄，直到输入正确
        while True:
            try:
                age = int(input("请输入学生年龄:"))
                # 限制年龄合理范围 1-150 岁
                if 0 < age < 150:
                    break   # 跳出最近一层循环
                else:
                    print("⚠️ 年龄必须在1-150之间！")
            except ValueError:
                # 输入非数字（字母、中文）触发异常
                print("❌ 输入错误！年龄只能输入整数！")

        student_id = input("请输入学生学号:")
        # 存储的 age 是整数类型
        self.students.append({"name": name, "age": age, "id": student_id})
        print("✅ 添加成功！")

    # 4. 查询学生
    def show_students(self):
        if not self.students:
            print("📪 暂无学生信息!")
            return
        print("\n===== 学生列表 =====")
        for i,stu in enumerate(self.students,1):
            print(f"{i}.姓名:{stu['name']},年龄:{stu['age']},学号:{stu['id']}")

    # 5. 修改学生
    def update_student(self):
        name = input("请输入你要修改的学生姓名:")
        for stu in self.students:
            if stu['name'] == name:
                stu['age'] = input("请输入新年龄:")
                stu['id'] = input("请输入新学号:")
                print("✅ 修改成功!")
                return
        print("❌ 未找到该学生")

    # 6. 删除学生
    def del_student(self):
        name = input("请输入你要修改的学生姓名:")
        for stu in self.students:
            if stu['name'] == name:
                # self.students.remove(name)    这样的话会在列表中寻找值为'张三'的元素,但列表里只有字典
                self.students.remove(stu)   # 直接把这个人的全部信息删了
                print("✅ 删除成功!")
                self.save_data()
                return      # 函数立即结束,不再执行后续代码.是跳出函数
        print("❌ 未找到该学生")


# 主程序:创建对象,调用功能
if __name__ == "__main__":
    print("="*40)
    print(" 面向对象版学生管理系统")
    print("="*40)

    # 创建管理系统对象
    manager = StudentManager()

    # 主菜单
    while True:
        print("\n1. 添加学生  2. 查询学生  3.修改学生  4.删除学生 5. 保存并退出")
        choice = input("请输入功能编号:")

        if choice =="1":
            manager.add_student()
        elif choice == "2":
            manager.show_students()
        elif choice == "3":
            manager.update_student()
        elif choice == "4":
            manager.del_student()
        elif choice == "5":
            print("👋 系统退出")
            break
        else:
            print("⚠️ 输入错误!请重新选择!")
