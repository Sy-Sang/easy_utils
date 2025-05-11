# Project Overview

## Module Tree

- spot\trader.py
- spot\forecast\market.py
- spot\forecast\yieldindex.py
- spot\forecast\plan_a\constructor.py
- spot\forecast\plan_a\constructor2.py
- spot\forecast\plan_a\simulator.py
- spot\forecast\plan_a\simulator2.py
- spot\forecast\plan_a\transformer.py
- spot\market\recycle.py
- spot\nb\simulator_test.py
- spot\resource\namedtuple.py

## Core Classes and Functions

### spot\trader.py
- class Station
    - method __init__()
    - method trade()

### spot\forecast\market.py
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
    - method curve_matrix()

### spot\forecast\yieldindex.py
- function difference_quantile()
- function zero_quantile()

### spot\forecast\plan_a\constructor.py
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

### spot\forecast\plan_a\constructor2.py
- class KLDivergenceConstructor
    - method __init__()

### spot\forecast\plan_a\simulator.py
- function matched_gaussian_kernel_distribution_builder()
- class MarketSimulator
    - method __init__()
    - method refresh()
    - method replicate_noice_bandwidth_refresh()
    - method observe()
    - method observed_crps()
    - method random()
    - method optimize()
    - method predicted_market_trade()
    - method real_market_trade()
    - method alpha()
    - method alpha_quantile()
- function run_once()

### spot\forecast\plan_a\simulator2.py
- class WeightGaussianMarketSimulator
    - method __init__()
    - method refresh()
    - method historical_observe()
- function run_once()

### spot\forecast\plan_a\transformer.py
- class MarketSampleDataset
    - method __init__()
    - method __len__()
    - method __getitem__()
- class MarketSampleTransformer
    - method __init__()
    - method forward()
- class TabTransformer
    - method __init__()
    - method forward()

### spot\market\recycle.py
- class Recycle
    - method __call__()
- class BasicRecycle
    - method __init__()
    - method __call__()
- class PointwiseRecycle
    - method penalty_q()
    - method __call__()

### spot\nb\simulator_test.py
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

### spot\resource\namedtuple.py

