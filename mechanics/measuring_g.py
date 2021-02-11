''' Measuring G '''
import math
import statistics
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def get_mu_and_sigma(data):
    ''' Returns the mean and the standard deviation of the data '''
    return statistics.mean(data), statistics.stdev(data)

def show_histogram(data, mu, sigma, title):
    ''' Displays the histogram of the data based on its mean and standard deviation '''
    mu = statistics.mean(data)
    sigma = statistics.stdev(data)

    plt.hist(data, density=True)

    # Label some stuff!
    plt.xlabel("Time (s)")
    plt.ylabel("Frequency")
    plt.title(title)

    x = np.linspace(start=mu-4*sigma, stop=mu+4*sigma, num=100)
    y = [1/math.sqrt(2*math.pi*sigma**2)*math.exp(-(i - mu)**2/(2*sigma**2)) for i in x]
    plt.plot(x, y, color="orange")

    # Plot the mean line
    plt.axvline(mu, color='red', linestyle='dashed', linewidth=1)
    min_ylim, max_ylim = plt.ylim()
    plt.text(mu*1.1, max_ylim*0.9, 'Mean: {:.2f}'.format(mu))

    # Display!
    plt.show()

def get_statistical_un(std, n):
    ''' Returns the statistical uncertainty '''
    return (std * 2)/(math.sqrt(n))

def get_uncertainty(statistical_un, systematic_un):
    ''' Returns the uncertainty '''
    return math.sqrt(statistical_un**2 + systematic_un**2)

def main():
    ''' Main '''
    sns.set()

    time = [
        1.1,
        1.1,
        1.08,
        1.12,
        1.09,
        1.1,
        1.1,
        1.1,
        1.09,
        1.11,
        1.09,
        1.09,
        1.1,
        1.11,
        1.1
    ]

    unit = {
        'time': 's'
    }

    print("~"*3 + " Time Data " + "~"*30)

    # Calculate mean and standard deviation of the time data.
    mu_time, sigma_time = get_mu_and_sigma(time)
    print(f"{'Mean ':-<30} {round(mu_time, 10):<12} {unit['time']}")

    # Calculate the statistical uncertainty of the time data.
    statistical_un_time = get_statistical_un(sigma_time, len(time))
    print(f"{'Statistical uncertainty ':-<30} {round(statistical_un_time, 10):<12} {unit['time']}")

    # Calculate the systematic uncertainty of the time data.
    systematic_un_time = 0.0033
    print(f"{'Systematic uncertainty ':-<30} {systematic_un_time:<12} {unit['time']}")

    # Calculate the uncertainty of the time data.
    uncertainty_time = get_uncertainty(statistical_un_time, systematic_un_time)
    print(f"{'Uncertainty ':-<30} {round(uncertainty_time, 10):<12} {unit['time']}")

    # Display the time with uncertainty.
    time_with_un = str(round(mu_time, 2)) + " ± " + str(round(uncertainty_time, 3))
    print(f"{'Time ':-<30} {time_with_un:<12} {unit['time']}")

    # Plot the histogram of the time data.
    time_title = "Histogram of the time measured"
    show_histogram(time, mu_time, sigma_time, time_title)

if __name__ == "__main__":
    main()
