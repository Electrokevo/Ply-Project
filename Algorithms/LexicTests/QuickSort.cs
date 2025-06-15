using System;
public class QuickSort
{
    public static void Sort(int[] arr, int low, int high)
    {
        if (low < high)
        {
            int pi = Partition(arr, low, high);

            Sort(arr, low, pi - 1);
            Sort(arr, pi + 1, high);
        }
    }

    private static int Partition(int[] arr, int low, int high)
    {
        int pivot = arr[high];
        int i = (low - 1);

        for (int j = low; j < high; j++)
        {
            if (arr[j] < pivot)
            {
                i++;
                Swap(ref arr[i], ref arr[j]);
            }
        }

        Swap(ref arr[i + 1], ref arr[high]);
        return i + 1;
    }

    private static void Swap(ref int a, ref int b)
    {
        int temp = a;
        a = b;
        b = temp;
    }

    public static void Main()
    {
        int[] arr = { 10, 80, 30, 90, 40, 50, 70 };
        int n = arr.Length;

        Sort(arr, 0, n - 1);

        foreach (int item in arr)
        {
            Console.Write(item + " ");
        }

        //test
        float f = 1.0F;
        double d = 1.0;
        decimal de = 1.0M;
    }
}
