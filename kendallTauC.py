
import numpy as np
import scipy.stats as stats
import pandas as pd

# reading excel sheets
CB = pd.read_excel('Tau.xlsx', sheet_name='CB')
AU = pd.read_excel('Tau.xlsx', sheet_name='AU')
AG110 = pd.read_excel('Tau.xlsx', sheet_name='AG110')
AG100 = pd.read_excel('Tau.xlsx', sheet_name='AG100')
AG111 = pd.read_excel('Tau.xlsx', sheet_name='AG111')
TIO2A100 = pd.read_excel('Tau.xlsx', sheet_name='TIO2A100')
TIO2A101 = pd.read_excel('Tau.xlsx', sheet_name='TIO2A101')
GRO = pd.read_excel('Tau.xlsx', sheet_name='GRO')
GR = pd.read_excel('Tau.xlsx', sheet_name='GR')
CdSe = pd.read_excel('Tau.xlsx', sheet_name='CdSe')
Fe2O = pd.read_excel('Tau.xlsx', sheet_name='Fe2O')
SIO2AM = pd.read_excel('Tau.xlsx', sheet_name='SIO2AM')
SIO2Q = pd.read_excel('Tau.xlsx', sheet_name='SIO2Q')
Tio2R100 = pd.read_excel('Tau.xlsx', sheet_name='Tio2R100')
Tio2R110 = pd.read_excel('Tau.xlsx', sheet_name='Tio2R110')


# extracting variables from CB sheet
x1 = CB['ITASSER_E']
x2 = CB['AF_E']
tau_CB, p_value1 = stats.kendalltau(x1, x2)

# extracting variables from AU
x3 = AU['ITASSER_E']
x4 = AU['AF_E']
tau_AU, p_value2 = stats.kendalltau(x3, x4)

# extracting variables from AG110
x5 = AG110['ITASSER_E']
x6 = AG110['AF_E']
tau_AG110, p_value2 = stats.kendalltau(x5, x6)

# extracting variables from AG100
x7 = AG100['ITASSER_E']
x8 = AG100['AF_E']
tau_AG100, p_value2 = stats.kendalltau(x7, x8)

# extracting variables from AG111
x9 = AG111['ITASSER_E']
x10 = AG111['AF_E']
tau_AG111, p_value2 = stats.kendalltau(x9, x10)

# extracting variables from TIO2A100
x11 = TIO2A100['ITASSER_E']
x12 = TIO2A100['AF_E']
tau_TIO2A100, p_value2 = stats.kendalltau(x11, x12)

# extracting variables from TIO2A101
x13 = TIO2A101['ITASSER_E']
x14 = TIO2A101['AF_E']
tau_TIO2A101, p_value2 = stats.kendalltau(x13, x14)

# extracting variables from GRO
x15 = GRO['ITASSER_E']
x16 = GRO['AF_E']
tau_GRO, p_value2 = stats.kendalltau(x15, x16)

# extracting variables from GR
x17 = GR['ITASSER_E']
x18 = GR['AF_E']
tau_GR, p_value2 = stats.kendalltau(x17, x18)

# extracting variables from CdSe
x19 = CdSe['ITASSER_E']
x20 = CdSe['AF_E']
tau_CdSe, p_value2 = stats.kendalltau(x19, x20)

# extracting variables from Fe2O
x21 = Fe2O['ITASSER_E']
x22 = Fe2O['AF_E']
tau_Fe2O, p_value2 = stats.kendalltau(x21, x22)

# extracting variables from SIO2AM
x23 = SIO2AM['ITASSER_E']
x24 = SIO2AM['AF_E']
tau_SIO2AM, p_value2 = stats.kendalltau(x23, x24)

# extracting variables from SIO2Q
x25 = SIO2Q['ITASSER_E']
x26 = SIO2Q['AF_E']
tau_SIO2Q, p_value2 = stats.kendalltau(x25, x26)

# extracting variables from Tio2R100
x27 = Tio2R100['ITASSER_E']
x28 = Tio2R100['AF_E']
tau_Tio2R100, p_value2 = stats.kendalltau(x27, x28)

# extracting variables from Tio2R110
x29 = Tio2R110['ITASSER_E']
x30 = Tio2R110['AF_E']
tau_Tio2R110, p_value2 = stats.kendalltau(x29, x30)

# Calculating Kendall coefficient
# Values close to 1 indicate strong agreement, and values close to -1 indicate strong disagreement
print('Kendall  CB coefficient: %.5f' % tau_CB)
print('Kendall  AU coefficient: %.5f' % tau_AU)
print('Kendall  AG110 coefficient: %.5f' % tau_AG110)
print('Kendall  AG100 coefficient: %.5f' % tau_AG100)
print('Kendall  AG111 coefficient: %.5f' % tau_AG111)
print('Kendall  TIO2A100 coefficient: %.5f' % tau_TIO2A100)
print('Kendall  TIO2A101 coefficient: %.5f' % tau_TIO2A101)
print('Kendall  GRO coefficient: %.5f' % tau_GRO)
print('Kendall  GR coefficient: %.5f' % tau_GR)
print('Kendall  CdSe coefficient: %.5f' % tau_CdSe)
print('Kendall  Fe2O coefficient: %.5f' % tau_Fe2O)
print('Kendall  Fe2O coefficient: %.5f' % tau_SIO2AM)
print('Kendall  Fe2O coefficient: %.5f' % tau_SIO2Q)
print('Kendall  Tio2R100 coefficient: %.5f' % tau_Tio2R100)
print('Kendall Tio2R110 coefficient: %.5f' % tau_Tio2R110)

