using System;
using System.Collections.Generic;
using System.Drawing;
using System.IO;

namespace Build_strategyCS
{
    public class Convolution
    {
        public Color[,] PictureModelColors{get;set;}
        public int WidthPictureModel { get; set; }
        public int HeightPictureModel { get; set; }
        public int HeightConvolution { get; set; }
        public int WidthConvolution { get; set; }

        public Convolution(Color[,] _pictureModelColors,int _widthPictureModel,int _heightPictureModel,int _heightConvolution,int _widthConvolution)
        {
            PictureModelColors = _pictureModelColors;
            HeightPictureModel = _heightPictureModel;
            HeightConvolution = _heightConvolution;
            WidthConvolution = _widthConvolution;

        }

        public Color run(int leftCornerX, int leftCornerY)
        {
            
            int meanR = 0;
            int meanG = 0;
            int meanB = 0;

            int nbPixels = 0;

            int column = leftCornerX;
            while ((column < WidthPictureModel) && (column - leftCornerX < WidthConvolution))
            {
                int line = leftCornerY;
                while ((line < HeightPictureModel) && (line - leftCornerY < HeightConvolution))
                {
                    nbPixels++;
                    meanR += PictureModelColors[column, line].R;
                    meanG += PictureModelColors[column, line].G;
                    meanB += PictureModelColors[column, line].B;

                    line++;
                }
                column++;
            }
            
            return Color.FromArgb(meanR / nbPixels, meanG / nbPixels, meanB / nbPixels);
        }
    }
}
