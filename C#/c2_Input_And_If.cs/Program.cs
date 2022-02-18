
using System;

class Program {
  public static void Main (string[] args) {
    
    Console.WriteLine("Please enter your name: ");
    var name = Console.ReadLine();

    if (name.Length >= 9)
    {
        Console.WriteLine("Letters are less");
    }
    else
    {
        Console.WriteLine("Letters are More");
    }
  }
}