using System;
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

        public static (string,string,(int,int),List<(int,int,Color)>) Parse(string filename)
        {
            List<(int, int, Color)> InfosPictures = new List<(int, int, Color)>();
            string directoryPath;
            string pictureModelPath;
            (int,int) dimensionsSupport;

            try
            {
                //Créez une instance de StreamReader pour lire à partir d'un fichier
                using (StreamReader sr = new StreamReader(filename))
                {
                    string line = sr.ReadLine();
                    directoryPath = getTheNWord(0, line);

                    // Lire les lignes du fichier jusqu'à la fin.

                    line = sr.ReadLine();
                    while (line[0] != 'C')
                    {

                        int indexOfthePictureInTheDirectory = Int32.Parse(getTheNWord(0, line));
                        int numberOfThisKindOfCaps = Int32.Parse(getTheNWord(1, line));


                        int r = Int32.Parse(getTheNWord(2, line));
                        int g = Int32.Parse(getTheNWord(3, line));
                        int b = Int32.Parse(getTheNWord(4, line));
                        Color colorOfTheCaps = new Color();
                        colorOfTheCaps = Color.FromArgb(r, g, b);

                        InfosPictures.Add((indexOfthePictureInTheDirectory, numberOfThisKindOfCaps, colorOfTheCaps));

                        line = sr.ReadLine();
                    }

                    pictureModelPath = line;

                    line = sr.ReadLine();
                    int heightPictureModel = Int32.Parse(getTheNWord(0, line));
                    int widthPictureModel = Int32.Parse(getTheNWord(1, line));
                    dimensionsSupport = (heightPictureModel, widthPictureModel);

                }

                return (directoryPath,pictureModelPath,dimensionsSupport,InfosPictures);
            }
            catch (Exception e)
            {
                Console.WriteLine("Le fichier n'a pas pu être lu.");
                Console.WriteLine(e.Message);

                throw new InvalidDataException();
            }
        }
    }
}
