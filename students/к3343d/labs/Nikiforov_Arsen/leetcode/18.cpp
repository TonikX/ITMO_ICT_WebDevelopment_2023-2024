// https://leetcode.com/problems/median-of-two-sorted-arrays/submissions/
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

