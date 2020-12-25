# -*- coding: utf-8 -*-
# @Time : 2020/12/25 15:36
# @Author : Seven
# @Email : sevenxiaolu@163.com
'''
正则表达式测试

macth函数进行匹配



'''
import re

#创建测试文本
test_string = '新闻 [1]  ，也叫消息，是指通过报纸、电台、广播、电视台等媒体途径所传播信息的 [2]  一种称谓。是记录社会、传播信息、反映时代的一种文体。新闻概念有广义与狭义之分，就其广义而言，除了发表于报刊、广播、互联网、电视上的评论与专文外的常用文本都属于新闻之列，包括消息、通讯、特写、速写（有的将速写纳入特写之列）等等 [3]  ，狭义的新闻则专指消息，消息是用概括的叙述方式，以较简明扼要的文字，迅速及时地报道国内外新近发生的、有价值的事实，让别人了解。每则新闻一般包括标题、导语、主体、背景和结语五部分。前三者是主要部分，后二者是辅助部分。写法上主要是叙述，有时兼有议论、描写、评论等。新闻是包含海量资讯的新闻服务平台，真实反映每时每刻的重要事件。可以通过查看新闻事件、热点话题、人物动态、产品资讯等,快速了解它们的最新进展。'


#进行简单匹配
def matching_one():
    #匹配算子
    regex = '新闻'
    p_string = test_string.split('。')
    for line in p_string:
        if re.search(regex,line) is not  None:
            print("简单匹配过后结果"+line)

'''
.   用于进行单个字符进行匹配
^+Sting   用于进行以某字符开头进行匹配
$_Sting   用于进行以某字符结尾进行匹配
'''
def matching_two():
    regex = '^新闻'
    p_string = test_string.split('。')
    for line in p_string:
        if re.search(regex,line) is not None:
            print("匹配新闻开头段落"+line)

if __name__ == '__main__':
    matching_one()
    print("----------------------------------------------------------------------------")
    matching_two()



















































