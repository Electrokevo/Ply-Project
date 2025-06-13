using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Algorithms;
internal class Program
{
    public static void Main()
    {
        Console.WriteLine("Algorithm 1---------------------------------------");
        int[] arr = [1, 3, 5, 7, 9, 11];
        int target = 7;
        int result = BinarySearch.Search(arr, target);
        if (result != -1)
            Console.WriteLine("Elemento encontrado en el índice " + result);
        else
        {
            Console.WriteLine("Elemento no encontrado");
        }

        Console.WriteLine("Algorithm 2---------------------------------------");
        arr = [10, 80, 30, 90, 40, 50, 70];
        int n = arr.Length;
        QuickSort.Sort(arr, 0, n - 1);
        foreach (int item in arr)
        {
            Console.Write(item + " ");
        }
    }
}
