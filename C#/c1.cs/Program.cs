using System;

class Program
    {
        //structure
        struct student
        {
            private string name;
            private int age;
        };
        static void Main(string[] args)
        {
            char a = 'X';
            int b = 10;
            bool c = false;

            Console.WriteLine("for variable \'a\'...");
            Console.WriteLine("default: " + a.GetType());
            Console.WriteLine("Name: " + a.GetType().Name);
            Console.WriteLine("FullName: " + a.GetType().FullName);
            Console.WriteLine("Namespace: " + a.GetType().Namespace);
            Console.WriteLine();

            Console.WriteLine("for variable \'b\'...");
            Console.WriteLine("default: " + b.GetType());
            Console.WriteLine("Name: " + b.GetType().Name);
            Console.WriteLine("FullName: " + b.GetType().FullName);
            Console.WriteLine("Namespace: " + b.GetType().Namespace);
            Console.WriteLine();

            Console.WriteLine("for variable \'c\'...");
            Console.WriteLine("default: " + c.GetType());
            Console.WriteLine("Name: " + c.GetType().Name);
            Console.WriteLine("FullName: " + c.GetType().FullName);
            Console.WriteLine("Namespace: " + c.GetType().Namespace);
            Console.WriteLine();

            student std = new student();
            Console.WriteLine("for structure \'std\'...");
            Console.WriteLine("default: " + std.GetType());
            Console.WriteLine("Name: " + std.GetType().Name);
            Console.WriteLine("FullName: " + std.GetType().FullName);
            Console.WriteLine("Namespace: " + std.GetType().Namespace);
            Console.WriteLine();

            //hit ENTER to exit
            Console.ReadLine();
        }
    }