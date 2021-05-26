# ASD and Eye Movement
Study on the correlation between ASD and eye movement.
## Setup
Setup the virtual environment and install using the dependencies in `requirements.txt`.
```sh
python3 -m virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```
## Running
Simply run the `aggregate.py` file in the `src/` folder in order to collect the data. Then, run the `results.py` file to display results. Make sure to be on the `src/` path while running the two programs. When running the `results.py` file, add any of the following cli arguments in order to generate a graph:
- tdb - Graph the scatter plot of Mean Brightness of Image and Weighted Variance of the TD Fixmaps.
- tdv - Graph the scatter plot of Variance of Brightness of Image and Weighted Variance of the TD Fixmaps.
- asdb - Graph the scatter plot of Mean Brightness of Image and Weighted Variance of the ASD Fixmaps.
- asdv - Graph the scatter plot of Variance of Brightness of Image and Weighted Variance of the ASD Fixmaps.
- td - Graph the distribution of the Weighted Variance of the TD Fixmaps.
- asd - Graph the distribution of the Weighted Variance of the ASD Fixmaps.
- combined - Graph the combined distribution of the Weighted Variance of the TD and ASD Fixmaps.
- b - Graph the combined scatter plots of Mean Brightness of Image and Weighted Variance of the TD and ASD Fixmaps.
- v - Graph the combined scatter plots of Variance of Brightness of Image and Weighted Variance of the TD and ASD Fixmaps.
