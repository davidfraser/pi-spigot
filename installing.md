# Installing this project

To install the code used to run this project

* Get Python 3.8 from [python.org](https://www.python.org) and install it
* Get the source code of this project and checkout this branch (`pi-day-2020`) from github
* (Preferably) [Create a new virtualenv](https://docs.python.org/3/library/venv.html) for the packages you will set up:
  - `python3 -m venv ../bytesofpi` 
  - Activating this with `..\bytesofpi\activate.bat`, or `. ../bytesofpi/activate.sh`.
* Installing requirements: `pip install -r requirements.txt`
* Get nodejs 12.16 or later from [nodejs.org](https://nodejs.org/), and install it. Make sure it's on your path
* Make sure you have a version of Latex [as required by matplotlib](https://matplotlib.org/3.1.1/tutorials/text/usetex.html).
  - This can be a basic (minimal + Latex) installation of TexLive that also has the `type1cm`, `cm-super` and `dvipng` packages installed
* Run Jupyter lab with `jupyter lab` (see the [instructions](https://jupyterlab.readthedocs.io/en/stable/getting_started/starting.html))
* Go to your browser and find the `talk-notes.ipynb` notebook, and open that