# _*_ coding:utf-8 _*_
import base64
import oracle_helper as helper


def main():
    with open(r'C:\Users\litao\desktop\1.jpg', 'rb') as f:
        base64_str = base64.b64encode(f.read())

    base64_s = str(base64_str, encoding='utf-8')
    print(base64_s)
    # with helper.OracleHelper() as f:
    #     r = f.execute_sql('update spider_pic_base set img_base64 = :img_base where id =  4;',
    #                       {'img_base': base64_s})


if __name__ == '__main__':
    main()
