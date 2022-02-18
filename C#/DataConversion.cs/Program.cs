using System;

class Program
    {

        static void Main(string[] args) {

        // float x = 77.5f; // keep f at the end to covert the same to float.
        // float y = 33.5f;
        // float z = x+y;
        //     // Console.WriteLine("Hello");
        // System.Console.WriteLine(x+y);

        // float m= 77.5f;
        // float n = 33.5f;
        // float k = x+y;
        // Console.WriteLine(k);

        // double p =12.5;// Doubel accept all float with f at the end.
        // double l= 13.5;
        // System.Console.WriteLine(p+l);

       
        // you can decalre mutlipel variable of the same type like the belwo:
        //int x=3, y=4,z=5;

        double num = 12.5;
        int num2 = Convert.ToInt32(num);// will explicityly convert, some values will be trimmed
        System.Console.WriteLine(num2);
        System.Console.WriteLine(Convert.ToString(num));

        // to see where each type belong to, use the below.
        System.Console.WriteLine(typeof(float));
        System.Console.WriteLine(typeof(string));
        System.Console.WriteLine(typeof(double));
        System.Console.WriteLine(typeof(Boolean));

        var num3 = "123";
        var num4= Convert.ToInt32(num3);
        System.Console.WriteLine(num3);







        }
            

        }

    