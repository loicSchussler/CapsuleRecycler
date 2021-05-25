﻿using System;
using System.Collections.Generic;
using System.Drawing;
using System.IO;

namespace Build_strategyCS
{
    public static class Parser
    {
        public static string getTheNWord(int n,string line)
        {
            string comp = "";
            int countSpace = 0;
            foreach (char c in line)
            {
                if (c == ' ')
                {
                    countSpace++;
                }
                else
                {
                    if (countSpace > n)
                    {
                        return comp;
                    }
                    else if (countSpace == n)
                    {
                        comp += c;
                    }

                }
            }
            return comp;
        }

        public static List<(int,int,Color)> Parse(string filename)
        {
            List<(int, int, Color)> InfosPictures = new List<(int, int, Color)>();

            try
            {
                //Créez une instance de StreamReader pour lire à partir d'un fichier
                using (StreamReader sr = new StreamReader(filename))
                {
                    string line = sr.ReadLine();
                    string directoryPath = getTheNWord(0, line);

                    // Lire les lignes du fichier jusqu'à la fin.
    
                    while ((line = sr.ReadLine()) != null)
                    {

                        int indexOfthePictureInTheDirectory = Int32.Parse(getTheNWord(0, line));
                        int numberOfThisKindOfCaps = Int32.Parse(getTheNWord(1, line));


                        int r = Int32.Parse(getTheNWord(2, line));
                        int g = Int32.Parse(getTheNWord(3, line));
                        int b = Int32.Parse(getTheNWord(4, line));
                        Color colorOfTheCaps = new Color();
                        colorOfTheCaps = Color.FromArgb(r, g, b);

                        InfosPictures.Add((indexOfthePictureInTheDirectory, numberOfThisKindOfCaps, colorOfTheCaps));
                    }
                }

                return InfosPictures;
            }
            catch (Exception e)
            {
                Console.WriteLine("Le fichier n'a pas pu être lu.");
                Console.WriteLine(e.Message);

                return null;
            }
        }
    }
}
