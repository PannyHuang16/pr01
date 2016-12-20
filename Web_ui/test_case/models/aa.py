import os
import function
#定义文件目录

def new_report(test_report):
    #result_dir = "E:\\PycharmProjects\\Web_ui\\pr01\\result\\report"
    base=function.base_adr()
    print(base)
    result_dir = base + "/result/report"
    print(result_dir)
    lists = os.listdir(result_dir) #获取该目录下的所有文件、文件夹，保存为列表
    #对目录下的文件按创建的时间进行排序
    lists.sort(key=lambda fn: os.path.getmtime(result_dir + "\\" + fn))
    #lists[-1]取到的是最新生成的文件或文件夹
    print(('最新的文件是：' + lists[-1]))
    test_report = os.path.join(result_dir,lists[-1])
    print(test_report)
