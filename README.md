# IST-Telecom-Lab2 2022/2023 | [LAB 2 - BPSK & QPSK systems](LAB_2_2022.pdf)

## Objective
The objective of this project is to analyze a Binary Phase Shift Keying (BPSK) system and design a Quadrature Phase Shift Keying (QPSK) demodulator with symbol synchronization using the GNU Radio platform.

## Overview
Binary Phase Shift Keying (BPSK) is a digital modulation scheme where binary data is represented by changes in the phase of the carrier signal. Quadrature Phase Shift Keying (QPSK) is an extension of BPSK, where four different phase shifts are used to encode the data, allowing for higher data rates.

Design of QPSK Demodulator with Symbol Synchronization
The QPSK demodulator with symbol synchronization will involve the following main stages:

- QPSK Demodulation: Demodulate the QPSK signal to extract the symbols using GNU Radio blocks.

- Carrier Recovery: Perform carrier recovery to accurately estimate the carrier phase for symbol synchronization.

- Symbol Synchronization: Synchronize the received symbols to the symbol clock.

- Data Decoding: Decode the synchronized symbols back into binary data.

## Project Implementation
The project will include the following steps:

- Analysis of BPSK System: Analyze the BPSK system to understand the principles of phase shift keying modulation.

- GNU Radio Implementation: Design and construct the QPSK demodulator using the GNU Radio platform. Utilize appropriate GNU Radio blocks for QPSK demodulation, carrier recovery, and symbol synchronization.

- Performance Evaluation: Evaluate the performance of the QPSK demodulator by measuring parameters such as bit error rate (BER) and constellation diagram.
