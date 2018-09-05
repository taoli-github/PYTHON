# jieba分词
import jieba
import pandas as pd


def main():
    df = pd.read_excel('F:/zhusu.xlsx', index_col=None)
    # for ind in df.index:
    # print(df['主诉'][ind])

    res = map(segment, list(df.主诉))

    df_out = pd.DataFrame({'zhusu': list(df.主诉), 'jieba': list(res)})

    df_out.to_excel('d:/zhusu_seg1.xlsx', index=False)


def segment(obj):
    lis = list(jieba.cut(obj, cut_all=False))
    return '/'.join([i for i in lis if len(i) > 1])


if __name__ == '__main__':
    jieba.load_userdict('userdict.txt')
    main()
