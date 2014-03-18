__author__ = 'song.yang'

# AC
class Solution:
    # @return an integer
    def atoi(self, str):
        str = str.strip()
        if not str:
            return 0

        INT_MAX = 2147483647
        INT_MIN = -2147483648
        INT_MAX_LEN = 10
        str2int_map = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}

        negtive = False

        if str.startswith('-'):
            negtive = True
            str = str[1:]
        elif str.startswith('+'):
            negtive = False
            str = str[1:]
        elif not str2int_map.has_key(str[0]):
            return 0

        result = 0; lenth = 0
        for s in str:
            if str2int_map.has_key(s) and lenth <= INT_MAX_LEN:
                result = 10*result + str2int_map.get(s)
                lenth += 1
            elif not str2int_map.has_key(s): break
            else :return INT_MAX if not negtive else INT_MIN

        if lenth == 0:
            return 0

        return min(result,INT_MAX) if not negtive else max(-result,INT_MIN)

if __name__ == '__main__':
    print Solution().atoi(' ++1')