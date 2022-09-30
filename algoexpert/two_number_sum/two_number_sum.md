# Two number sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

## Example 1

<pre>
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
</pre>

## Example 2
<pre>
Input: nums = [3,2,4], target = 6
Output: [1,2]
</pre>

## Example 3

<pre>
Input: nums = [3,3], target = 6
Output: [0,1]
</pre>

## Constraints
<pre>
<ul>
<li> 2 <= nums.length <= 104</li>
<li> -109 <= nums[i] <= 109 </li>
<li> -109 <= target <= 109 </li>
<li> Only one valid answer exists.</li>
</ul>
</pre>

**Follow-up:** Can you come up with an algorithm that is less than O(n^2) time complexity?
