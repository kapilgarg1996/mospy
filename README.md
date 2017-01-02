# mospy
A simple python application to create a mosaic using any set of pictures.

# Installation

**`pip install mospy`**

# Usage

1. ### Command Line Interface
  * **mospy "number of grids" "image dataset directory path" "image path"**
    * number of grids : Number of pieces in mosaic
    * image dataset directory path : the folder path which contains the images using which the mosaic is to be formed
    * image path : the image path whose mosaic is to be formed
    * eg. `mospy 32 ./pictures ./pictures/my.jpg`

  * ![Mosaic](https://drive.google.com/open?id=0B8VOyX5ZTJ31N0dvamJ4VUtmV1k)

  * ![Original Image](https://drive.google.com/open?id=0B8VOyX5ZTJ31MmRFOHpVNDlPX2M)

2. ### Graphical Interface
  * **mospy-app**

  * ![GUI Mospy](https://drive.google.com/open?id=0B8VOyX5ZTJ31TFYxOXJxa0xBd3c)

# Project Setup for development

1. (optional but recommended)create a virtualenv directory and activate the virtual environment.

  ```
  virtualenv environment
  cd environment
  source bin/activate
  ```
2. Clone the project
  * `git clone https://github.com/kapilgarg1996/mospy.git`
3. install application and dependencies
  * `pip install -e mospy`
4. install tkinter
  * `sudo apt-get install python-tk`
5. Test run the GUI application
  * `mospy-app`

# File Bugs

You can report any bug [here](https://github.com/kapilgarg1996/mospy/issues)