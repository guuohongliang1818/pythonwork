# 姓名：郭宏亮
# 时间：2023/8/3 15:44
import openpyxl

list_1 = []
excel = openpyxl.load_workbook("E:/wlhy-service/vehicle_type_info.xlsx")
sheet = excel["vehicle_type_info"]
for i in sheet.values:
    if type(i[0]) is int:
        data = {}
        data["code"] = i[1]
        data["name"] = i[2]
        list_1.append(data)

print("原始长度：", len(list_1))

list_2 = []
excel1 = openpyxl.load_workbook("E:/wlhy-service/SYS_PARAMETER.xlsx")
sheet1 = excel1["SYS_PARAMETER"]
for i in sheet1.values:
    if type(i[0]) is int:
        data = {}
        data["code"] = i[1]
        data["name"] = i[2]
        list_2.append(data)

print("原始长度：", len(list_2))

list_same_code = []
list_same_name = []
i = 0
for data1 in list_1:
    for data2 in list_2:
        if data1.get("code") == data2.get("code") and data1.get("name") == data2.get("name"):
            i = i + 1
            print(i, data1, data2)
            list_same_code.append(data1.get("code"))
            list_same_name.append(data1.get("name"))

for data1 in list_1:
    if data1.get("code") in list_same_code and data1.get("name") in list_same_name:
        pass
    else:
        print("小凯多余的数据：", data1)
print("=============")
for data2 in list_2:
    if data2.get("code") in list_same_code and data2.get("name") in list_same_name:
        pass
    else:
        print("五洲多余的数据：", data2)
