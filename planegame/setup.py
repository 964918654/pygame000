from cx_Freeze import setup, Executable

# win32的界面
base = 'Win32GUI'    
# base = None    

# 设置打包的信息 "main.py" 打包的主文件名 base 打包的环境
executables = [Executable("mian.py", base=base)]

# 要一起打包的包，一般不用指定，会自动搜索，如果有没有匹配到的则需要指定
packages = []
# 需要一起打包的资源文件
files = ['images']
# 打包的设置
options = {
    'build_exe': {    
        'packages':packages, # 依赖的包
        'include_files':files #依赖的资源
    },    
}

# 执行打包程序
setup(
    name = "feiji", #项目名
    options = options, # 配置信息
    version = "1.0", # 项目的版本
    description = '打包测试，外星人入侵', #项目的描述
    executables = executables #主文件环境信息
)