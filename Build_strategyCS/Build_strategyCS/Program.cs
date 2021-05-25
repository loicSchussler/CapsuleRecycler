using System;
using System.Collections.Generic;
using System.Drawing;

namespace Build_strategyCS
{
    class Program
    {
        public static int GetDistance(Color current, Color match)
        {
            int redDifference;
            int greenDifference;
            int blueDifference;

            redDifference = current.R - match.R;
            greenDifference = current.G - match.G;
            blueDifference = current.B - match.B;

            return redDifference * redDifference + greenDifference * greenDifference + blueDifference * blueDifference;
        }

        public static int FindNearestColor(Color[] map, Color current)
        {
            int shortestDistance;
            int index;

            index = -1;
            shortestDistance = int.MaxValue;

            for (int i = 0; i < map.Length; i++)
            {
                Color match;
                int distance;

                match = map[i];
                distance = GetDistance(current, match);

                if (distance < shortestDistance)
                {
                    index = i;
                    shortestDistance = distance;
                }
            }

            return index;
        }

        static void Main(string[] args)
        {
            Bitmap img = new Bitmap(@"C:\Users\schus\OneDrive\Bureau\Projets\Projet capsules\Build_strategyCS\Build_strategyCS\biche.jpg");
            int imgWidth = img.Width;
            int imgHeight = img.Height;

            Color[,] imgColors = new Color[imgWidth,imgHeight];
            Color[] Palette = new Color[10000];

            int r = 0;
            int g = 0;
            int b = 0;

            for (int i =0; i < 10000; i++)
            {
                Random rr = new Random();
                Random rg = new Random();
                Random rb = new Random();

                r = rr.Next(0, 255);
                g = rg.Next(0, 255);
                b = rb.Next(0, 255);


                Palette[i] = Color.FromArgb(r, g, b);
            }

            for (int line = 0; line < imgHeight; line++)
            {
                for (int column = 0; column < imgWidth; column++)
                {
                    imgColors[column,line] = img.GetPixel(column,line);
                    int indexNearest = FindNearestColor(Palette, imgColors[column,line]);
                    Color color = Palette[indexNearest];
                    img.SetPixel(column,line,color);  
                }
            }

            img.Save(@"C:\Users\schus\OneDrive\Bureau\Projets\Projet capsules\Build_strategyCS\Build_strategyCS\biche1.jpg");
        }
    }
}
