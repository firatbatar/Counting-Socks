# PROJ-201---Counting-Socks

## Description
Suppose that there is a certain amount of socks
with a constant probability of being used and washed during each 'cycle'.
When a sock is used and washed it is aged by one.

The question is what will be the distribution of the ages of socks with different parameters
(SOCK_COUNT, USAGE_PROBABILITY, MAX_CYCLE)

### Simulation
The code simulates several washing simulations with given parameters.
Then according to observed data an expected normal and uniform distributions are calculated.
Lastly, the observed data is tested against these expected distributions using *Chi-Square Goodness of Fit Test*.

### Data
The observed data is saved into *.xlsx* sheets and, along with expected distributions,
they are plotted into histograms. Lastly, the results of the Chi-Square test are saved into
*.docx* documents.


## Folder Structure
In order to work the program needs some folder to exist (this can be changed via code but God knows from where.)


```
.
├───data
└───graphs
    ├───cycle
    ├───sock_count
    └───usage_probability
```