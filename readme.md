# Nonin Onyx 9560BT Data Read

This repo enables you to read waveform data from Nonin Onyx 9560BT and store it to CSV file.
It also allows you to plot data in real-time.

## Environment

Environment is managed using conda:

`conda env create -f conda.yaml`

## Pre-requisite

1. You need to have device capable to establish serial over BlueTooth connection
2. You need to pair Nonin inside the OS

## Usage

To read data, run

`python read_data.py COM6 `

where COM6 is the serial port over BlueTooth

To plot i realtime

## License

Information about the project's license.
