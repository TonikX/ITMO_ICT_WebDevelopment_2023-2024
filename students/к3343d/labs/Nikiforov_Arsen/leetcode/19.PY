class Solution(object):
    def strongPasswordChecker(self, password):
        """
        :type password: str
        :rtype: int
        """
        # Инициализация переменных
        n = len(password)
        missing_type = 3 - sum((any(x.islower() for x in password), any(x.isupper() for x in password), any(x.isdigit() for x in password)))
        change = 0
        one = two = 0
        p = 2
        while p < n:
            if password[p] == password[p-1] == password[p-2]:
                length = 2
                while p < n and password[p] == password[p-1]:
                    length += 1
                    p += 1
                    
                change += length // 3
                if length % 3 == 0: one += 1
                elif length % 3 == 1: two += 1
            else:
                p += 1

        if n < 6:
            return max(missing_type, 6 - n)
        elif n <= 20:
            return max(missing_type, change)
        else:
            delete = n - 20
            change -= min(delete, one * 1) // 1
            change -= min(max(delete - one, 0), two * 2) // 2
            change -= max(delete - one - 2 * two, 0) // 3
                
            return delete + max(missing_type, change)
