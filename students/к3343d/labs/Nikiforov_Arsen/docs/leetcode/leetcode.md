# Решения задач с LeetCode

##1.py - Сложение двух чисел: 
Программа решает задачу нахождения двух чисел в списке nums, сумма которых равна заданной целевой сумме target. Он использует хэш-таблицу num_map, чтобы отслеживать уже пройденные числа и их индексы. В цикле for он вычисляет разницу между target и текущим числом, и если такая разница (complement) уже присутствует в хэш-таблице, возвращается индекс этой разницы и текущего числа, образуя пару, сумма которой равна target. В противном случае текущее число добавляется в хэш-таблицу, и если не найдена подходящая пара, возвращается пустой список.
```python
# https://leetcode.com/problems/add-two-numbers/submissions/
class Solution:
    def twoSum(self, nums, target):
        num_map = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in num_map:
                return [num_map[complement], i]
            num_map[nums[i]] = i
        return []

```

##2.py - Самая длинная подстрока без повторяющихся символов: Находит максимальную длину подстроки в строке s, не содержащей повторяющихся символов.

```python
class Solution:
    def lengthOfLongestSubstring(self, s):
        start, maxLength = 0, 0
        charIndexMap = {}
        for i in range(len(s)):
            if s[i] in charIndexMap and charIndexMap[s[i]] >= start:
                start = charIndexMap[s[i]] + 1
            charIndexMap[s[i]] = i
            maxLength = max(maxLength, i - start + 1)
        return maxLength
```

##3.py - Самая длинная палиндромная подстрока: Определяет самую длинную палиндромную подстроку внутри входной строки s.
```python
class Solution:
    def longestPalindrome(self, s):
        def expandAroundCenter(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        if not s or len(s) < 1:
            return ""

        start, end = 0, 0
        for i in range(len(s)):
            len1 = expandAroundCenter(i, i)
            len2 = expandAroundCenter(i, i + 1)
            longer = len1 if len(len1) > len(len2) else len2
            if len(longer) > end - start:
                start, end = i - ((len(longer) - 1) // 2), i + (len(longer) // 2)

        return s[start:end + 1]

```

##4.py - Преобразование строки в 'зигзаг': Преобразует строку s в последовательность, расположенную в виде зигзага на заданном количестве строк, и читает её построчно.
```python
class Solution:
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s

        result = [''] * numRows
        index, step = 0, 1

        for char in s:
            result[index] += char

            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1

            index += step

        return ''.join(result)
```

##5.py - Реверс числа: Инвертирует целое число x, если инвертированное число не выходит за пределы диапазона 32-битного знакового целого.
```python
class Solution:
    def reverse(self, x):
        sign = [1,-1][x < 0]
        reversed_x = sign * int(str(abs(x))[::-1])

        return reversed_x if -2**31 <= reversed_x <= 2**31 - 1 else 0
```

##6.py - Преобразование строки в целое число (atoi): Конвертирует строку в 32-битное знаковое целое число, следуя правилам, подобным функции atoi в C/C++.
```python
class Solution:
    def myAtoi(self, s):
        s = s.strip()
        if not s:
            return 0

        sign, i = 1, 0
        if s[0] in ["-", "+"]:
            sign = -1 if s[0] == "-" else 1
            i = 1

        number = 0
        for j in range(i, len(s)):
            if not s[j].isdigit():
                break
            number = number * 10 + int(s[j])

        return max(-2**31, min(sign * number, 2**31 - 1))

```

##7.py - Проверка числа на палиндром: Определяет, является ли целое число x палиндромом, то есть читается одинаково в обоих направлениях.
```python
class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        reversed_x, original_x = 0, x
        while x > 0:
            reversed_x = reversed_x * 10 + x % 10
            x //= 10
        return original_x == reversed_x
```

##8.py - Сопоставление с регулярным выражением: Проверяет, соответствует ли строка s заданному шаблону p с использованием регулярных выражений.
```python
class Solution(object):
    def isMatch(self, s, p):
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[-1][-1] = True

        for i in range(len(s), -1, -1):
            for j in range(len(p) - 1, -1, -1):
                first_match = i < len(s) and p[j] in {s[i], '.'}
                if j + 1 < len(p) and p[j + 1] == '*':
                    dp[i][j] = dp[i][j + 2] or first_match and dp[i + 1][j]
                else:
                    dp[i][j] = first_match and dp[i + 1][j + 1]

        return dp[0][0]

```

##9.py - Контейнер с водой: Вычисляет максимально возможное количество воды, которое может содержаться между двумя вертикальными линиями.
```python
class Solution(object):
    def maxArea(self, height):
        left, right = 0, len(height) - 1
        max_area = 0
        while left < right:
            width = right - left
            max_area = max(max_area, min(height[left], height[right]) * width)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area

```

##10.py - Целое число в римское число: Конвертирует целое число num в римское числовое представление.
```python
class Solution(object):
    def intToRoman(self, num):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        syms = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        roman_num = ''
        i = 0
        while num > 0:
            for _ in range(num // val[i]):
                roman_num += syms[i]
                num -= val[i]
            i += 1
        return roman_num

```

