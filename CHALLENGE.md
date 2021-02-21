# Electricity Tariff Calculator Challenge 

## Synopsis
You are tasked with building a tool to identify the cheapest electricity tariff for a number of different households.

Each household is assumed to have the same electrical appliances. Each appliance has a stated power consumption in Watts (W) and is run for a certain number of hours each month, which varies from house to house.

Each tariff specifies different unit costs per kilowatt hour (kWh) and there are different rates for daytime and night-time electricity consumption.  Additionally, each tariff has a fixed monthly standing charge, regardless of consumption. Finally, each tariff offers a percentage discount on the cost of electricity consumed per month above a specified threshold (in kWh). The discount does not apply to the standing charge.

Identify the cheapest tariff per household when discounts are considered.

## Input
Your tool should accept `input.csv` as input. It contains three datasets:

1. The power consumption for each appliance
1. The rates, charges, monthly discount threshold and percentage discount for each tariff
1. The number of daytime and night-time hours that each appliance is run in each household

## Output
Given `input.csv`, your tool should report the following cheapest tariff per household:

```
Household,Tariff,Cost (£)
Household A,Tariff 1,45.76
Household B,Tariff 3,38.96
Household C,Tariff 1,46.55
Household D,Tariff 3,43.86
```
