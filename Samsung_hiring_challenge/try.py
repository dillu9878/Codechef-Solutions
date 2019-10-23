import pandas as pd
def main():
    data = pd.read_csv('ban-eng.csv')
    print(data.head(10))
    print('*'*60)
    data1 = pd.read_csv('eng-ban.csv')
    print(data1.head(10))

if __name__ == '__main__':
    main()