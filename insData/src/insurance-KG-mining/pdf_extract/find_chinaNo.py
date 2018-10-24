# encoding: utf-8
# description: 用于中文序号的提取
from __future__ import print_function
import os
import re


def produce_filename(targetdir):
    targetnames = os.listdir(targetdir)
    for name in targetnames:
        if '.txt' == name[-4:]:
            print("//" * 20, name, "//" * 20)
            print(name, 'OK')
            attr_get(targetdir + "\\" + name)


def attr_get(filename):
    f = open(filename, 'r', encoding='utf-8')
    newname = "attr_get_幸福人寿﹝2014﹞疾病保险023号.txt"
    # print(newname)
    save = open(newname, 'a+', encoding='utf-8')
    s = f.read()
    # patterns = "[\u4e00-\u9fa5]+\[[\d*\]][\u4e00-\u9fa5]+"
    i = 0
    data_set = ["保险责任", "保险事故", "保险费", "保险期间", "解除合同", "保险金给付", "保险金额",
                "责任免除", "保险事故通知", "保险事故的通知", "犹豫期", "效力恢复", "宽限期", "投保范围", "续保", "缴费方式",
                "疾病身故保险金", "护理保险金", "健康护理保险金", "长寿护理保险金", "健康维护保险金",
                "观察期", "最低保证利率", "保单贷款政策", "部分领取", "等待期", "保险金额计算方式",
                "保险费率的调整", "宽限期", "退保", "自动垫交保险费", "重大疾病保险金", "身故保险金", "重大疾病的范围",
                "是否有多次给付", "重大疾病保险金给付日", "给付总额的保证", "基本保险金额的变更",
                "退保/解除合同", "首个重大疾病保险金给付日", "承保人群", "重度失能保险金", "一般失能保险金",
                "身体全残保险金", "一般失能的范围", "重度失能的范围", "保费豁免", "给付标准和保险期间的关系",
                "减保", "减保（减额交清保险）", "减额交清保险", "身故给付", "身故给付（可能以特殊退费形式）",
                "可能以特殊退费形式", "定期复查", "保单年度累计给付限额", "保单年度累计给付限额（年限额）",
                "年限额", "所有保险期间内最高给付限额", "所有保险期间内最高给付限额（最高给付金额）",
                "最高给付金额", "每日给付限额", "每日给付限额（日限额）", "日限额", "保单年度内累计最高给付日数",
                "住院及手术医疗保险金", "门诊医疗保险金", "参加社会医疗保险", "社保补偿", "是否存在提额情况",
                "保险人不同意续保下", "住院费用和门诊费用的范围", "无保险事故优惠", "保险事故通知时间", "合同终止与满期之间间隔限制",
                "合作医院", "预授权", "未及时核定补偿", "险种转换", "是否存在保额提升情况"]
    while (i < 80):
        try:
            pattern = "第(一|二|三|四|五|六|七|八|九|十|十一|十二|十三|十四|十五|十六|十七|十八|十九|二十|二十一|二十二|二十三|二十四|二十五|二十六|二十七|二十八|二十九|三十)\s*条(\n|\s)+" + str(
                data_set[i]) + "(\n|\s)+[\u4e00-\u9fa5]+\s*"
            pattern_sub = "第(一|二|三|四|五|六|七|八|九|十|十一|十二|十三|十四|十五|十六|十七|十八|十九|二十|二十一|二十二|二十三|二十四|二十五|二十六|二十七|二十八|二十九|三十)\s*条(\n|\s)+"
            match = re.search(pattern, s, re.M)
            begin = match.start()
            start = match.end()
            match1 = re.search(pattern_sub, s[start:], re.M)
            end = match1.start()
            print('ROUNDBEGIN', data_set[i], file=save)
            print(s[begin:end + start], file=save)
            print('ROUNDEND', data_set[i], file=save)
            i += 1
        except:
            i += 1
    save.close()
    f.close()


# produce_filename('D:\\KG\\jibing')
attr_get('/Users/zhaoning/Documents/project/dataMining/userIntent/insData/src/insurance-KG-mining/testdata/幸福人寿﹝2014﹞疾病保险023号.txt')
