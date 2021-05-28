using System;
using System.Collections.Generic;
using System.Drawing;
using System.IO;
using Build_strategyCS;

namespace Build_strategyCS
{
    class Program
    {

        static void Main(string[] args)
        {

            List<(int, int, Color)> InfosPictures = Parser.Parse(@"C:\Users\schus\OneDrive\Bureau\Projets\CapsuleRecycler\Build_strategyCS\Build_strategyCS\test.txt");
         
            Bitmap img = new Bitmap(@"C:\Users\schus\OneDrive\Bureau\Projets\Projet capsules\Build_strategyCS\Build_strategyCS\biche.jpg");
            


            img.Save(@"C:\Users\schus\OneDrive\Bureau\Projets\Projet capsules\Build_strategyCS\Build_strategyCS\biche1.jpg");
        }
    }
}
