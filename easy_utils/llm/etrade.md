# Project Overview

## Module Tree

- etrade\spot\trader.py
- etrade\spot\forecast\market.py
- etrade\spot\forecast\yieldindex.py
- etrade\spot\forecast\plan_a\constructor.py
- etrade\spot\forecast\plan_a\constructor2.py
- etrade\spot\forecast\plan_a\simulator.py
- etrade\spot\forecast\plan_a\transformer.py
- etrade\spot\market\recycle.py
- etrade\spot\nb\simulator_test.py
- etrade\spot\resource\namedtuple.py

## Core Classes and Functions

### etrade\spot\trader.py
- class Station
    - method __init__()
    - method trade()

### etrade\spot\forecast\market.py
- class DistributiveSeries
    - method __init__()
    - method rvf()
    - method mean()
    - method correlated_rvf()
- class DistributiveMarket
    - method __init__()
    - method __repr__()
    - method plot()
    - method plot2()
    - method rvf()
    - method observe()
    - method random_sample()
    - method mean()
    - method correlated_rvf()
    - method trade()
    - method trade_with_recycle()
    - method market_trade()
    - method power_generation_optimizer()
    - method faster_power_generation_optimizer()
    - method submitted_quantity_optimizer()
    - method crps()
    - method faster_crps()
    - method price_kl_divergence()
    - method quantile_rmse_matrix()
    - method pdf_difference()
    - method ppf_difference()

### etrade\spot\forecast\yieldindex.py
- function difference_quantile()
- function zero_quantile()

### etrade\spot\forecast\plan_a\constructor.py
- class AbstractDistributionConstructor
    - method random()
- class DistributionConstructor
    - method __init__()
    - method random()
- class OrdinaryGaussianKernelDistributionConstructor
    - method __init__()
    - method random()
- class MarketConstructor
    - method __init__()
    - method random()
- function market_hybridization()
- function market_hybridization_by_weight()

### etrade\spot\forecast\plan_a\constructor2.py
- class KLDivergenceConstructor
    - method __init__()

### etrade\spot\forecast\plan_a\simulator.py
- function matched_gaussian_kernel_distribution_builder()
- class MarketSimulator
    - method __init__()
    - method refresh()
    - method replicate_noice_bandwidth_refresh()
    - method observe()
    - method observed_crps()
    - method random()
    - method optimize()
    - method optimized_trade()
    - method zero_quantile()
    - method alpha()
    - method alpha_quantile()
- class WeightGaussianMarketSimulator
    - method __init__()
    - method refresh()
- function run_once()

### etrade\spot\forecast\plan_a\transformer.py
- class MarketSampleDataset
    - method __init__()
    - method __len__()
    - method __getitem__()
- class MarketSampleTransformer
    - method __init__()
    - method forward()

### etrade\spot\market\recycle.py
- class Recycle
    - method __call__()
- class BasicRecycle
    - method __init__()
    - method __call__()
- class PointwiseRecycle
    - method penalty_q()
    - method __call__()

### etrade\spot\nb\simulator_test.py
- function matched_gaussian_kernel_distribution_builder()
- class MarketSimulator
    - method __init__()
    - method refresh()
    - method replicate_noice_bandwidth_refresh()
    - method observe()
    - method observed_crps()
    - method random()
    - method optimize()
    - method quantile()
    - method zero_quantile()

### etrade\spot\resource\namedtuple.py

