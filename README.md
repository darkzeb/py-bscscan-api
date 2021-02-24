# py-bscscan-api module

BSCscan.com API python bindings 

Restarted from the famous https://github.com/corpetty/py-etherscan-api by [Corey Petty](https://github.com/corpetty)

## Description

This module is written as an effort to provide python bindings to the BSCscan.com API, which can be found at:
https://bscscan.com/apis.

In order to use this, you must attain an BSCscan user account, and generate an API key.

In order to use the API, you must provide an API key at runtime, which can be found at the bscscan.com API website.
If you'd like to use the provided examples without altering them, then the JSON file `api_key.json` must be stored in
the base directory. Its format is as follows:

    { "key" : "YourApiKeyToken" }

with `YourApiKeyToken` is your provided API key token from BSCscan.com

## Installation

To install the package to your computer, simply run the following command in the base directory:

    python3 -m pip install py-bscscan-api

## Available bindings

Currently, only the following bscscan.com API modules are available:

- accounts
- contracts
- tokens
- stats

The remaining available modules provided by bscscan.com will be added eventually...

## Available Networks

Currently, this works for the following networks:

- Mainnet

## Examples

All possible calls have an associated example file in the examples folder to show how to call the binding

## TODO:

- 

## A votre bon coeur

BSC: 0x1326Eb599D470f92C661c8D9172e8b1B3e944c7c

