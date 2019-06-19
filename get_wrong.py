import json

in_file = 'PMP考前冲刺题（一）.json'
out_file = 'PMP考前冲刺题（一）错题.json'

question_list = json.loads(open(in_file, 'r', encoding="utf8").read())

wrong_list = []
for question in question_list:
    answer = question[6]
    my_answer = question[7]
    if my_answer != answer:
        wrong_list.append(question)

open(out_file, 'w', encoding='utf8').write(json.dumps(wrong_list, ensure_ascii=False, indent=2))