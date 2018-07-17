# _*_ coding:utf-8 _*_
import base64


def main():
    with open(r'C:\Users\litao\Pictures\Camera Roll\1.jpg', 'rb') as f:
        print(len(base64.b64encode(f.read())))


if __name__ == '__main__':
    main()
