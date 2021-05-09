using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;

namespace Rextester
{
    public class Program
    {
        public static void Main(string[] args)
        {
            double sum = 0;
            int count = 2;
            while(count < 2000000){
                if(isPrime(count))
                    sum += count;
                count++;
            }
            
            Console.WriteLine(sum);
            
        }
        
        // if p divisor of n => p<=Vn
        static bool isPrime(int a){
            for(int i = 2; i<=Math.Sqrt(a); i++) 
                if (a % i == 0) 
                    return false;
            return true;
        }
    }
}
