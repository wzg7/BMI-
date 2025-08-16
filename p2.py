# 获取用户输入身高体重，并转化为浮点型
def calculate_bmi():
    try:
        height = float(input('请输入身高：'))
        weight = float(input('请输入体重：'))
# 数据验证，避免数据异常
    except ValueError:
        print('非法数据,请重新输入')
        return
    if height <= 0 or weight <= 0:
        print('身高或体重不能小于0')
        return
# 根据公式和输入数据计算BMI
    BMI = weight / (height**2)
# 根据得到的BMI数值进行判断是否健康
    if BMI < 18.5:
        print('体重过轻')
    elif BMI < 24:
        print('体重正常')
    elif BMI < 27:
        print('体重过重')
    else:
        print('体重过胖')
# 调用函数
calculate_bmi()
