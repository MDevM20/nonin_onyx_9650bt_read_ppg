# Nonin Onyx 9560BT Data Read

This repo enables you to read waveform data from Nonin Onyx 9560BT and store it to CSV file.
It also allows you to plot data in real-time.

## Protocol

Nonin can send multiple data stream, they are:

<li>Data format 13 – provides easy spot-check measurements with the storage and forwarding of measurements. 
<li>Data format 8 – provides real-time oximetry measurements every second. 
<li>Data format 2 – provides real-time oximetry measurements with compressed waveform (8 bit waveform) every 1/75th of a second. 
<li>Data format 7 – provides real-time oximetry measurements with full resolution waveform (16 bit waveform) every 1/75th of a second.

For greater detail see the appropriate data format section in this document.

https://www.manua.ls/nonin-medical/onyx-ii-9560/manual?p=16

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

To plot i realtime, open new terminal and run

`python plot.py <FILE_NAME>`

where <FILE_NAME> is plotted by read_data.py

## License

MIT
