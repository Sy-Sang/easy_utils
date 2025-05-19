# Project Overview

## Module Tree

- .\abstract.py
- nonparametric\continuous\histogram.py
- nonparametric\continuous\kernel.py
- nonparametric\continuous\kernel2.py
- nonparametric\continuous\mfk\nd.py
- nonparametric\continuous\mfk\skewnd.py
- nonparametric\continuous\mfk\skewnd2.py
- nonparametric\discrete\basic.py
- parameter\abstract.py
- parameter\continuous\basic.py
- parameter\continuous\heavytail.py
- parameter\continuous\lifetime.py
- parameter\continuous\uniform.py
- parameter\continuous\kernel\gaussian.py
- tools\clip.py
- tools\convert.py
- tools\divergence.py

## Core Classes and Functions

### .\abstract.py
- class AbstractDistribution
    - method __init__()
    - method clone()
    - method __str__()
    - method __repr__()
    - method ppf()
    - method pdf()
    - method cdf()
    - method domain()
    - method curves()
    - method rvf()
    - method rvf_scalar()
    - method mean_integral()
    - method variance_integral()
    - method skewness_integral()
    - method kurtosis_integral()
    - method moment_integral()

### nonparametric\continuous\histogram.py
- function freedman_diaconis()
- class HistogramDistribution
    - method __init__()
    - method __str__()
    - method __repr__()
    - method ppf()
    - method cdf()
    - method pdf()
- class LogHistogramDistribution
    - method __init__()
    - method __str__()
    - method __repr__()
    - method ppf()
    - method pdf()
    - method cdf()

### nonparametric\continuous\kernel.py
- function silverman_bandwidth()
- class GaussianKernel
    - method pdf()
- class KernelMixDistribution
    - method __init__()
    - method __str__()
    - method __repr__()
    - method pdf()
    - method cdf()
    - method ppf_guess()
    - method ppf()
- class LogKernelMixDistribution
    - method __init__()
    - method ppf()
    - method pdf()
    - method cdf()

### nonparametric\continuous\kernel2.py
- function find_closest_divisor()
- function silverman_bandwidth()
- class KernelMixDistribution
    - method __init__()
    - method __str__()
    - method __repr__()
    - method kernel_data()
    - method pdf()
    - method cdf()
    - method ppf()

### nonparametric\continuous\mfk\nd.py
- function data_moment()
- function moment_loss()
- class KernelDistribution
    - method __init__()
    - method __str__()
    - method __repr__()
    - method pdf()
    - method cdf()
    - method ppf()
- function auto_bounds()
- function moment_fitted_kde()

### nonparametric\continuous\mfk\skewnd.py
- class SkewNormalKernel
    - method mean()
    - method variance()
    - method skewness()
    - method kurtosis()
    - method moment()
- class SkewKernelDistribution
    - method __init__()
    - method __str__()
    - method __repr__()
    - method pdf()
    - method cdf()
    - method ppf()
    - method mean()
    - method variance()
    - method skewness()
    - method moment()
- class SkewKDFitter
    - method __init__()
    - method loss()
    - method fit()

### nonparametric\continuous\mfk\skewnd2.py
- class SkewWeightKernelDistribution
    - method __init__()
    - method __str__()
    - method __repr__()
    - method pdf()
    - method cdf()
    - method ppf()
    - method mean()
    - method variance()
    - method skewness()
    - method moment()
- class SkewWeightKDFitter
    - method __init__()
    - method adj()
    - method adj_loss()
    - method fit()
- class SkewWeightKDFitter2
    - method __init__()
    - method zoom()
    - method zoom_and_adj()
    - method zoom_and_adj_loss()
    - method dof_zoom_and_adj_loss()
    - method fit()
    - method dof_fit()
- function snd_fitter()
- function dof_snd_fitter()

### nonparametric\discrete\basic.py
- function standardization()
- class DiscreteDistribution
    - method __init__()
    - method __str__()
    - method __repr__()
    - method pdf()
    - method cdf()
    - method ppf()

### parameter\abstract.py
- class DistributionParams
    - method __init__()
- class ParameterDistribution
    - method __init__()
    - method __str__()
    - method __repr__()
    - method ppf()
    - method pdf()
    - method cdf()
    - method get_param_constraints()
    - method parameter_verification()

### parameter\continuous\basic.py
- class NormalDistribution
    - method __init__()
    - method get_param_constraints()
    - method ppf()
    - method pdf()
    - method cdf()
- class LogNormalDistribution
    - method ppf()
    - method pdf()
    - method cdf()
- class ExponentialDistribution
    - method __init__()
    - method get_param_constraints()
    - method ppf()
    - method pdf()
    - method cdf()
- class SkewNormalDistribution
    - method __init__()
    - method get_param_constraints()
    - method pdf()
    - method cdf()
    - method single_ppf()
    - method ppf()

### parameter\continuous\heavytail.py
- class StudentTDistribution
    - method __init__()
    - method get_param_constraints()
    - method pdf()
    - method cdf()
    - method ppf()

### parameter\continuous\lifetime.py
- class WeibullDistribution
    - method __init__()
    - method get_param_constraints()
    - method ppf()
    - method pdf()
    - method cdf()
- class GumbelDistribution
    - method __init__()
    - method get_param_constraints()
    - method pdf()
    - method cdf()
    - method ppf()

### parameter\continuous\uniform.py
- class UniformDistribution
    - method __init__()
    - method ppf()
    - method pdf()
    - method cdf()
    - method get_param_constraints()

### parameter\continuous\kernel\gaussian.py
- class GaussianKernelMixDistribution
    - method __init__()
    - method __str__()
    - method __repr__()
    - method kernel_data()
    - method pdf()
    - method cdf()
    - method ppf()
- class GaussianKernelWeightedMixDistribution
    - method __init__()
    - method __str__()
    - method __repr__()
    - method kernel_data()
    - method pdf()
    - method cdf()
    - method ppf()

### tools\clip.py
- class ClippedHistogramDistribution
    - method __init__()
    - method __repr__()
    - method __str__()
    - method domain()
- class ClampedDistribution
    - method __init__()
    - method __repr__()
    - method __str__()
    - method domain()
    - method cdf()
    - method pdf()
    - method ppf()

### tools\convert.py
- function resample_like_standard_normal()
- function resample_like_distribution()
- function generate_correlated_sample()
- function generate_correlated_sample_matrix()

### tools\divergence.py
- function kl_divergence_continuous()
- function crps()
- function quantile_RMSE()
- function js_divergence_continuous()

