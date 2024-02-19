public int CountCombinations(int[] arr1, int[] arr2, int[] arr3, int target)
{
    var count = 0;
    var hashSet = new HashSet<int>();

    foreach (var num in arr1)
    {
        hashSet.Add(num);
    }

    foreach (var num in arr2)
    {
        if (hashSet.Contains(target - num))
        {
            count++;
        }
    }

    foreach (var num in arr3)
    {
        if (hashSet.Contains(target - num))
        {
            count++;
        }
    }

    return count;
}

int[] arr1 = new int[] { 1, 5, 90, 4, 3 };
int[] arr2 = new int[] { 3, 4, 5, 7 };
int[] arr3 = new int[] { 7, 13, 2 };
int target = 21;