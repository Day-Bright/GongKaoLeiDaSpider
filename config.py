filter_words = ["劳务派遣", "选调", "编外", "入围", "拟聘", "入围", "政审", "拟录用", "派遣制", "递补", "体检", "面试", "成绩", "辅助", "结果", "编制外", "非事业编制"
                ]  # 通过关键词筛选掉不用的公考信息

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "max-age=0",
    "referer": "https://www.gongkaoleida.com/",
    "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
}

province_num = {"国家": 3510, "安徽": 1117, "北京": 1, "重庆": 2460, "福建": 1255, "广东": 2129, "甘肃": 3191, "广西": 2290, "贵州": 2723, "河北": 37, "湖北": 1849,
                "黑龙江": 705, "河南": 1654, "海南": 2429, "湖南": 1979, "吉林": 627, "江苏": 878, "江西": 1359, "辽宁": 498, "内蒙古": 374, "宁夏": 3357, "青海": 3304, "四川": 2500, "山东": 1482,
                "上海": 859, "山西": 232, "陕西": 3063, "天津": 19, "西藏": 2980, "新疆": 3390, "云南": 2826, "浙江": 1004, "香港": 3508, "澳门": 3509, "台湾": 3507}

category = {"公务员": 2, "事业单位": 3, "教师": 59, "医疗": 60, "选调": 7, "遴选": 63, "选调生": 62, "三支一扶": 8, "大学生村官": 9,
            "基层工作者": 66, "银行": 67, "国企": 78, "公益性岗位": 80}

my_sender = "1520207872@qq.com"  # 发送人
my_pass = "xxxxxxx"  # 邮箱授权码
my_user = "1520207872@qq.com"  # 接受人
my_province = "浙江"  # 省份选择
my_category = ["公务员", "事业单位"]  # 考试类型选择
time_span = 2  # 发布时间距今2天

