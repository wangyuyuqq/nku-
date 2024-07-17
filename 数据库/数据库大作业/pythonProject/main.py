import pymysql
from tkinter import ttk
import tkinter as tk
import tkinter.font as tkFont
from tkinter import *    # 图形界面库
import tkinter.messagebox as messagebox    # 弹窗
from PIL import Image, ImageTk
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x_cordinate = int((screen_width / 2) - (width / 2))
    y_cordinate = int((screen_height / 2) - (height / 2))
    window.geometry(f"{width}x{height}+{x_cordinate}+{y_cordinate}")
class StartPage:
    def __init__(self, parent_window):
        parent_window.destroy()  # 销毁子界面,从别处返回后销毁原界面

        self.window = tk.Tk()  # 初始框的声明
        self.window.title('教务信息管理系统')
        self.window.geometry('400x600')  # 这里的乘是小x
        center_window(self.window, 400, 600)  # 设置窗口在屏幕中央
        # 设置背景图片
        self.bg_image = Image.open("background.jpg")
        self.bg_image = self.bg_image.resize((400, 600), Image.Resampling.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        self.bg_label = tk.Label(self.window, image=self.bg_photo)
        self.bg_label.place(relwidth=1, relheight=1)

        # 主标题
        label = tk.Label(self.window, text="教务信息管理系统", font=("Verdana", 24), bg='skyblue', fg='white')
        label.pack(pady=40)  # pady=40 界面的长度
        # 设置按钮样式
        style = ttk.Style()
        style.configure('TButton', font=('Verdana', 16), padding=10)
        style.map('TButton', background=[('active', '#45a049')], foreground=[('active', 'white')])
        # 按钮样式
        button_style = {
            'width': 20,
            'style': 'TButton'
        }

        # 创建按钮
        ttk.Button(self.window, text="管理员登录", command=lambda: AdminPage(self.window), **button_style).pack(pady=10)
        ttk.Button(self.window, text="学生登录", command=lambda: StudentPage(self.window), **button_style).pack(pady=10)
        ttk.Button(self.window, text="教师登录", command=lambda: TeacherPage(self.window), **button_style).pack(pady=10)
        ttk.Button(self.window, text="关于", command=lambda: AboutPage(self.window), **button_style).pack(pady=10)
        ttk.Button(self.window, text='退出系统', command=self.window.destroy, **button_style).pack(pady=10)

        self.window.mainloop()  # 主消息循环
# 管理员登陆页面
class AdminPage:
    def __init__(self, parent_window):
        parent_window.destroy()  # 销毁主界面

        self.window = tk.Tk()  # 初始框的声明
        self.window.title('管理员登录')
        self.window.geometry('800x600')  # 这里的乘是小x
        center_window(self.window, 800, 600)  # 设置窗口在屏幕中央
        # 设置背景图片
        self.bg_image = Image.open("background.jpg")
        self.bg_image = self.bg_image.resize((800, 600), Image.Resampling.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        self.bg_label = tk.Label(self.window, image=self.bg_photo)
        self.bg_label.place(relwidth=1, relheight=1)

        # 登录框架
        self.login_frame = tk.Frame(self.window, bg='white', bd=2, relief="ridge")
        self.login_frame.place(relx=0.5, rely=0.5, anchor="center", width=350, height=450)

        # 标题
        self.title_label = tk.Label(self.login_frame, text="管理员登录", font=("Verdana", 24), bg='white')
        self.title_label.pack(pady=20)

        # 用户名
        self.user_label = tk.Label(self.login_frame, text="管理员账号", font=("Verdana", 14), bg='white')
        self.user_label.pack(pady=10, anchor='w', padx=20)
        self.admin_username = tk.Entry(self.login_frame, width=30, font=("Verdana", 14), bd=2, relief="groove")
        self.admin_username.pack(pady=10, padx=20)

        # 密码
        self.pass_label = tk.Label(self.login_frame, text="管理员密码", font=("Verdana", 14), bg='white')
        self.pass_label.pack(pady=10, anchor='w', padx=20)
        self.admin_pass = tk.Entry(self.login_frame, width=30, font=("Verdana", 14), show='*', bd=2, relief="groove")
        self.admin_pass.pack(pady=10, padx=20)

        # 登录按钮
        self.login_button = tk.Button(self.login_frame, text="登录", font=("Verdana", 14), bg='green', fg='white', bd=2, relief="groove", command=self.login)
        self.login_button.pack(pady=20)

        # 返回首页按钮
        self.back_button = tk.Button(self.login_frame, text="返回首页", font=("Verdana", 14), bg='grey', fg='white', bd=2, relief="groove", command=self.back)
        self.back_button.pack(pady=10)

        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击
        self.window.mainloop()  # 进入消息循环

    def login(self):
        print(str(self.admin_username.get()))
        print(str(self.admin_pass.get()))
        admin_pass = None

        # 数据库操作 查询管理员表
        # 打开数据库连接 autocommit为自动连接参数
        db = pymysql.connect(host="localhost", user="root", password="wy1211..", database="emp_project", port=3306)
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "SELECT * FROM admin_login WHERE admin_id = '%s'" % (self.admin_username.get())  # SQL 查询语句
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                admin_id = row[0]
                admin_pass = row[1]
                # 打印结果
                print("admin_id=%s,admin_pass=%s" % (admin_id, admin_pass))
        except:
            print("Error: unable to fetch data")
            messagebox.showinfo('警告！', '用户名或密码不正确！')
        db.close()  # 关闭数据库连接

        print("正在登陆管理员管理界面")
        print("self", self.admin_pass)
        print("local", admin_pass)

        if self.admin_pass.get() == admin_pass:
            AdminManage(self.window,self.admin_username.get())  # 进入管理员操作界面
        else:
            messagebox.showinfo('警告！', '用户名或密码不正确！')

    def back(self):
        StartPage(self.window)  # 显示主窗口 销毁本窗口
# 学生登录页面
class StudentPage:
    def __init__(self, parent_window):
        parent_window.destroy()  # 销毁主界面

        self.window = tk.Tk()  # 初始框的声明
        self.window.title('学生登录')
        self.window.geometry('800x600')  # 这里的乘是小x
        center_window(self.window, 800, 600)  # 设置窗口在屏幕中央
        # 设置背景图片
        self.bg_image = Image.open("background.jpg")
        self.bg_image = self.bg_image.resize((800, 600), Image.Resampling.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        self.bg_label = tk.Label(self.window, image=self.bg_photo)
        self.bg_label.place(relwidth=1, relheight=1)

        # 登录框架
        self.login_frame = tk.Frame(self.window, bg='white', bd=2, relief="ridge")
        self.login_frame.place(relx=0.5, rely=0.5, anchor="center", width=400, height=450)

        # 标题
        self.title_label = tk.Label(self.login_frame, text="学生登录", font=("Verdana", 24), bg='white')
        self.title_label.pack(pady=20)

        # 用户名
        self.user_label = tk.Label(self.login_frame, text="学生账号", font=("Verdana", 14), bg='white')
        self.user_label.pack(pady=10, anchor='w', padx=20)
        self.user_entry = tk.Entry(self.login_frame, width=30, font=("Verdana", 14), bd=2, relief="groove")
        self.user_entry.pack(pady=10, padx=20)

        # 密码
        self.pass_label = tk.Label(self.login_frame, text="学生密码", font=("Verdana", 14), bg='white')
        self.pass_label.pack(pady=10, anchor='w', padx=20)
        self.pass_entry = tk.Entry(self.login_frame, width=30, font=("Verdana", 14), show='*', bd=2, relief="groove")
        self.pass_entry.pack(pady=10, padx=20)

        # 登录按钮
        self.login_button = tk.Button(self.login_frame, text="登录", font=("Verdana", 14), bg='green', fg='white', bd=2, relief="groove", command=self.login)
        self.login_button.pack(pady=20)

        # 返回首页按钮
        self.back_button = tk.Button(self.login_frame, text="返回首页", font=("Verdana", 14), bg='gray', fg='white', bd=2, relief="groove", command=self.back)
        self.back_button.pack(pady=10)

        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击
        self.window.mainloop()  # 进入消息循环

    def login(self):
        print(str(self.user_entry.get()))
        print(str(self.pass_entry.get()))
        stu_pass = None

        # 数据库操作 查询学生表
        db = pymysql.connect(host="localhost", user="root", password="wy1211..", database="emp_project", port=3306)
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "SELECT * FROM student_login WHERE stu_id = '%s'" % (self.user_entry.get())  # SQL 查询语句
        try:
            cursor.execute(sql)  # 执行SQL语句
            results = cursor.fetchall()  # 获取所有记录列表
            for row in results:
                stu_id = row[0]
                stu_pass = row[1]
                print(stu_pass)
                print("stu_id=%s,stu_pass=%s" % (stu_id, stu_pass))  # 打印结果
        except:
            print("Error: unable to fetch data")
            messagebox.showinfo('警告！', '用户名或密码不正确！')
        db.close()  # 关闭数据库连接

        print("正在登录学生信息查看界面")
        print("self", self.pass_entry.get())
        print("local", stu_pass)

        if self.pass_entry.get() == stu_pass:
            StudentView(self.window, self.user_entry.get())  # 进入学生信息查看界面
        else:
            messagebox.showinfo('警告！', '用户名或密码不正确！')

    def back(self):
        StartPage(self.window)  # 显示主窗口 销毁本窗口
# 教师登录页面
class TeacherPage:
    def __init__(self, parent_window):
        parent_window.destroy()  # 销毁主界面

        self.window = tk.Tk()  # 初始框的声明
        self.window.title('教师登录')
        self.window.geometry('800x600')  # 这里的乘是小x
        center_window(self.window, 800, 600)  # 设置窗口在屏幕中央
        # 设置背景图片
        self.bg_image = Image.open("background.jpg")
        self.bg_image = self.bg_image.resize((800, 600), Image.Resampling.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        self.bg_label = tk.Label(self.window, image=self.bg_photo)
        self.bg_label.place(relwidth=1, relheight=1)

        # 登录框架
        self.login_frame = tk.Frame(self.window, bg='white', bd=2, relief="ridge")
        self.login_frame.place(relx=0.5, rely=0.5, anchor="center", width=400, height=450)

        # 标题
        self.title_label = tk.Label(self.login_frame, text="教师登录", font=("Verdana", 24), bg='white')
        self.title_label.pack(pady=20)

        # 用户名
        self.user_label = tk.Label(self.login_frame, text="用户名", font=("Verdana", 14), bg='white')
        self.user_label.pack(pady=10, anchor='w', padx=20)
        self.user_entry = tk.Entry(self.login_frame, width=30, font=("Verdana", 14), bd=2, relief="groove")
        self.user_entry.pack(pady=10, padx=20)

        # 密码
        self.pass_label = tk.Label(self.login_frame, text="密码", font=("Verdana", 14), bg='white')
        self.pass_label.pack(pady=10, anchor='w', padx=20)
        self.pass_entry = tk.Entry(self.login_frame, width=30, font=("Verdana", 14), show='*', bd=2, relief="groove")
        self.pass_entry.pack(pady=10, padx=20)

        # 登录按钮
        self.login_button = tk.Button(self.login_frame, text="登录", font=("Verdana", 14), bg='green', fg='white', bd=2, relief="groove", command=self.login)
        self.login_button.pack(pady=20)

        # 返回首页按钮
        self.back_button = tk.Button(self.login_frame, text="返回首页", font=("Verdana", 14), bg='gray', fg='white', bd=2, relief="groove", command=self.back)
        self.back_button.pack(pady=10)

        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击
        self.window.mainloop()  # 进入消息循环

    def login(self):
        print(str(self.user_entry.get()))
        print(str(self.pass_entry.get()))
        teacher_pass = None

        # 数据库操作 查询教师表
        db = pymysql.connect(host="localhost", user="root", password="wy1211..", database="emp_project", port=3306)
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "SELECT * FROM teacher_login WHERE tea_id = '%s'" % (self.user_entry.get())  # SQL 查询语句
        try:
            cursor.execute(sql)  # 执行SQL语句
            results = cursor.fetchall()  # 获取所有记录列表
            for row in results:
                tea_id = row[0]
                tea_pwd = row[1]
                print("teacher_id=%s, teacher_pass=%s" % (tea_id, tea_pwd))  # 打印结果
        except:
            print("Error: unable to fetch data")
            messagebox.showinfo('警告！', '用户名或密码不正确！')
        db.close()  # 关闭数据库连接

        print("正在登录教师管理界面")
        print("self", self.pass_entry.get())
        print("local", tea_pwd)

        if self.pass_entry.get() == tea_pwd:
            TeacherView(self.window,self.user_entry.get())  # 进入教师管理界面
        else:
            messagebox.showinfo('警告！', '用户名或密码不正确！')

    def back(self):
        StartPage(self.window)  # 显示主窗口 销毁本窗口
# 管理员操作界面
class AdminManage:
    def __init__(self, parent_window,admin_id=None):
        parent_window.destroy()  # 销毁子界面，确保不会有多个Tk实例

        self.window = tk.Tk()  # 创建一个新的Tk实例，即新的窗口
        self.window.title('管理员操作界面')  # 设置窗口标题
        center_window(self.window, 400, 600)  # 设置窗口在屏幕中央

        # 设置背景图片
        self.bg_image = Image.open("background.jpg")
        self.bg_image = self.bg_image.resize((400, 600), Image.Resampling.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        self.bg_label = tk.Label(self.window, image=self.bg_photo)
        self.bg_label.place(relwidth=1, relheight=1)

        # 主标题
        self.title_label = tk.Label(self.window, text="请选择操作", font=("Verdana", 24), bg='skyblue', fg='white')
        self.title_label.pack(pady=20)

        # 设置按钮样式
        style = ttk.Style()
        style.configure('TButton', font=('Verdana', 16), padding=10)
        style.map('TButton', background=[('active', '#45a049')], foreground=[('active', 'white')])

        # 按钮样式
        button_style = {
            'width': 20,
            'style': 'TButton'
        }
        if admin_id!=None:
            admin_name = self.get_admin_name(admin_id)
            messagebox.showinfo('欢迎', f'欢迎你！管理员 {admin_name}')
        # 创建按钮
        ttk.Button(self.window, text="学生信息", command=lambda: Student(self.window), **button_style).pack(pady=10)
        ttk.Button(self.window, text="教师信息", command=lambda: Teacher(self.window), **button_style).pack(pady=10)
        ttk.Button(self.window, text="课程信息", command=lambda: Lesson(self.window), **button_style).pack(pady=10)

        ttk.Button(self.window, text="选课信息", command=lambda: Learn(self.window), **button_style).pack(pady=10)
        ttk.Button(self.window, text="授课信息", command=lambda: Teach(self.window), **button_style).pack(pady=10)
        ttk.Button(self.window, text="学生课程信息", command=lambda: StudentCourseInfoView(self.window),
                   **button_style).pack(pady=10)

        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击
        self.window.mainloop()  # 进入消息循环

    def get_admin_name(self, admin_id):
        db = pymysql.connect(host="localhost", user="root", password="wy1211..", database="emp_project", port=3306)
        cursor = db.cursor()
        sql = "SELECT tea_name FROM teacher WHERE tea_id = %s"
        try:
            cursor.execute(sql, (admin_id,))
            result = cursor.fetchone()
            if result:
                return result[0]
            else:
                return "未知"
        except Exception as e:
            print("Error: unable to fetch data")
            messagebox.showinfo('警告！', f'数据库连接失败！\n错误信息：{e}')
            return "未知"
        finally:
            db.close()  # 关闭数据库连接
    def back(self):
        StartPage(self.window)  # 显示主窗口 销毁本窗口
# 学生信息界面
class Student:
    def __init__(self, parent_window):
        parent_window.destroy()  # 销毁主界面
        self.window = tk.Tk()  # 初始框的声明
        self.window.title('学生信息')
        center_window(self.window, 750, 600)  # 设置窗口在屏幕中央

        # 设置背景图片
        self.bg_image = Image.open("background2.jpg")
        self.bg_image = self.bg_image.resize((750, 600), Image.Resampling.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        self.bg_label = tk.Label(self.window, image=self.bg_photo)
        self.bg_label.place(relwidth=1, relheight=1)

        # 定义框架
        self.frame_left_top = tk.Frame(self.window, bg='white', width=300, height=200)
        self.frame_right_top = tk.Frame(self.window, bg='white', width=200, height=200)
        self.frame_center = tk.Frame(self.window, bg='white', width=500, height=400)
        self.frame_bottom = tk.Frame(self.window, bg='white', width=750, height=50)

        # 定义下方中心列表区域
        self.columns = ("学号", "姓名", "性别", "学院")
        self.tree = ttk.Treeview(self.frame_center, show="headings", height=18, columns=self.columns)
        self.vbar = ttk.Scrollbar(self.frame_center, orient=tk.VERTICAL, command=self.tree.yview)
        self.hbar = ttk.Scrollbar(self.frame_center, orient=tk.HORIZONTAL, command=self.tree.xview)
        self.tree.configure(yscrollcommand=self.vbar.set, xscrollcommand=self.hbar.set)

        # 表格的标题
        self.tree.column("学号", width=100, anchor='center')
        self.tree.column("姓名", width=100, anchor='center')
        self.tree.column("性别", width=100, anchor='center')
        self.tree.column("学院", width=200, anchor='center')

        # 调用方法获取表格内容插入
        self.tree.grid(row=0, column=0, sticky=tk.NSEW)
        self.vbar.grid(row=0, column=1, sticky=tk.NS)
        self.hbar.grid(row=1, column=0, sticky=tk.EW)

        self.frame_center.grid_rowconfigure(0, weight=1)
        self.frame_center.grid_columnconfigure(0, weight=1)

        self.id = []
        self.name = []
        self.gender = []
        self.college = []
        # 打开数据库连接
        db = pymysql.connect(host="localhost", user="root", password="wy1211..", database="emp_project", port=3306)
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "SELECT * FROM student"  # SQL 查询语句
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                self.id.append(row[0])
                self.name.append(row[1])
                self.gender.append(row[2])
                self.college.append(row[4])
        except:
            print("Error: unable to fetch data")
            messagebox.showinfo('警告！', '数据库连接失败！')
        db.close()  # 关闭数据库连接

        # 写入数据
        for i in range(min(len(self.id), len(self.name), len(self.gender), len(self.college))):
            self.tree.insert('', i, values=(self.id[i], self.name[i], self.gender[i], self.college[i]))

        for col in self.columns:  # 绑定函数，使表头可排序
            self.tree.heading(col, text=col,
                              command=lambda _col=col: self.tree_sort_column(self.tree, _col, False))

        # 定义顶部区域
        # 定义左上方区域
        self.top_title = Label(self.frame_left_top, text="学生信息:", font=('Verdana', 20), bg='white')
        self.top_title.grid(row=0, column=0, columnspan=2, sticky=tk.NSEW, padx=50, pady=10)

        self.var_id = StringVar()  # 声明学号
        self.var_name = StringVar()  # 声明姓名
        self.var_gender = StringVar()  # 声明性别
        self.var_college = StringVar()  # 声明学院
        # 学号
        self.right_top_id_label = Label(self.frame_left_top, text="学号：", font=('Verdana', 15), bg='white')
        self.right_top_id_entry = Entry(self.frame_left_top, textvariable=self.var_id, font=('Verdana', 15))
        self.right_top_id_label.grid(row=1, column=0)  # 位置设置
        self.right_top_id_entry.grid(row=1, column=1)
        # 姓名
        self.right_top_name_label = Label(self.frame_left_top, text="姓名：", font=('Verdana', 15), bg='white')
        self.right_top_name_entry = Entry(self.frame_left_top, textvariable=self.var_name, font=('Verdana', 15))
        self.right_top_name_label.grid(row=2, column=0)  # 位置设置
        self.right_top_name_entry.grid(row=2, column=1)
        # 性别
        self.right_top_gender_label = Label(self.frame_left_top, text="性别：", font=('Verdana', 15), bg='white')
        self.right_top_gender_entry = Entry(self.frame_left_top, textvariable=self.var_gender, font=('Verdana', 15))
        self.right_top_gender_label.grid(row=3, column=0)  # 位置设置
        self.right_top_gender_entry.grid(row=3, column=1)
        # 学院
        self.right_top_college_label = Label(self.frame_left_top, text="学院：", font=('Verdana', 15), bg='white')
        self.right_top_college_entry = Entry(self.frame_left_top, textvariable=self.var_college, font=('Verdana', 15))
        self.right_top_college_label.grid(row=4, column=0)  # 位置设置
        self.right_top_college_entry.grid(row=4, column=1)

        # 定义右上方区域
        self.right_top_title = Label(self.frame_right_top, text="操作：", font=('Verdana', 20), bg='white')
        self.tree.bind('<Button-1>', self.click)  # 左键获取位置
        self.right_top_button1 = ttk.Button(self.frame_right_top, text='添加学生信息', width=20, command=self.new_row)
        self.right_top_button2 = ttk.Button(self.frame_right_top, text='更新学生信息', width=20, command=self.updata_row)
        self.right_top_button3 = ttk.Button(self.frame_right_top, text='删除学生信息', width=20, command=self.del_row)

        # 位置设置
        self.right_top_title.grid(row=0, column=0, pady=10)
        self.right_top_button1.grid(row=1, column=0, padx=20, pady=10)
        self.right_top_button2.grid(row=2, column=0, padx=20, pady=10)
        self.right_top_button3.grid(row=3, column=0, padx=20, pady=10)

        # 整体区域定位
        self.frame_left_top.grid(row=0, column=0, padx=10, pady=10, sticky=tk.NSEW)
        self.frame_right_top.grid(row=0, column=1, padx=10, pady=10, sticky=tk.NSEW)
        self.frame_center.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky=tk.NSEW)
        self.frame_bottom.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky=tk.NSEW)

        self.frame_left_top.grid_propagate(False)
        self.frame_right_top.grid_propagate(False)
        self.frame_center.grid_propagate(False)
        self.frame_bottom.grid_propagate(False)

        self.frame_left_top.tkraise()
        self.frame_right_top.tkraise()
        self.frame_center.tkraise()
        self.frame_bottom.tkraise()

        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击
        self.window.mainloop()  # 进入消息循环

    def back(self):
        AdminManage(self.window)  # 显示主窗口 销毁本窗口

    def click(self, event):
        self.col = self.tree.identify_column(event.x)  # 列
        self.row = self.tree.identify_row(event.y)  # 行
        self.row_info = self.tree.item(self.row, "values")
        self.var_id.set(self.row_info[0])
        self.var_name.set(self.row_info[1])
        self.var_gender.set(self.row_info[2])
        self.var_college.set(self.row_info[3])

    def tree_sort_column(self, tv, col, reverse):  # Treeview、列名、排列方式
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        l.sort(reverse=reverse)  # 排序方式
        for index, (val, k) in enumerate(l):  # 根据排序后索引移动
            tv.move(k, '', index)
        tv.heading(col, command=lambda: self.tree_sort_column(tv, col, not reverse))  # 重写标题，使之成为再点倒序的标题

    def new_row(self):
        if str(self.var_id.get()) in self.id:
            messagebox.showinfo('警告！', '该学号已被占用！')
        else:
            if self.var_id.get() != '' and self.var_name.get() != '' and self.var_gender.get() != '':
                db = pymysql.connect(host="localhost", user="root", password="wy1211..", database="emp_project", port=3306)
                cursor = db.cursor()
                sql = "INSERT INTO student(stu_id, stu_name, stu_gender, stu_adm_time, stu_college) VALUES (%s, %s, %s, '2024-05-30', %s)"
                try:
                    cursor.execute(sql, (self.var_id.get(), self.var_name.get(), self.var_gender.get(), self.var_college.get()))
                    db.commit()
                    messagebox.showinfo('提示！', '插入成功！')
                    self.id.append(self.var_id.get())
                    self.name.append(self.var_name.get())
                    self.gender.append(self.var_gender.get())
                    self.college.append(self.var_college.get())
                    self.tree.insert('', len(self.id) - 1, values=(
                        self.id[len(self.id) - 1], self.name[len(self.id) - 1], self.gender[len(self.id) - 1], self.college[len(self.id) - 1]))
                    self.tree.update()
                except:
                    db.rollback()
                    messagebox.showinfo('警告！', '数据库连接失败！')
                db.close()
            else:
                messagebox.showinfo('警告！', '请填写必要学生数据')

    def updata_row(self):
        res = messagebox.askyesnocancel('警告！', '是否更新所填数据？')
        if res:
            if self.var_id.get() == self.row_info[0]:
                db = pymysql.connect(host="localhost", user="root", password="wy1211..", database="emp_project",
                                     port=3306)
                cursor = db.cursor()
                sql = "UPDATE student SET stu_name = %s, stu_gender = %s, stu_college = %s WHERE stu_id = %s"
                sql_update_major = "CALL update_student_major(%s, %s)"
                try:
                    if self.var_college.get() != self.row_info[3]:
                        cursor.execute(sql_update_major, (self.var_id.get(), self.var_college.get()))
                    cursor.execute(sql, (
                    self.var_name.get(), self.var_gender.get(), self.var_college.get(), self.var_id.get()))
                    db.commit()
                    messagebox.showinfo('提示！', '转专业成功！')

                    id_index = self.id.index(self.row_info[0])
                    self.name[id_index] = self.var_name.get()
                    self.gender[id_index] = self.var_gender.get()
                    self.college[id_index] = self.var_college.get()

                    self.tree.item(self.tree.selection()[0], values=(
                        self.var_id.get(), self.var_name.get(), self.var_gender.get(), self.var_college.get()))
                except pymysql.MySQLError as e:
                    db.rollback()
                    messagebox.showinfo('警告！', str(e))
                finally:
                    db.close()
            else:
                messagebox.showinfo('提示！', '不能更改学生学号哦！')

    def del_row(self):
        res = messagebox.askyesnocancel('警告！', '是否删除所选数据？')
        if res:
            db = pymysql.connect(host="localhost", user="root", password="wy1211..", database="emp_project", port=3306)
            cursor = db.cursor()
            sql="BEGIN"
            sql1 = "DELETE FROM student WHERE stu_id = '%s'" % (self.row_info[0])
            sql2 = "DELETE FROM student_login WHERE stu_id =' %s'" % (self.row_info[0])
            sql3 = "DELETE FROM learn WHERE stu_id = '%s'" % (self.row_info[0])
            sql4 = "COMMIT"
            try:
                cursor.execute(sql)
                cursor.execute(sql1)
                cursor.execute(sql2)
                cursor.execute(sql3)
                cursor.execute(sql4)
                db.commit()
                messagebox.showinfo('提示！', '删除成功！连同学生的登录信息，选课信息一起删除!')
                id_index = self.id.index(self.row_info[0])
                del self.id[id_index]
                del self.name[id_index]
                del self.gender[id_index]
                del self.college[id_index]
                self.tree.delete(self.tree.selection()[0])
            except:
                db.rollback()
                messagebox.showinfo('警告！', '数据库连接失败！')
            db.close()
# 教师信息界面
class Teacher:
    def __init__(self, parent_window):
        parent_window.destroy()  # 销毁主界面

        self.window = tk.Tk()  # 初始框的声明
        self.window.title('教师信息')
        center_window(self.window, 750, 600)  # 设置窗口在屏幕中央

        # 设置背景图片
        self.bg_image = Image.open("background2.jpg")
        self.bg_image = self.bg_image.resize((750, 600), Image.Resampling.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        self.bg_label = tk.Label(self.window, image=self.bg_photo)
        self.bg_label.place(relwidth=1, relheight=1)

        # 定义框架
        self.frame_left_top = tk.Frame(self.window, bg='white', width=300, height=200)
        self.frame_right_top = tk.Frame(self.window, bg='white', width=200, height=200)
        self.frame_center = tk.Frame(self.window, bg='white', width=500, height=400)
        self.frame_bottom = tk.Frame(self.window, bg='white', width=750, height=50)

        # 定义下方中心列表区域
        self.columns = ("职工号", "姓名", "职称", "薪水")
        self.tree = ttk.Treeview(self.frame_center, show="headings", height=18, columns=self.columns)
        self.vbar = ttk.Scrollbar(self.frame_center, orient=tk.VERTICAL, command=self.tree.yview)
        self.hbar = ttk.Scrollbar(self.frame_center, orient=tk.HORIZONTAL, command=self.tree.xview)
        self.tree.configure(yscrollcommand=self.vbar.set, xscrollcommand=self.hbar.set)

        # 表格的标题
        self.tree.column("职工号", width=100, anchor='center')
        self.tree.column("姓名", width=100, anchor='center')
        self.tree.column("职称", width=150, anchor='center')
        self.tree.column("薪水", width=150, anchor='center')

        # 调用方法获取表格内容插入
        self.tree.grid(row=0, column=0, sticky=tk.NSEW)
        self.vbar.grid(row=0, column=1, sticky=tk.NS)
        self.hbar.grid(row=1, column=0, sticky=tk.EW)

        self.frame_center.grid_rowconfigure(0, weight=1)
        self.frame_center.grid_columnconfigure(0, weight=1)

        self.id = []
        self.name = []
        self.title = []
        self.salary = []
        # 打开数据库连接
        db = pymysql.connect(host="localhost", user="root", password="wy1211..", database="emp_project", port=3306)
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "SELECT * FROM teacher"  # SQL 查询语句
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                self.id.append(row[0])
                self.name.append(row[1])
                self.title.append(row[2])
                self.salary.append(row[3])
        except:
            print("Error: unable to fetch data")
            messagebox.showinfo('警告！', '发生错误！')
        db.close()  # 关闭数据库连接
        # 写入数据
        for i in range(min(len(self.id), len(self.name), len(self.title), len(self.salary))):
            self.tree.insert('', i, values=(self.id[i], self.name[i], self.title[i], self.salary[i]))

        for col in self.columns:  # 绑定函数，使表头可排序
            self.tree.heading(col, text=col,
                              command=lambda _col=col: self.tree_sort_column(self.tree, _col, False))

        # 定义左上方区域
        self.top_title = Label(self.frame_left_top, text="教师信息:", font=('Verdana', 20), bg='white')
        self.top_title.grid(row=0, column=0, columnspan=2, sticky=tk.NSEW, padx=50, pady=10)

        self.var_id = StringVar()
        self.var_name = StringVar()
        self.var_title = StringVar()
        self.var_salary = StringVar()
        # 职工号
        self.right_top_id_label = Label(self.frame_left_top, text="职工号：", font=('Verdana', 15), bg='white')
        self.right_top_id_entry = Entry(self.frame_left_top, textvariable=self.var_id, font=('Verdana', 15))
        self.right_top_id_label.grid(row=1, column=0)  # 位置设置
        self.right_top_id_entry.grid(row=1, column=1)
        # 姓名
        self.right_top_name_label = Label(self.frame_left_top, text="姓名：", font=('Verdana', 15), bg='white')
        self.right_top_name_entry = Entry(self.frame_left_top, textvariable=self.var_name, font=('Verdana', 15))
        self.right_top_name_label.grid(row=2, column=0)  # 位置设置
        self.right_top_name_entry.grid(row=2, column=1)
        # 职称
        self.right_top_title_label = Label(self.frame_left_top, text="职称：", font=('Verdana', 15), bg='white')
        self.right_top_title_entry = Entry(self.frame_left_top, textvariable=self.var_title, font=('Verdana', 15))
        self.right_top_title_label.grid(row=3, column=0)  # 位置设置
        self.right_top_title_entry.grid(row=3, column=1)
        # 薪水
        self.right_top_salary_label = Label(self.frame_left_top, text="薪水：", font=('Verdana', 15), bg='white')
        self.right_top_salary_entry = Entry(self.frame_left_top, textvariable=self.var_salary, font=('Verdana', 15))
        self.right_top_salary_label.grid(row=4, column=0)  # 位置设置
        self.right_top_salary_entry.grid(row=4, column=1)

        # 定义右上方区域
        self.right_top_title = Label(self.frame_right_top, text="操作：", font=('Verdana', 20), bg='white')

        self.tree.bind('<Button-1>', self.click)  # 左键获取位置
        self.right_top_button1 = ttk.Button(self.frame_right_top, text='添加教师信息', width=20, command=self.new_row)
        self.right_top_button2 = ttk.Button(self.frame_right_top, text='更新教师信息', width=20,
                                            command=self.updata_row)
        self.right_top_button3 = ttk.Button(self.frame_right_top, text='删除教师信息', width=20, command=self.del_row)

        # 位置设置
        self.right_top_title.grid(row=0, column=0, pady=10)
        self.right_top_button1.grid(row=1, column=0, padx=20, pady=10)
        self.right_top_button2.grid(row=2, column=0, padx=20, pady=10)
        self.right_top_button3.grid(row=3, column=0, padx=20, pady=10)

        # 整体区域定位
        self.frame_left_top.grid(row=0, column=0, padx=10, pady=10, sticky=tk.NSEW)
        self.frame_right_top.grid(row=0, column=1, padx=10, pady=10, sticky=tk.NSEW)
        self.frame_center.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky=tk.NSEW)
        self.frame_bottom.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky=tk.NSEW)

        self.frame_left_top.grid_propagate(False)
        self.frame_right_top.grid_propagate(False)
        self.frame_center.grid_propagate(False)
        self.frame_bottom.grid_propagate(False)

        self.frame_left_top.tkraise()
        self.frame_right_top.tkraise()
        self.frame_center.tkraise()
        self.frame_bottom.tkraise()

        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击
        self.window.mainloop()  # 进入消息循环

    def back(self):
        AdminManage(self.window)  # 显示主窗口 销毁本窗口

    def click(self, event):
        self.col = self.tree.identify_column(event.x)  # 列
        self.row = self.tree.identify_row(event.y)  # 行

        self.row_info = self.tree.item(self.row, "values")
        self.var_id.set(self.row_info[0])
        self.var_name.set(self.row_info[1])
        self.var_title.set(self.row_info[2])
        self.var_salary.set(self.row_info[3])
        self.right_top_id_entry = Entry(self.frame_left_top, state='disabled', textvariable=self.var_id,
                                        font=('Verdana', 15))

    def tree_sort_column(self, tv, col, reverse):  # Treeview、列名、排列方式
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        l.sort(reverse=reverse)  # 排序方式
        for index, (val, k) in enumerate(l):  # 根据排序后索引移动
            tv.move(k, '', index)
        tv.heading(col, command=lambda: self.tree_sort_column(tv, col, not reverse))  # 重写标题，使之成为再点倒序的标题

    def new_row(self):
        if str(self.var_id.get()) in self.id:
            messagebox.showinfo('警告！', '职工号不能重复！')
        else:
            if self.var_id.get() != '' and self.var_name.get() != '' and self.var_salary.get() != '':
                db = pymysql.connect(host="localhost", user="root", password="wy1211..", database="emp_project",
                                     port=3306)
                cursor = db.cursor()
                sql = "INSERT INTO teacher(tea_id, tea_name, tea_title, tea_salary) VALUES (%s, %s, %s, %s)"
                try:
                    cursor.execute(sql, (self.var_id.get(), self.var_name.get(), self.var_title.get() or '无职称',
                                         int(self.var_salary.get())))
                    db.commit()
                    self.id.append(self.var_id.get())
                    self.name.append(self.var_name.get())
                    self.title.append(self.var_title.get() or '无职称')
                    self.salary.append(int(self.var_salary.get()))
                    self.tree.insert('', len(self.id) - 1, values=(
                        self.id[len(self.id) - 1], self.name[len(self.id) - 1], self.title[len(self.id) - 1],
                        self.salary[len(self.id) - 1]))
                    self.tree.update()
                    messagebox.showinfo('提示！', '插入成功！')
                except:
                    db.rollback()
                    messagebox.showinfo('警告！', '数据库连接失败！')
                db.close()
            else:
                messagebox.showinfo('警告！', '请填写必要教师数据')

    def updata_row(self):
        res = messagebox.askyesnocancel('提示：', '是否更新所填数据？')
        if res:
            if self.var_id.get() == self.row_info[0]:  # 如果所填学号与所选学号一致
                db = pymysql.connect(host="localhost", user="root", password="wy1211..", database="emp_project",
                                     port=3306)
                cursor = db.cursor()
                sql = "UPDATE teacher SET tea_name = %s, tea_title = %s, tea_salary = %s WHERE tea_id = %s"
                try:
                    cursor.execute(sql, (
                    self.var_name.get(), self.var_title.get(), int(self.var_salary.get()), self.var_id.get()))
                    db.commit()
                    messagebox.showinfo('提示！', '更新成功！')

                    id_index = self.id.index(self.row_info[0])
                    self.name[id_index] = self.var_name.get()
                    self.title[id_index] = self.var_title.get()
                    self.salary[id_index] = int(self.var_salary.get())

                    self.tree.item(self.tree.selection()[0], values=(
                        self.var_id.get(), self.var_name.get(), self.var_title.get(), self.var_salary.get()))
                except:
                    db.rollback()
                    messagebox.showinfo('警告！', '教师工资太低了！')
                db.close()
            else:
                messagebox.showinfo('警告！', '不能修改教师职工号！')

    def del_row(self):
        res = messagebox.askyesnocancel('警告！', '是否删除所选数据？')
        if res:
            db = pymysql.connect(host="localhost", user="root", password="wy1211..", database="emp_project", port=3306)
            cursor = db.cursor()
            sql1 = "BEGIN"
            sql2 = "DELETE FROM lesson WHERE lesson_id in (SELECT lesson_id FROM teach WHERE tea_id = %s)"
            sql3 = "DELETE FROM teacher WHERE tea_id = %s"
            sql4 = "COMMIT"
            try:
                cursor.execute(sql1)
                cursor.execute(sql2, (self.row_info[0],))
                cursor.execute(sql3, (self.row_info[0],))
                cursor.execute(sql4)
                db.commit()
                messagebox.showinfo('提示！', '删除成功！')

                id_index = self.id.index(self.row_info[0])
                del self.id[id_index]
                del self.name[id_index]
                del self.title[id_index]
                del self.salary[id_index]
                self.tree.delete(self.tree.selection()[0])
            except:
                db.rollback()
                messagebox.showinfo('警告！', '删除失败，数据库连接失败！')
            db.close()
class Lesson:
    def __init__(self, parent_window):
        parent_window.destroy()  # 销毁主界面
        self.window = tk.Tk()  # 初始框的声明
        self.window.title('课程信息')
        center_window(self.window, 750, 600)  # 设置窗口在屏幕中央

        # 设置背景图片
        self.bg_image = Image.open("background2.jpg")
        self.bg_image = self.bg_image.resize((750, 600), Image.Resampling.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        self.bg_label = tk.Label(self.window, image=self.bg_photo)
        self.bg_label.place(relwidth=1, relheight=1)

        # 定义框架
        self.frame_left_top = tk.Frame(self.window, bg='white', width=300, height=200)
        self.frame_right_top = tk.Frame(self.window, bg='white', width=200, height=200)
        self.frame_center = tk.Frame(self.window, bg='white', width=500, height=400)
        self.frame_bottom = tk.Frame(self.window, bg='white', width=750, height=50)

        # 定义下方中心列表区域
        self.columns = ("课程代码", "课程名称", "学分", "课时")
        self.tree = ttk.Treeview(self.frame_center, show="headings", height=18, columns=self.columns)
        self.vbar = ttk.Scrollbar(self.frame_center, orient=tk.VERTICAL, command=self.tree.yview)
        self.hbar = ttk.Scrollbar(self.frame_center, orient=tk.HORIZONTAL, command=self.tree.xview)
        self.tree.configure(yscrollcommand=self.vbar.set, xscrollcommand=self.hbar.set)

        # 表格的标题
        self.tree.column("课程代码", width=150, anchor='center')  # 表示列,不显示
        self.tree.column("课程名称", width=150, anchor='center')
        self.tree.column("学分", width=100, anchor='center')
        self.tree.column("课时", width=100, anchor='center')

        # 调用方法获取表格内容插入
        self.tree.grid(row=0, column=0, sticky=tk.NSEW)
        self.vbar.grid(row=0, column=1, sticky=tk.NS)
        self.hbar.grid(row=1, column=0, sticky=tk.EW)

        self.frame_center.grid_rowconfigure(0, weight=1)
        self.frame_center.grid_columnconfigure(0, weight=1)

        self.id = []
        self.name = []
        self.cre = []
        self.hour = []
        # 打开数据库连接
        db = pymysql.connect(host="localhost", user="root", password="wy1211..", database="emp_project", port=3306)
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "SELECT * FROM lesson"  # SQL 查询语句
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                self.id.append(row[0])
                self.name.append(row[1])
                self.cre.append(row[2])
                self.hour.append(row[3])
        except:
            print("Error: unable to fetch data")
            messagebox.showinfo('警告！', '数据库连接失败！')
        db.close()  # 关闭数据库连接

        # 写入数据
        for i in range(min(len(self.id), len(self.name), len(self.cre), len(self.hour))):
            self.tree.insert('', i, values=(self.id[i], self.name[i], self.cre[i], self.hour[i]))

        for col in self.columns:  # 绑定函数，使表头可排序
            self.tree.heading(col, text=col,
                              command=lambda _col=col: self.tree_sort_column(self.tree, _col, False))

        # 定义左上方区域
        self.top_title = Label(self.frame_left_top, text="课程信息:", font=('Verdana', 20), bg='white')
        self.top_title.grid(row=0, column=0, columnspan=2, sticky=tk.NSEW, padx=50, pady=10)

        self.var_id = StringVar()  # 声明课号
        self.var_name = StringVar()  # 声明姓名
        self.var_cre = StringVar()  # 声明学分
        self.var_hour = StringVar()  # 声明课时
        # 课程代码
        self.right_top_id_label = Label(self.frame_left_top, text="课程代码：", font=('Verdana', 15), bg='white')
        self.right_top_id_entry = Entry(self.frame_left_top, textvariable=self.var_id, font=('Verdana', 15))
        self.right_top_id_label.grid(row=1, column=0)  # 位置设置
        self.right_top_id_entry.grid(row=1, column=1)
        # 课程名称
        self.right_top_name_label = Label(self.frame_left_top, text="课程名称：", font=('Verdana', 15), bg='white')
        self.right_top_name_entry = Entry(self.frame_left_top, textvariable=self.var_name, font=('Verdana', 15))
        self.right_top_name_label.grid(row=2, column=0)  # 位置设置
        self.right_top_name_entry.grid(row=2, column=1)
        # 学分
        self.right_top_gender_label = Label(self.frame_left_top, text="学分：", font=('Verdana', 15), bg='white')
        self.right_top_gender_entry = Entry(self.frame_left_top, textvariable=self.var_cre, font=('Verdana', 15))
        self.right_top_gender_label.grid(row=3, column=0)  # 位置设置
        self.right_top_gender_entry.grid(row=3, column=1)
        # 课时
        self.right_top_gender_label = Label(self.frame_left_top, text="课时：", font=('Verdana', 15), bg='white')
        self.right_top_gender_entry = Entry(self.frame_left_top, textvariable=self.var_hour, font=('Verdana', 15))
        self.right_top_gender_label.grid(row=4, column=0)  # 位置设置
        self.right_top_gender_entry.grid(row=4, column=1)

        # 定义右上方区域
        self.right_top_title = Label(self.frame_right_top, text="操作：", font=('Verdana', 20), bg='white')

        self.tree.bind('<Button-1>', self.click)  # 左键获取位置
        self.right_top_button1 = ttk.Button(self.frame_right_top, text='新建课程信息', width=20, command=self.new_row)
        self.right_top_button2 = ttk.Button(self.frame_right_top, text='更新课程信息', width=20, command=self.updata_row)
        self.right_top_button3 = ttk.Button(self.frame_right_top, text='删除课程信息', width=20, command=self.del_row)

        # 位置设置
        self.right_top_title.grid(row=0, column=0, pady=10)
        self.right_top_button1.grid(row=1, column=0, padx=20, pady=10)
        self.right_top_button2.grid(row=2, column=0, padx=20, pady=10)
        self.right_top_button3.grid(row=3, column=0, padx=20, pady=10)

        # 整体区域定位
        self.frame_left_top.grid(row=0, column=0, padx=10, pady=10, sticky=tk.NSEW)
        self.frame_right_top.grid(row=0, column=1, padx=10, pady=10, sticky=tk.NSEW)
        self.frame_center.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky=tk.NSEW)
        self.frame_bottom.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky=tk.NSEW)

        self.frame_left_top.grid_propagate(False)
        self.frame_right_top.grid_propagate(False)
        self.frame_center.grid_propagate(False)
        self.frame_bottom.grid_propagate(False)

        self.frame_left_top.tkraise()
        self.frame_right_top.tkraise()
        self.frame_center.tkraise()
        self.frame_bottom.tkraise()

        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击
        self.window.mainloop()  # 进入消息循环

    def back(self):
        AdminManage(self.window)  # 显示主窗口 销毁本窗口

    def click(self, event):
        self.col = self.tree.identify_column(event.x)  # 列
        self.row = self.tree.identify_row(event.y)  # 行

        self.row_info = self.tree.item(self.row, "values")
        self.var_id.set(self.row_info[0])
        self.var_name.set(self.row_info[1])
        self.var_cre.set(self.row_info[2])
        self.var_hour.set(self.row_info[3])
        self.right_top_id_entry = Entry(self.frame_left_top, state='disabled', textvariable=self.var_id, font=('Verdana', 15))

    def tree_sort_column(self, tv, col, reverse):  # Treeview、列名、排列方式
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        l.sort(reverse=reverse)  # 排序方式
        # rearrange items in sorted positions
        for index, (val, k) in enumerate(l):  # 根据排序后索引移动
            tv.move(k, '', index)
        tv.heading(col, command=lambda: self.tree_sort_column(tv, col, not reverse))  # 重写标题，使之成为再点倒序的标题

    def new_row(self):
        if str(self.var_id.get()) in self.id:
            messagebox.showinfo('警告！', '该课号已被占用！')
        else:
            if self.var_id.get() != '' and self.var_name.get() != '' and self.var_cre.get() != '':
                db = pymysql.connect(host="localhost", user="root", password="wy1211..", database="emp_project", port=3306)
                cursor = db.cursor()
                sql = "INSERT INTO lesson(lesson_id, lesson_name, credit, class_hour) VALUES (%s, %s, %s, %s)"
                try:
                    cursor.execute(sql, (self.var_id.get(), self.var_name.get(), self.var_cre.get(), self.var_hour.get() or '尚未设置学时'))
                    db.commit()
                    self.id.append(self.var_id.get())
                    self.name.append(self.var_name.get())
                    self.cre.append(self.var_cre.get())
                    self.hour.append(self.var_hour.get() or '尚未设置学时')
                    self.tree.insert('', len(self.id) - 1, values=(
                        self.id[len(self.id) - 1], self.name[len(self.id) - 1], self.cre[len(self.id) - 1], self.hour[len(self.id) - 1]))
                    self.tree.update()
                    messagebox.showinfo('提示！', '插入成功！')
                except:
                    db.rollback()
                    messagebox.showinfo('警告！', '插入失败，数据库连接失败！')
                db.close()
            else:
                messagebox.showinfo('警告！', '请填写必要课程信息')

    def updata_row(self):
        res = messagebox.askyesnocancel('警告！', '是否更新所填数据？')
        if res:
            if self.var_id.get() == self.row_info[0]:
                db = pymysql.connect(host="localhost", user="root", password="wy1211..", database="emp_project", port=3306)
                cursor = db.cursor()
                sql = "UPDATE lesson SET lesson_name = %s, credit = %s, class_hour = %s WHERE lesson_id = %s"
                try:
                    cursor.execute(sql, (self.var_name.get(), self.var_cre.get(), self.var_hour.get(), self.var_id.get()))
                    db.commit()
                    messagebox.showinfo('提示！', '更新成功！')
                    id_index = self.id.index(self.row_info[0])
                    self.name[id_index] = self.var_name.get()
                    self.cre[id_index] = self.var_cre.get()
                    self.hour[id_index] = self.var_hour.get()
                    self.tree.item(self.tree.selection()[0], values=(
                        self.var_id.get(), self.var_name.get(), self.var_cre.get(), self.var_hour.get()))
                except:
                    db.rollback()
                    messagebox.showinfo('警告！', '更新失败，数据库连接失败！')
                db.close()
            else:
                messagebox.showinfo('警告！', '不能修改课程代码！')

    def del_row(self):
        res = messagebox.askyesnocancel('警告！', '是否删除所选数据？')
        if res:
            db = pymysql.connect(host="localhost", user="root", password="wy1211..", database="emp_project", port=3306)
            cursor = db.cursor()
            sql = "DELETE FROM lesson WHERE lesson_id = %s"
            try:
                cursor.execute(sql, (self.row_info[0],))
                db.commit()
                messagebox.showinfo('提示！', '删除成功！')
                id_index = self.id.index(self.row_info[0])
                del self.id[id_index]
                del self.name[id_index]
                del self.cre[id_index]
                del self.hour[id_index]
                self.tree.delete(self.tree.selection()[0])
            except:
                db.rollback()
                messagebox.showinfo('警告！', '删除失败，数据库连接失败！')
            db.close()
# 选课信息界面
class Learn:
    def __init__(self, parent_window):
        parent_window.destroy()  # 销毁主界面

        self.window = tk.Tk()  # 初始框的声明
        self.window.title('选课信息')
        center_window(self.window, 750, 600)  # 设置窗口在屏幕中央

        self.bg_image = Image.open("background.jpg")
        self.bg_image = self.bg_image.resize((750, 600), Image.Resampling.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        self.bg_label = tk.Label(self.window, image=self.bg_photo)
        self.bg_label.place(relwidth=1, relheight=1)

        # 定义框架
        self.frame_left_top = tk.Frame(self.window, bg='white', width=300, height=200)
        self.frame_right_top = tk.Frame(self.window, bg='white', width=200, height=200)
        self.frame_center = tk.Frame(self.window, bg='white', width=500, height=400)
        self.frame_bottom = tk.Frame(self.window, bg='white', width=750, height=50)

        # 定义下方中心列表区域
        self.columns = ("学生学号", "课程代码", "教室", "成绩", "学分")
        self.tree = ttk.Treeview(self.frame_center, show="headings", height=18, columns=self.columns)
        self.vbar = ttk.Scrollbar(self.frame_center, orient=tk.VERTICAL, command=self.tree.yview)
        self.hbar = ttk.Scrollbar(self.frame_center, orient=tk.HORIZONTAL, command=self.tree.xview)
        self.tree.configure(yscrollcommand=self.vbar.set, xscrollcommand=self.hbar.set)

        # 表格的标题
        self.tree.column("学生学号", width=120, anchor='center')  # 表示列,不显示
        self.tree.column("课程代码", width=120, anchor='center')
        self.tree.column("教室", width=100, anchor='center')
        self.tree.column("成绩", width=100, anchor='center')
        self.tree.column("学分", width=80, anchor='center')

        # 调用方法获取表格内容插入
        self.tree.grid(row=0, column=0, sticky=tk.NSEW)
        self.vbar.grid(row=0, column=1, sticky=tk.NS)
        self.hbar.grid(row=1, column=0, sticky=tk.EW)

        self.frame_center.grid_rowconfigure(0, weight=1)
        self.frame_center.grid_columnconfigure(0, weight=1)

        self.id = []  # 学生学号
        self.les = []  # 课程代码
        self.cla = []  # 教室
        self.scr = []  # 成绩
        self.cre = []  # 学分
        # 打开数据库连接
        db = pymysql.connect(host="localhost", user="root", password="wy1211..", database="emp_project", port=3306)
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "SELECT learn.stu_id, learn.lesson_id, learn.class_number, learn.score, lesson.credit FROM learn JOIN lesson ON learn.lesson_id = lesson.lesson_id"  # SQL 查询语句
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                self.id.append(row[0])
                self.les.append(row[1])
                self.cla.append(row[2])
                self.scr.append(row[3])
                self.cre.append(row[4])
        except:
            print("Error: unable to fetch data")
            messagebox.showinfo('警告！', '数据库连接失败！')
        db.close()  # 关闭数据库连接

        # 写入数据
        for i in range(len(self.id)):
            self.tree.insert('', i, values=(self.id[i], self.les[i], self.cla[i], self.scr[i], self.cre[i]))

        for col in self.columns:  # 绑定函数，使表头可排序
            self.tree.heading(col, text=col,
                              command=lambda _col=col: self.tree_sort_column(self.tree, _col, False))

        # 定义顶部区域
        # 定义左上方区域
        self.top_title = Label(self.frame_left_top, text="选课信息:", font=('Verdana', 20), bg='white')
        self.top_title.grid(row=0, column=0, columnspan=2, sticky=tk.NSEW, padx=50, pady=10)

        self.var_id = StringVar()  # 声明学号
        self.var_les = StringVar()  # 声明课程代码
        self.var_cla = StringVar()  # 声明教室
        self.var_scr = StringVar()  # 声明成绩
        # 学号
        self.right_top_id_label = Label(self.frame_left_top, text="学生学号：", font=('Verdana', 15), bg='white')
        self.right_top_id_entry = Entry(self.frame_left_top, textvariable=self.var_id, font=('Verdana', 15))
        self.right_top_id_label.grid(row=1, column=0)  # 位置设置
        self.right_top_id_entry.grid(row=1, column=1)
        # 课程代码
        self.right_top_name_label = Label(self.frame_left_top, text="课程代码：", font=('Verdana', 15), bg='white')
        self.right_top_name_entry = Entry(self.frame_left_top, textvariable=self.var_les, font=('Verdana', 15))
        self.right_top_name_label.grid(row=2, column=0)  # 位置设置
        self.right_top_name_entry.grid(row=2, column=1)
        # 教室
        self.right_top_gender_label = Label(self.frame_left_top, text="教室：", font=('Verdana', 15), bg='white')
        self.right_top_gender_entry = Entry(self.frame_left_top, textvariable=self.var_cla, font=('Verdana', 15))
        self.right_top_gender_label.grid(row=3, column=0)  # 位置设置
        self.right_top_gender_entry.grid(row=3, column=1)
        # 成绩
        self.right_top_gender_label = Label(self.frame_left_top, text="成绩：", font=('Verdana', 15), bg='white')
        self.right_top_gender_entry = Entry(self.frame_left_top, textvariable=self.var_scr, font=('Verdana', 15))
        self.right_top_gender_label.grid(row=4, column=0)  # 位置设置
        self.right_top_gender_entry.grid(row=4, column=1)

        # 定义右上方区域
        self.right_top_title = Label(self.frame_right_top, text="操作：", font=('Verdana', 20), bg='white')

        self.tree.bind('<Button-1>', self.click)  # 左键获取位置
        self.right_top_button1 = ttk.Button(self.frame_right_top, text='新建选课信息', width=20, command=self.new_row)
        self.right_top_button2 = ttk.Button(self.frame_right_top, text='更新选课信息', width=20,
                                            command=self.updata_row)
        self.right_top_button3 = ttk.Button(self.frame_right_top, text='删除选课信息', width=20, command=self.del_row)

        # 位置设置
        self.right_top_title.grid(row=0, column=0, pady=10)
        self.right_top_button1.grid(row=1, column=0, padx=20, pady=10)
        self.right_top_button2.grid(row=2, column=0, padx=20, pady=10)
        self.right_top_button3.grid(row=3, column=0, padx=20, pady=10)

        # 整体区域定位
        self.frame_left_top.grid(row=0, column=0, padx=10, pady=10, sticky=tk.NSEW)
        self.frame_right_top.grid(row=0, column=1, padx=10, pady=10, sticky=tk.NSEW)
        self.frame_center.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky=tk.NSEW)
        self.frame_bottom.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky=tk.NSEW)

        self.frame_left_top.grid_propagate(False)
        self.frame_right_top.grid_propagate(False)
        self.frame_center.grid_propagate(False)
        self.frame_bottom.grid_propagate(False)

        self.frame_left_top.tkraise()
        self.frame_right_top.tkraise()
        self.frame_center.tkraise()
        self.frame_bottom.tkraise()

        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击
        self.window.mainloop()  # 进入消息循环
    def back(self):
        AdminManage(self.window)  # 显示主窗口 销毁本窗口
    def click(self, event):
        self.col = self.tree.identify_column(event.x)  # 列
        self.row = self.tree.identify_row(event.y)  # 行

        self.row_info = self.tree.item(self.row, "values")
        self.var_id.set(self.row_info[0])
        self.var_les.set(self.row_info[1])
        self.var_cla.set(self.row_info[2])
        self.var_scr.set(self.row_info[3])
        self.right_top_id_entry = Entry(self.frame_left_top, state='disabled', textvariable=self.var_id,
                                        font=('Verdana', 15))
    def tree_sort_column(self, tv, col, reverse):  # Treeview、列名、排列方式
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        l.sort(reverse=reverse)  # 排序方式
        # rearrange items in sorted positions
        for index, (val, k) in enumerate(l):  # 根据排序后索引移动
            tv.move(k, '', index)
        tv.heading(col, command=lambda: self.tree_sort_column(tv, col, not reverse))  # 重写标题，使之成为再点倒序的标题
    def new_row(self):
        stu_id = []  # 所有学生
        les_id = []  # 所有课程
        lesed_id = []  # 有人教
        stu_les=[] #学生选过的课
        db = pymysql.connect(host="localhost", user="root", password="wy1211..", database="emp_project", port=3306)
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql1 = "SELECT stu_id FROM student"
        cursor.execute(sql1)
        results = cursor.fetchall()
        for row in results:
            stu_id.append(row[0])
        sql2 = "SELECT lesson_id FROM lesson"
        cursor.execute(sql2)
        results = cursor.fetchall()
        for row in results:
            les_id.append(row[0])
        sql3 = "SELECT lesson_id FROM teach"
        cursor.execute(sql3)
        results = cursor.fetchall()
        for row in results:
            lesed_id.append(row[0])
        sql4 = ("SELECT learn.lesson_id "
                "FROM learn "
                "WHERE learn.stu_id = %s")
        cursor.execute(sql4, (self.var_id.get(),))
        results = cursor.fetchall()
        for row in results:
            stu_les.append(row[0])
        sql5 = ("SELECT lesson.credit "
                "FROM lesson "
                "WHERE lesson_id = %s")
        cursor.execute(sql5, (self.var_les.get(),))
        new_credits=cursor.fetchall()
        if self.var_id.get() == '' or self.var_les.get() == '':
            messagebox.showinfo('警告！', '请输入选课信息')
        else:
            if self.var_id.get() not in stu_id or self.var_les.get() not in les_id:
                messagebox.showinfo('警告！', '该学生或该课程不存在！')
            elif self.var_les.get() not in lesed_id:
                messagebox.showinfo('警告！', '无人开设此课程！')
            elif self.var_les.get() in stu_les:
                messagebox.showinfo('警告！', '该学生已经选过该课程！')
            else:
                db = pymysql.connect(host="localhost", user="root", password="wy1211..", database="emp_project",
                                     port=3306)
                cursor = db.cursor()  # 使用cursor()方法获取操作游标
                sql = "INSERT INTO learn(stu_id, lesson_id, score, class_number) VALUES (%s, %s, %s, %s)"
                try:
                    cursor.execute(sql, (self.var_id.get(), self.var_les.get(), self.var_scr.get(), self.var_cla.get()))
                    db.commit()
                    self.id.append(self.var_id.get())
                    self.les.append(self.var_les.get())
                    self.cla.append(self.var_cla.get())
                    self.scr.append(self.var_scr.get())
                    self.tree.insert('', len(self.id) - 1, values=(
                        self.id[len(self.id) - 1], self.les[len(self.id) - 1], self.cla[len(self.id) - 1],
                        self.scr[len(self.id) - 1], new_credits))
                    self.tree.update()
                    messagebox.showinfo('提示！', '总学分小于20，插入成功！')
                except Exception as e:
                    db.rollback()
                    messagebox.showinfo('警告！', f'总学分大于20，插入失败！{e}')
                db.close()

    def updata_row(self):
        res = messagebox.askyesnocancel('警告！', '是否更新所填数据？')
        if res:
            if self.var_id.get() == self.row_info[0]:
                db = pymysql.connect(host="localhost", user="root", password="wy1211..", database="emp_project",
                                     port=3306)
                cursor = db.cursor()
                sql5 = ("SELECT lesson.credit "
                        "FROM lesson "
                        "WHERE lesson_id = %s")
                cursor.execute(sql5, (self.var_les.get(),))
                new_credits = cursor.fetchall()
                sql = "CALL update_student_score(%s, %s, %s)"
                try:
                    cursor.execute(sql, (self.var_id.get(), self.var_les.get(), self.var_scr.get()))
                    db.commit()
                    messagebox.showinfo('提示！', '更新成功！')
                    id_index = self.id.index(self.row_info[0])
                    self.les[id_index] = self.var_les.get()
                    self.cla[id_index] = self.var_cla.get()
                    self.scr[id_index] = self.var_scr.get()
                    self.tree.item(self.tree.selection()[0], values=(
                        self.var_id.get(), self.var_les.get(), self.var_cla.get(), self.var_scr.get(),new_credits))
                except :
                    db.rollback()
                    messagebox.showinfo('警告！', f'学生成绩不能大于100！')
                db.close()
            else:
                messagebox.showinfo('警告！', '不能修改学生学号！')

    def del_row(self):
        res = messagebox.askyesnocancel('警告！', '是否删除所选数据？')
        if res:
            db = pymysql.connect(host="localhost", user="root", password="wy1211..", database="emp_project", port=3306)
            cursor = db.cursor()
            sql = "DELETE FROM learn WHERE stu_id = %s AND lesson_id = %s"
            try:
                cursor.execute(sql, (self.row_info[0], self.row_info[1]))
                db.commit()
                messagebox.showinfo('提示！', '删除成功！')
            except:
                db.rollback()
                messagebox.showinfo('警告！', '删除失败，数据库连接失败！')
            db.close()
            id_index = self.id.index(self.row_info[0])
            del self.id[id_index]
            del self.les[id_index]
            del self.cla[id_index]
            del self.scr[id_index]
            self.tree.delete(self.tree.selection()[0])
# 授信息界面
class Teach:
    def __init__(self, parent_window):
        parent_window.destroy()  # 销毁主界面

        self.window = tk.Tk()  # 初始框的声明
        self.window.title('授课信息')
        center_window(self.window, 750, 600)  # 设置窗口在屏幕中央

        self.bg_image = Image.open("background2.jpg")
        self.bg_image = self.bg_image.resize((750, 600), Image.Resampling.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        self.bg_label = tk.Label(self.window, image=self.bg_photo)
        self.bg_label.place(relwidth=1, relheight=1)

        # 定义框架
        self.frame_left_top = tk.Frame(self.window, bg='white', width=300, height=200)
        self.frame_right_top = tk.Frame(self.window, bg='white', width=200, height=200)
        self.frame_center = tk.Frame(self.window, bg='white', width=500, height=400)
        self.frame_bottom = tk.Frame(self.window, bg='white', width=750, height=50)

        # 定义下方中心列表区域
        self.columns = ("教师职工号", "课程代码", "教室", "结课方式")
        self.tree = ttk.Treeview(self.frame_center, show="headings", height=18, columns=self.columns)
        self.vbar = ttk.Scrollbar(self.frame_center, orient=tk.VERTICAL, command=self.tree.yview)
        self.hbar = ttk.Scrollbar(self.frame_center, orient=tk.HORIZONTAL, command=self.tree.xview)
        self.tree.configure(yscrollcommand=self.vbar.set, xscrollcommand=self.hbar.set)

        # 表格的标题
        self.tree.column("教师职工号", width=150, anchor='center')  # 表示列,不显示
        self.tree.column("课程代码", width=150, anchor='center')
        self.tree.column("教室", width=100, anchor='center')
        self.tree.column("结课方式", width=100, anchor='center')

        # 调用方法获取表格内容插入
        self.tree.grid(row=0, column=0, sticky=tk.NSEW)
        self.vbar.grid(row=0, column=1, sticky=tk.NS)
        self.hbar.grid(row=1, column=0, sticky=tk.EW)

        self.frame_center.grid_rowconfigure(0, weight=1)
        self.frame_center.grid_columnconfigure(0, weight=1)

        self.id = []  # 教师职工号
        self.les = []  # 课程代码
        self.cla = []  # 教室
        self.scr = []  # 结课方式
        # 打开数据库连接
        db = pymysql.connect(host="localhost", user="root", password="wy1211..", database="emp_project", port=3306)
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "SELECT * FROM teach"  # SQL 查询语句
        try:
            cursor.execute(sql)  # 执行SQL语句
            results = cursor.fetchall()
            for row in results:
                self.id.append(row[0])
                self.les.append(row[1])
                self.cla.append(row[3])
                self.scr.append(row[2])
        except:
            print("Error: unable to fetch data")
            messagebox.showinfo('警告！', '数据库连接失败！')
        db.close()  # 关闭数据库连接

        # 写入数据
        for i in range(min(len(self.id), len(self.les), len(self.cla), len(self.scr))):
            self.tree.insert('', i, values=(self.id[i], self.les[i], self.cla[i], self.scr[i]))

        for col in self.columns:  # 绑定函数，使表头可排序
            self.tree.heading(col, text=col, command=lambda _col=col: self.tree_sort_column(self.tree, _col, False))

        # 定义顶部区域
        self.top_title = Label(self.frame_left_top, text="授课信息:", font=('Verdana', 20), bg='white')
        self.top_title.grid(row=0, column=0, columnspan=2, sticky=tk.NSEW, padx=50, pady=10)

        self.var_id = StringVar()  # 声明职工号
        self.var_les = StringVar()  # 声明课程代码
        self.var_cla = StringVar()  # 声明教室
        self.var_scr = StringVar()  # 声明结课方式
        # 教师职工号
        self.right_top_id_label = Label(self.frame_left_top, text="教师职工号：", font=('Verdana', 15), bg='white')
        self.right_top_id_entry = Entry(self.frame_left_top, textvariable=self.var_id, font=('Verdana', 15))
        self.right_top_id_label.grid(row=1, column=0)
        self.right_top_id_entry.grid(row=1, column=1)
        # 课程代码
        self.right_top_name_label = Label(self.frame_left_top, text="课程代码：", font=('Verdana', 15), bg='white')
        self.right_top_name_entry = Entry(self.frame_left_top, textvariable=self.var_les, font=('Verdana', 15))
        self.right_top_name_label.grid(row=2, column=0)
        self.right_top_name_entry.grid(row=2, column=1)
        # 教室
        self.right_top_gender_label = Label(self.frame_left_top, text="教室：", font=('Verdana', 15), bg='white')
        self.right_top_gender_entry = Entry(self.frame_left_top, textvariable=self.var_cla, font=('Verdana', 15))
        self.right_top_gender_label.grid(row=3, column=0)
        self.right_top_gender_entry.grid(row=3, column=1)
        # 结课方式
        self.right_top_gender_label = Label(self.frame_left_top, text="结课方式：", font=('Verdana', 15), bg='white')
        self.right_top_gender_entry = Entry(self.frame_left_top, textvariable=self.var_scr, font=('Verdana', 15))
        self.right_top_gender_label.grid(row=4, column=0)
        self.right_top_gender_entry.grid(row=4, column=1)

        # 定义右上方区域
        self.right_top_title = Label(self.frame_right_top, text="操作：", font=('Verdana', 20), bg='white')

        self.tree.bind('<Button-1>', self.click)  # 左键获取位置
        self.right_top_button1 = ttk.Button(self.frame_right_top, text='新建授课信息', width=20, command=self.new_row)
        self.right_top_button2 = ttk.Button(self.frame_right_top, text='更新授课信息', width=20, command=self.updata_row)
        self.right_top_button3 = ttk.Button(self.frame_right_top, text='删除授课信息', width=20, command=self.del_row)

        # 位置设置
        self.right_top_title.grid(row=1, column=0, pady=10)
        self.right_top_button1.grid(row=2, column=0, padx=20, pady=10)
        self.right_top_button2.grid(row=3, column=0, padx=20, pady=10)
        self.right_top_button3.grid(row=4, column=0, padx=20, pady=10)

        # 整体区域定位
        self.frame_left_top.grid(row=0, column=0, padx=10, pady=10, sticky=tk.NSEW)
        self.frame_right_top.grid(row=0, column=1, padx=10, pady=10, sticky=tk.NSEW)
        self.frame_center.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky=tk.NSEW)
        self.frame_bottom.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky=tk.NSEW)

        self.frame_left_top.grid_propagate(False)
        self.frame_right_top.grid_propagate(False)
        self.frame_center.grid_propagate(False)
        self.frame_bottom.grid_propagate(False)

        self.frame_left_top.tkraise()
        self.frame_right_top.tkraise()
        self.frame_center.tkraise()
        self.frame_bottom.tkraise()

        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击
        self.window.mainloop()  # 进入消息循环

    def back(self):
        AdminManage(self.window)  # 显示主窗口 销毁本窗口

    def click(self, event):
        self.col = self.tree.identify_column(event.x)  # 列
        self.row = self.tree.identify_row(event.y)  # 行

        self.row_info = self.tree.item(self.row, "values")
        self.var_id.set(self.row_info[0])
        self.var_les.set(self.row_info[1])
        self.var_cla.set(self.row_info[2])
        self.var_scr.set(self.row_info[3])
        self.right_top_id_entry = Entry(self.frame_left_top, state='disabled', textvariable=self.var_id, font=('Verdana', 15))

    def tree_sort_column(self, tv, col, reverse):  # Treeview、列名、排列方式
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        l.sort(reverse=reverse)  # 排序方式
        for index, (val, k) in enumerate(l):  # 根据排序后索引移动
            tv.move(k, '', index)
        tv.heading(col, command=lambda: self.tree_sort_column(tv, col, not reverse))

    def new_row(self):
        tea_id = []
        les_id = []
        db = pymysql.connect(host="localhost", user="root", password="wy1211..", database="emp_project", port=3306)
        cursor = db.cursor()
        sql1 = "SELECT tea_id FROM teacher"
        cursor.execute(sql1)
        results = cursor.fetchall()
        for row in results:
            tea_id.append(row[0])
        sql2 = "SELECT lesson_id FROM lesson"
        cursor.execute(sql2)
        results = cursor.fetchall()
        for row in results:
            les_id.append(row[0])
        db.close()

        if self.var_id.get() == '' or self.var_les.get() == '':
            messagebox.showinfo('警告！', '请输入必要的授课信息')
        else:
            if self.var_id.get() not in tea_id or self.var_les.get() not in les_id:
                messagebox.showinfo('警告！', '该教师或该课程不存在！')
            else:
                db = pymysql.connect(host="localhost", user="root", password="wy1211..", database="emp_project", port=3306)
                cursor = db.cursor()
                sql = "INSERT INTO teach(tea_id, lesson_id, class, end_way) VALUES (%s, %s, %s, %s)"
                try:
                    cursor.execute(sql, (self.var_id.get(), self.var_les.get(), self.var_cla.get(), self.var_scr.get()))
                    db.commit()
                    self.id.append(self.var_id.get())
                    self.les.append(self.var_les.get())
                    self.cla.append(self.var_cla.get())
                    self.scr.append(self.var_scr.get())
                    self.tree.insert('', len(self.id) - 1, values=(self.id[-1], self.les[-1], self.cla[-1], self.scr[-1]))
                    self.tree.update()
                    messagebox.showinfo('提示！', '插入成功！')
                except:
                    db.rollback()
                    messagebox.showinfo('警告！', '该授课信息已存在！')
                db.close()

    def updata_row(self):
        res = messagebox.askyesnocancel('警告！', '是否更新所填数据？')
        if res:
            if self.var_id.get() == self.row_info[0]:
                db = pymysql.connect(host="localhost", user="root", password="wy1211..", database="emp_project", port=3306)
                cursor = db.cursor()
                sql = "call updata_teach(%s, %s, %s, %s, %s)"
                try:
                    cursor.execute(sql, (self.var_les.get(), self.var_scr.get(), self.var_cla.get(), self.row_info[0], self.row_info[1]))
                    cursor.execute("CALL update_learn_class();")
                    db.commit()
                    messagebox.showinfo('提示！', '更新成功！')
                    id_index = self.id.index(self.row_info[0])
                    self.les[id_index] = self.var_les.get()
                    self.cla[id_index] = self.var_cla.get()
                    self.scr[id_index] = self.var_scr.get()
                    self.tree.item(self.tree.selection()[0], values=(self.var_id.get(), self.var_les.get(), self.var_cla.get(), self.var_scr.get()))
                except:
                    db.rollback()
                    messagebox.showinfo('警告！', '该授课信息已存在！')
                db.close()
            else:
                messagebox.showinfo('警告！', '不能修改教师职工号！')

    def del_row(self):
        res = messagebox.askyesnocancel('警告！', '是否删除所选数据？')
        if res:
            db = pymysql.connect(host="localhost", user="root", password="wy1211..", database="emp_project", port=3306)
            cursor = db.cursor()
            sql = "DELETE FROM teach WHERE tea_id = %s AND lesson_id = %s"
            try:
                cursor.execute(sql, (self.row_info[0], self.row_info[1]))
                db.commit()
                messagebox.showinfo('提示！', '删除成功！')
                id_index = self.id.index(self.row_info[0])
                del self.id[id_index]
                del self.les[id_index]
                del self.cla[id_index]
                del self.scr[id_index]
                self.tree.delete(self.tree.selection()[0])
            except:
                db.rollback()
                messagebox.showinfo('警告！', '删除失败，数据库连接失败！')
            db.close()