##11.py - Римское число в целое: Преобразует римское числовое представление в целое число.
```python
class Solution(object):
    def romanToInt(self, s):
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        integer = 0
        for i in range(len(s)):
            if i > 0 and roman[s[i]] > roman[s[i - 1]]:
                integer += roman[s[i]] - 2 * roman[s[i - 1]]
            else:
                integer += roman[s[i]]
        return integer

```

##12.py - Самый длинный общий префикс: Находит самый длинный общий префикс среди массива строк.
```python
class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        shortest = min(strs, key=len)
        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]
        return shortest 
```

##13.py - Тройки чисел с суммой ноль: Возвращает все уникальные тройки чисел из массива nums, сумма которых равна нулю.
```python
class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        result = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return result
```

##14.py - Тройки чисел с суммой, ближайшей к заданному числу: Находит сумму трех чисел, наиболее близкую к заданному целевому числу.
```python
class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        closest = sum(nums[:3])
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                if abs(current_sum - target) < abs(closest - target):
                    closest = current_sum
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    return target
        return closest
```

##15.py - Комбинации букв телефонного номера: Генерирует все возможные комбинации букв для заданного набора цифр, как на кнопках телефона.
```python

class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
            return []

        digit_to_char = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def backtrack(index, path):
            if index == len(digits):
                combinations.append(''.join(path))
                return
            possible_letters = digit_to_char[digits[index]]
            for letter in possible_letters:
                path.append(letter)
                backtrack(index + 1, path)
                path.pop()

        combinations = []
        backtrack(0, [])
        return combinations
```

##16.py - Удаление дубликатов из отсортированного массива
Удаляет дубликаты из отсортированного массива nums, сохраняя только уникальные элементы, и возвращает их количество.
```python
class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        j = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[j]:
                j += 1
                nums[j] = nums[i]

        return j + 1

```
##17.py - Реверс узлов в группах по k
Разворачивает узлы связного списка по k элементов за раз, возвращая модифицированный список.
```python
class Solution(object):
    def reverseKGroup(self, head, k):
        # Функция для разворота связного списка
        def reverseLinkedList(head, k):
            new_head, ptr = None, head
            while k:
                next_node = ptr.next
                ptr.next = new_head
                new_head = ptr
                ptr = next_node
                k -= 1
            return new_head

        count = 0
        ptr = head
        while count < k and ptr:
            ptr = ptr.next
            count += 1

        if count == k:
            reversed_head = reverseLinkedList(head, k)
            head.next = self.reverseKGroup(ptr, k)
            return reversed_head
        return head

```

##18.cpp - Задача "Median of Two Sorted Arrays" заключается в нахождении медианы двух отсортированных массивов. 
Медиана - это такое значение, что половина элементов массива меньше его, а другая половина больше или равна ему. 
Если общее количество элементов в обоих массивах нечетное, медиана - это один элемент. 
Если четное - это среднее двух центральных элементов.

Код решает задачу, используя бинарный поиск по меньшему массиву для эффективного нахождения правильного разреза. 
Он определяет граничные элементы с каждой стороны разреза, чтобы проверить, могут ли эти элементы формировать медиану. 
Если разрез корректен, медиана вычисляется на основе этих граничных элементов в зависимости от четности общего количества элементов в обоих массивах.
```
#include <vector>
#include <climits>
using namespace std;

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        // Если nums1 больше nums2, меняем их местами для упрощения логики
        if(nums2.size() < nums1.size()) return findMedianSortedArrays(nums2, nums1);

        int n1 = nums1.size();
        int n2 = nums2.size();
        int low = 0, high = n1;

        while(low <= high) {
            // Находим середины обоих массивов
            int cut1 = (low + high) / 2;
            int cut2 = (n1 + n2 + 1) / 2 - cut1;

            // Определяем левые и правые границы разделения
            int left1 = cut1 == 0 ? INT_MIN : nums1[cut1 - 1];
            int left2 = cut2 == 0 ? INT_MIN : nums2[cut2 - 1];
            int right1 = cut1 == n1 ? INT_MAX : nums1[cut1];
            int right2 = cut2 == n2 ? INT_MAX : nums2[cut2];

            // Проверяем, корректно ли разделены массивы
            if(left1 <= right2 && left2 <= right1) {
                // Если общее количество элементов четное
                if((n1 + n2) % 2 == 0)
                    return (max(left1, left2) + min(right1, right2)) / 2.0;
                else
                    return max(left1, left2);
            }  
            else if(left1 > right2) {
                high = cut1 - 1;
            }
            else {
                low = cut1 + 1;
            }
        }
        return 0.0; // В случае ошибки
    }
};

```

#19.py - Strong Password Checker

Есть функция strongPasswordChecker, которая оценивает стойкость пароля и возвращает минимальное количество действий для усиления безопасности. Оценка включает проверку наличия строчных букв, прописных букв, цифр и повторяющихся символов. Код определяет, сколько символов нужно добавить или удалить, чтобы соответствовать заданным требованиям.
```Python
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
```

![Выполненные задания на сайте leetcode](../img/leetcode.png)

