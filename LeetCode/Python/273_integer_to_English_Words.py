class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'
        s = str(num)
        alt = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
        nums = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
        words = ['', 'Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        amounts = ['', 'Thousand', 'Million', 'Billion']
        part = []
        n = len(s)
        res = ''
        skip = False
        nonzero_chunk = False
        for i in range(n):
            if (n - i) % 3 == 0:
                if s[i] != '0':
                    nonzero_chunk = True
                res += nums[int(s[i])]
                res += ' '
                if s[i] != '0':
                    res += 'Hundred '
            elif (n - i) % 3 == 2:
                if s[i] != '0':
                    nonzero_chunk = True
                if s[i] == '1':
                    res += alt[int(s[i + 1])]
                    res += ' '
                    skip = True
                else:
                    res += words[int(s[i])]
                    res += ' '
            else:
                if s[i] == '0' and not nonzero_chunk:
                    continue
                if not skip:    
                    res += nums[int(s[i])]
                    res += ' '
                skip = False
                res += amounts[(n - i) // 3]
                res += ' '
                nonzero_chunk = False
        return ' '.join(filter(lambda x: x != '', res.split(' ')))