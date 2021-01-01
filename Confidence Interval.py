# the point of this file is to make a function that will take in a list of numbers or already be given
# the sample mean and sample s.d., and pump out the confidence interval.

# Importing the packages I need
import statistics as stats
import scipy.stats as scst
import math

#----------------------------------------------------------------------------------------------
# creating function for a normal distribution

def norm_con_int(percent,values=0,average=0,samp_sd=0,n=0):
    if average == 0:
        a = stats.mean(values)
        s = math.sqrt(stats.variance(values))
        z = scst.norm.ppf(1-((1-percent)/2))
        u = len(values)
        lb = a - z*(s/math.sqrt(u))
        ub = a + z*(s/math.sqrt(u))
        return (lb,ub)
    if average != 0:
        z = scst.norm.ppf(1-((1-percent)/2))
        lb = average - z*(samp_sd/math.sqrt(n))
        ub = average + z*(samp_sd/math.sqrt(n))
        return (lb,ub)


# ----------------------------------------------------------------------------------------

# now lets to a t distribution

def t_con_int(percent,values=0,average=0,samp_sd=0,n=0):
    if average == 0:
        a = stats.mean(values)
        s = math.sqrt(stats.variance(values))
        u = len(values)
        df = u-1
        t = scst.t.ppf(1-((1-percent)/2),df)
        lb = a - t*(s/math.sqrt(u))
        ub = a + t*(s/math.sqrt(u))
        return (lb,ub)
    if values == 0:
        df = n-1
        t = scst.t.ppf(1-((1-percent)/2),df)
        lb = average - t*(samp_sd/math.sqrt(n))
        ub = average + t*(samp_sd/math.sqrt(n))
        return (lb,ub)


# -------------------------------------------------------------------------------------------

# now time to do difference with t dist

def t_diff_con_int(percent,values_1=0,values_2=0,average_1=0,average_2=0,sd_1=0,sd_2=0,n_1=0,n_2=0):
    if values_1 != 0:
        a_1 = stats.mean(values_1)
        a_2 = stats.mean(values_2)
        s_1 = stats.variance(values_1)
        s_2 = stats.variance(values_2)
        u_1 = len(values_1)
        u_2 = len(values_1)
        df = u_1 + u_2 - 2
        t = scst.t.ppf(1 - ((1 - percent) / 2), df)
        Sp = ((((u_1-1)*s_1)+((u_2-1)*s_2))/df)
        diff = (a_1 - a_2)
        lb = diff - t*math.sqrt(Sp)*math.sqrt((1/u_1)+(1/u_2))
        ub = diff + t*math.sqrt(Sp)*math.sqrt((1/u_1)+(1/u_2))
        return (lb,ub)
    if average_1 != 0:
        df = n_1 + n_2 - 2
        t = scst.t.ppf(1 - ((1 - percent) / 2), df)
        Sp = ((((n_1 - 1) * (sd_1**2)) + ((n_2 - 1) * (sd_2**2))) / df)
        diff = average_1 - average_2
        lb = diff - t*math.sqrt(Sp)*math.sqrt((1/n_1)+(1/n_2))
        ub = diff + t*math.sqrt(Sp)*math.sqrt((1/n_1)+(1/n_2))
        return (lb,ub)

