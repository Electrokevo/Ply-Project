public class BinarySearch
{
    public static int Search(int[] array, int target)
    {
        int left = 0, right = array.Length - 1;
        while (left <= right)
        {
            int mid = left + (right - left) / 2;

            if (array[mid] == target)
                return mid;

            if (array[mid] < target)
                left = mid + 1;
            else
                right = mid - 1;
        }
        return -1;  // Elemento no encontrado
    }

    public static void Main()
    {
        int[] arr = { 1, 3, 5, 7, 9, 11 };
        int target = 7;
        int result = Search(arr, target);

        if (result != -1)
            Console.WriteLine("Elemento encontrado en el índice " + result);
        else
            Console.WriteLine("Elemento no encontrado");
    }
}