# 学生查看信息界面
class StudentView:
    def __init__(self, parent_window, student_id):
        parent_window.destroy()  # 销毁主界面

        self.window = tk.Tk()  # 初始框的声明
        self.window.title('学生信息查看')
        center_window(self.window, 400, 600)  # 设置窗口在屏幕中央

        # 设置背景图片
        self.bg_image = Image.open("background.jpg")
        self.bg_image = self.bg_image.resize((400, 600), Image.Resampling.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        self.bg_label = tk.Label(self.window, image=self.bg_photo)
        self.bg_label.place(relwidth=1, relheight=1)

        # 默认信息
        self.id = ''
        self.name = ''
        self.gender = ''
        self.adm_time = ''
        self.college = ''

        # 打开数据库连接
        db = pymysql.connect(host="localhost", user="root", password="wy1211..", database="emp_project", port=3306)
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "SELECT * FROM student WHERE stu_id = '%s'" % (student_id)  # SQL 查询语句
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                self.id = row[0]
                self.name = row[1]
                self.gender = row[2]
                self.adm_time = str(row[3])
                self.college = row[4]
        except:
            print("Error: unable to fetch data")
            messagebox.showinfo('警告！', '数据库连接失败！')
        db.close()  # 关闭数据库连接

        # 标题
        label = tk.Label(self.window, text=f'欢迎, {self.name}', bg='skyblue', font=('Verdana', 24), width=30, height=2)
        label.pack(pady=20)

        # 信息标签
        Label(self.window, text=f'学号: {self.id}', font=('Verdana', 18), bg='white').pack(pady=5)
        Label(self.window, text=f'姓名: {self.name}', font=('Verdana', 18), bg='white').pack(pady=5)
        Label(self.window, text=f'性别: {self.gender}', font=('Verdana', 18), bg='white').pack(pady=5)
        Label(self.window, text=f'入学时间: {self.adm_time}', font=('Verdana', 18), bg='white').pack(pady=5)
        Label(self.window, text=f'学院: {self.college}', font=('Verdana', 18), bg='white').pack(pady=5)

        # 返回按钮
        Button(self.window, text="返回首页", width=15, font=tkFont.Font(size=16), command=self.back, bg='gray', fg='white').pack(pady=20)

        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击
        self.window.mainloop()  # 进入消息循环

    def back(self):
        StartPage(self.window)  # 显示主窗口 销毁本窗口
# 教师查看信息界面
class TeacherView:
    def __init__(self, parent_window, teacher_id):
        parent_window.destroy()  # 销毁主界面

        self.window = tk.Tk()  # 初始框的声明
        self.window.title('教师信息查看')
        center_window(self.window, 400, 600)  # 设置窗口在屏幕中央

        # 设置背景图片
        self.bg_image = Image.open("background.jpg")
        self.bg_image = self.bg_image.resize((400, 600), Image.Resampling.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        self.bg_label = tk.Label(self.window, image=self.bg_photo)
        self.bg_label.place(relwidth=1, relheight=1)

        # 默认信息
        self.id = ''
        self.name = ''
        self.title = ''
        self.salary = ''
        self.college = ''

        # 打开数据库连接
        db = pymysql.connect(host="localhost", user="root", password="wy1211..", database="emp_project", port=3306)
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "SELECT * FROM teacher WHERE tea_id = '%s'" % (teacher_id)  # SQL 查询语句
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                self.id = row[0]
                self.name = row[1]
                self.title = row[2]
                self.salary = str(row[3])
                self.college = row[4]
        except:
            print("Error: unable to fetch data")
            messagebox.showinfo('警告！', '数据库连接失败！')
        db.close()  # 关闭数据库连接

        # 标题
        label = tk.Label(self.window, text=f'欢迎, {self.name}', bg='skyblue', font=('Verdana', 24), width=30, height=2)
        label.pack(pady=20)

        # 信息标签
        Label(self.window, text=f'职工号: {self.id}', font=('Verdana', 18), bg='white').pack(pady=5)
        Label(self.window, text=f'姓名: {self.name}', font=('Verdana', 18), bg='white').pack(pady=5)
        Label(self.window, text=f'职称: {self.title}', font=('Verdana', 18), bg='white').pack(pady=5)
        Label(self.window, text=f'薪水: {self.salary}', font=('Verdana', 18), bg='white').pack(pady=5)
        Label(self.window, text=f'学院: {self.college}', font=('Verdana', 18), bg='white').pack(pady=5)

        # 返回按钮
        Button(self.window, text="返回首页", width=15, font=tkFont.Font(size=16), command=self.back, bg='gray', fg='white').pack(pady=20)

        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击
        self.window.mainloop()  # 进入消息循环

    def back(self):
        StartPage(self.window)  # 显示主窗口 销毁本窗口
class StudentCourseInfoView:
    def __init__(self, parent_window):
        parent_window.destroy()  # 销毁主界面
        self.window = tk.Tk()  # 初始框的声明
        self.window.title('学生课程信息查看')
        center_window(self.window, 800, 600)  # 设置窗口在屏幕中央
        # 设置背景图片
        self.bg_image = Image.open("background.jpg")
        self.bg_image = self.bg_image.resize((800, 600), Image.Resampling.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        self.bg_label = tk.Label(self.window, image=self.bg_photo)
        self.bg_label.place(relwidth=1, relheight=1)

        # 主标题
        self.title_label = tk.Label(self.window, text="学生课程信息查看", font=("Verdana", 24), bg='skyblue',
                                    fg='white')
        self.title_label.pack(pady=20)

        # 查询框和查询按钮
        self.query_frame = tk.Frame(self.window, bg='white')
        self.query_frame.pack(pady=10)

        self.query_label = tk.Label(self.query_frame, text="学号：", font=("Verdana", 14), bg='white')
        self.query_label.pack(side=tk.LEFT, padx=5)

        self.query_entry = tk.Entry(self.query_frame, font=("Verdana", 14))
        self.query_entry.pack(side=tk.LEFT, padx=5)

        self.query_button = tk.Button(self.query_frame, text="查询", font=("Verdana", 14), command=self.query_student)
        self.query_button.pack(side=tk.LEFT, padx=5)

        # 定义框架
        self.frame_center = tk.Frame(self.window, bg='white', bd=2, relief="ridge")
        self.frame_center.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

        # 定义下方中心列表区域
        self.columns = (
        "学号", "姓名", "性别", "入学日期", "学院", "课程ID", "课程名", "学分", "学时", "成绩", "班级号")
        self.tree = ttk.Treeview(self.frame_center, show="headings", columns=self.columns)

        self.tree.column("学号", width=100, anchor='center')
        self.tree.column("姓名", width=100, anchor='center')
        self.tree.column("性别", width=80, anchor='center')
        self.tree.column("入学日期", width=120, anchor='center')
        self.tree.column("学院", width=150, anchor='center')
        self.tree.column("课程ID", width=100, anchor='center')
        self.tree.column("课程名", width=150, anchor='center')
        self.tree.column("学分", width=50, anchor='center')
        self.tree.column("学时", width=50, anchor='center')
        self.tree.column("成绩", width=50, anchor='center')
        self.tree.column("班级号", width=100, anchor='center')

        for col in self.columns:
            self.tree.heading(col, text=col)

        # 添加滚动条
        self.vbar = ttk.Scrollbar(self.frame_center, orient=tk.VERTICAL, command=self.tree.yview)
        self.hbar = ttk.Scrollbar(self.frame_center, orient=tk.HORIZONTAL, command=self.tree.xview)
        self.tree.configure(yscrollcommand=self.vbar.set, xscrollcommand=self.hbar.set)

        self.tree.grid(row=0, column=0, sticky='nsew')
        self.vbar.grid(row=0, column=1, sticky='ns')
        self.hbar.grid(row=1, column=0, sticky='ew')

        self.frame_center.grid_rowconfigure(0, weight=1)
        self.frame_center.grid_columnconfigure(0, weight=1)

        # 从数据库中读取数据并插入到表格中
        self.load_data()

        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击
        self.window.mainloop()  # 进入消息循环

    def load_data(self):
        # 打开数据库连接
        db = pymysql.connect(host="localhost", user="root", password="wy1211..", database="emp_project", port=3306)
        cursor = db.cursor()
        sql = ("SELECT * "
               "FROM stu_course_info")
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                self.tree.insert('', 'end', values=row)
        except Exception as e:
            print("Error: unable to fetch data")
            messagebox.showinfo('警告！', f'数据库连接失败！\n错误信息：{e}')
        db.close()  # 关闭数据库连接

    def query_student(self):
        student_id = self.query_entry.get()
        for item in self.tree.get_children():
            self.tree.delete(item)

        db = pymysql.connect(host="localhost", user="root", password="wy1211..", database="emp_project", port=3306)
        cursor = db.cursor()
        sql = """
            SELECT 
                s.stu_id,
                s.stu_name,
                s.stu_gender,
                s.stu_adm_time,
                s.stu_college,
                le.lesson_id,
                le.lesson_name,
                le.credit,
                le.class_hour,
                l.score,
                l.class_number
            FROM 
                student s
            JOIN 
                learn l ON s.stu_id = l.stu_id
            JOIN 
                lesson le ON l.lesson_id = le.lesson_id
            WHERE 
                s.stu_id = %s;
        """
        try:
            cursor.execute(sql, (student_id,))
            results = cursor.fetchall()
            for row in results:
                self.tree.insert('', 'end', values=row)
        except Exception as e:
            print("Error: unable to fetch data")
            messagebox.showinfo('警告！', f'数据库连接失败！\n错误信息：{e}')
        db.close()  # 关闭数据库连接

    def back(self):
        AdminManage(self.window)  # 显示主窗口 销毁本窗口
class AboutPage:
    def __init__(self, parent_window):
        parent_window.destroy()  # 销毁主界面

        self.window = tk.Tk()  # 初始框的声明
        self.window.title('关于')
        center_window(self.window, 400, 600)  # 设置窗口在屏幕中央

        # 设置背景图片
        self.bg_image = Image.open("background.jpg")
        self.bg_image = self.bg_image.resize((400, 600), Image.Resampling.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        self.bg_label = tk.Label(self.window, image=self.bg_photo)
        self.bg_label.place(relwidth=1, relheight=1)

        # 主标题放在框架外部
        self.title_label = tk.Label(self.window, text="教务信息管理系统", font=("Verdana", 24), bg='skyblue', fg='white')
        self.title_label.pack(pady=20)  # 调整间距以放在框架外部

        # 信息框架
        self.info_frame = tk.Frame(self.window, bg='white', bd=2, relief="ridge")
        self.info_frame.place(relx=0.5, rely=0.5, anchor="center", width=350, height=350)

        # 姓名
        self.name_label = tk.Label(self.info_frame, text="姓名：王昱", font=("Verdana", 18), bg='white')
        self.name_label.pack(pady=10)

        # 学号
        self.id_label = tk.Label(self.info_frame, text="学号：2212046", font=("Verdana", 18), bg='white')
        self.id_label.pack(pady=10)

        # 专业
        self.major_label = tk.Label(self.info_frame, text="专业：信息安全", font=("Verdana", 18), bg='white')
        self.major_label.pack(pady=10)

        self.id_label = tk.Label(self.info_frame, text="学号：数据库工程作业", font=("Verdana", 18), bg='white')
        self.id_label.pack(pady=10)
        # 返回按钮
        self.back_button = tk.Button(self.info_frame, text="返回首页", font=("Verdana", 14), bg='gray', fg='white', bd=2, relief="groove", command=self.back)
        self.back_button.pack(pady=40)

        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击
        self.window.mainloop()  # 进入消息循环

    def back(self):
        StartPage(self.window)  # 显示主窗口 销毁本窗口

if __name__ == '__main__':
    window = tk.Tk()
    StartPage(window)


