# jieba分词
import jieba
import jieba.posseg as posg
import pandas as pd
import logging


def main():
    df = pd.read_excel('F:/zhusu.xlsx', index_col=None)
    # for ind in df.index:
    # print(df['主诉'][ind])

    res = map(segment, list(df.主诉))
    res_pro = map(pro_seg, list(df.主诉))

    df_out = pd.DataFrame({'zhusu': list(df.主诉), 'jieba': list(res), 'jieba_tag': list(res_pro)})

    df_out.to_excel('d:/zhusu_seg1.xlsx', index=False)


def segment(obj):
    lis = list(jieba.cut(obj, cut_all=False))
    return '/'.join([i for i in lis if len(i) > 1])


def pro_seg(obj):
    res = posg.cut(obj)
    dic = []
    for w, p in res:
        if w in stop_words:
            continue
        if p == 'symptom' or p == 'sign' or p == 'disease':
            dic.append({'word': w, 'property': p})
    return dic


logging.basicConfig(filename='seg.log',
                    format='%(asctime)s -%(name)s-%(levelname)s-%(module)s:%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S %p',
                    level=logging.INFO
                    )


if __name__ == '__main__':
    jieba.load_userdict('userdict.txt')
    with open('stopwords.txt', 'r', encoding='utf-8') as f:
        stop_words = f.read().split('\n')
    # main()
    result = pro_seg('乏力纳差心慌手抖')
    logging.info(result)
