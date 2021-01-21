# name = ['hot','dag','anny']
# name1 = "Janny"
# age = 9
# list1 = [1,2,3]
# dic1 = {'name':'jenny','gender' : 'male' }
#
# print(f"my name is {name[0]},my age is {age},my dict is {dic1['gender']}")
# print ('my name is %s ,my age is %d' %(name,age))
# print ('my list is {},dict is {}'.format(list1,dic1))
# print ('my name is {1}, my age is {1}'.format(name,age))
# print ('our name are  {}、{} and {}'.format(*name))
# print ('my name is {name}, my gender is {gender}'.format(**dic1))

# list = [11,12,11,12,12,13,14,14]
# a = set(list)
# print(a)
# b = {11,12,11,12,12,13,14,14}
# print(set(b))


#字符串去重，排序从小到大，输出adfjl
# s = "ajldjlajfdljfddd"
# s = set(s)
# s = list(s)
# print(s)
# s.sort(reverse=False)
# res = "".join(s)
# print(res)

#统计每个单词出现的次数
# from collections import Counter
# m = "kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h"
# res = Counter(m)
# print(res)


#字符串a = "not 404 found 张三 99 深圳"，每个词中间是空格，用正则过滤掉英文和数字，最终输出"张三  深圳"

a = "not 404 found 张三 99 深圳"