import re, json, os

def extract_question(in_file, out_file):
    cc1_all_text = open(in_file, 'r', encoding='utf8').read()

    rlt = []
    for item in re.finditer(r'<div class="st_content_txt">', cc1_all_text):
        rlt.append(item.start())
        
    print(f'find {len(rlt)}')

    def has_images(question_body):
        img_s = question_body.find('<img ')
        if img_s != -1:
            return True
        else:
            return False
        

    question_list = []
    need_images = []
    for pos in rlt:
        span1 = cc1_all_text.find('<span>', pos) + 6
        span1_end = cc1_all_text.find('</span>', span1)
        question_order = cc1_all_text[span1 : span1_end]

        question_body_s = cc1_all_text.find('</em>', span1_end) + 5
        question_body_e = cc1_all_text.find('</div>', question_body_s)
        question_body = cc1_all_text[question_body_s : question_body_e].replace('\n', '').replace('\r', '').replace('<br>', '\n')
        question_body = re.sub(r'^\s+', '', question_body)

        

        last_end = question_body_e
        def find_selection():
            nonlocal last_end
            sel_s = cc1_all_text.find('<li>', last_end)
            sel_s = cc1_all_text.find('<input', sel_s)
            sel_s = cc1_all_text.find('>', sel_s) + 1
            sel_e = cc1_all_text.find('</li>', sel_s)
            sel = cc1_all_text[sel_s:sel_e].replace('\n', ' ').replace('\r', '').replace('<br>', '\n')
            sel = re.sub(r'^\s+', '', sel)
            last_end = sel_e + 4
            return sel

        a = find_selection()
        b = find_selection()
        c = find_selection()
        d = find_selection()

        answer_s = cc1_all_text.find('class="answer_right">', last_end) + 21
        answer_e = cc1_all_text.find('</span>', answer_s)
        answer = cc1_all_text[answer_s: answer_e]

        my_answer_s = cc1_all_text.find('class="answer_wrong">', answer_e) + 21
        my_answer_e = cc1_all_text.find('</span>', my_answer_s)
        my_answer = cc1_all_text[my_answer_s: my_answer_e]

        jiexi_s = cc1_all_text.find('<div class="jxxq_jx_txt">', my_answer_e) + 25
        jiexi_e = cc1_all_text.find('</div>', jiexi_s)
        jiexi = cc1_all_text[jiexi_s:jiexi_e]
        jiexi = re.sub('^\s+', '', jiexi, flags=re.M)


        question_list.append([question_order, question_body, a, b, c, d, answer, my_answer, jiexi])
        if has_images(question_body):
            need_images.append(question_order)

        print(f'{question_order} {question_body[:50]}...')


    print('write to file: ', out_file,', count: ' , len(question_list))
    print(f'need images: ' + ','.join(need_images))
    open(out_file, 'w', encoding='utf8').write(json.dumps(question_list, ensure_ascii=False, indent=2))


html_files = os.listdir('html')
json_files = list(map(lambda x:x[:-5] + '.json', html_files))

for i in range(len(html_files)):
    in_file =  'html/' + html_files[i]
    out_file = 'json/' + json_files[i]
    print('process', in_file)
    if os.path.isfile(out_file):
        print('\t', 'already exists, skip', in_file)
    else:
        extract_question(in_file, out_file)


