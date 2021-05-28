using System;
using System.Collections.Generic;
using System.Drawing;
using System.IO;

namespace Build_strategyCS
{
    class PictureAnalyser
    {
        public Bitmap PictureModel { get; set; }
        public int HeightSupport { get; set; }
        public int WidthSupport { get; set; }
        public Color[,] PictureModelColors { get; set; }
        public List<Color> Palette { get; set; }
        public List<(Color,int)> CapsulesDisponibles { get; set; } 
        public int NbCapsules { get; set; }
        public List<(int,int,Color)> Strategy { get; set; }

        public PictureAnalyser(Bitmap _pictureModel,int _heightSupport,int _widthSupport)
        {
            PictureModel = _pictureModel;
            HeightSupport = _heightSupport;
            WidthSupport = _widthSupport;
            PictureModelColors = new Color[PictureModel.Width, PictureModel.Height];

            initPaletteAndCapsulesDisponibles();

        }

        public void initPaletteAndCapsulesDisponibles()
        {
            foreach (var couple in CapsulesDisponibles){
                NbCapsules += couple.Item2;
            }

        }
        

        public void initPictureModelColors()
        {
            for (int line = 0; line < PictureModel.Height; line++)
            {
                for (int column = 0; column < PictureModel.Width; column++)
                {
                    int indexNearest = ColorTools.FindNearestColor(Palette, PictureModel.GetPixel(column, line));
                    PictureModelColors[column, line] = Palette[indexNearest];
                }
            }
        }

        public void main()
        {


            Convolution convolutionMatrix = new Convolution(PictureModelColors, PictureModel.Width, PictureModel.Height, PictureModel.Width / NbCapsules, PictureModel.Height / NbCapsules);

            initPictureModelColors();

            int line = 0;
            int column = 0;

            while (line < PictureModel.Height)
            {
                while (column < PictureModel.Width)
                {
                    Color colorZone = convolutionMatrix.run(column, line);
                    Strategy.Add((column, line, colorZone));

                    column += PictureModel.Width / NbCapsules;
                }
                line += PictureModel.Height / NbCapsules;
            }

        }

    }
}
