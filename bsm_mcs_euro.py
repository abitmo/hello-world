#
# Monte Carlo valuation of European Call Option
# in Black-Scholes-Merton model
# bsm_mcs_euro.py
#
# LAST EDIT: 15/03/2018 01:14:37 

import numpy as np

#Parameter Values
#S0 = 100.		# initial index level
#K = 105.		#strike
#T = 1.0			# time to maturity
#r = 0.05		# riskless interest rate
#sigma = 0.2		# volatility

#I = 100000		# number of simulations

def EUCallOpt_Price_BSM_MC(S0, K, T, r, sigma, I):
	#Valuation Algorithm
	z = np.random.standard_normal(I)	# pseudo-random numbers
	ST = S0 * np.exp((r - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * z) #index values at maturity
	hT = np.maximum(ST-K, 0)	#inner values at maturity
	C0 = np.exp(-r * T) * np.sum(hT)/I	 # Monte Carlo estimator

	#Result Output
	return C0
