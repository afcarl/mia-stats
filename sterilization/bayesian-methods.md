### Methods Blurb

A simple Bayesian estimation model was built to model the uncertainty surrounding the percentage reduction, given the data at hand. Briefly, the pre-sanitization and post-sanitization colony counts were modelled using a Poisson likelihood, with a DiscreteUniform(0, 1000) prior placed on the Poisson rate parameter. The notation is as follows:

$mu_{pre} \sim DiscreteUniform(0, 1000)$

$CFU_{pre} \sim Poisson(\mu_{pre})$

$mu_{post} \sim DiscreteUniform(0, 1000)$

$CFU_{post} \sim Poisson(\mu_{post})$

We then deterministically compute the percentage reduction $\delta_{p}$ from the estimated $\mu$ posterior distributions.

$\delta_{p} = \frac{\mu_{pre} - \mu_{post}}{\mu_{pre}} \times 100\%$

The Bayesian estimation model was implemented in PyMC3 (ver. 3.0) in the Python programming language (ver 3.5). Notebooks are available on GitHub (https://github.com/ericmjl/mia-stats/blob/master/sterilization/sterilization.ipynb) and is archived on Zenodo (DOI: http://doi.org/10.5281/zenodo.275624).
