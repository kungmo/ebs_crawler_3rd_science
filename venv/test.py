test_list = ['aa', 'bb', 'cc', 'dd']

page_num = 16

url = 'https://mid.ebs.co.kr/course/view?courseId=10203440#qna/list/20001283/' + str(page_num) + '///0/titleContent//N//'

print(url)

for element in test_list:
    if test_list.index(element)%2 == 0:
        print('질문: ', element)
    else:
        print('답변: ', element)