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

    syphax = [
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

    unit = 's'

    print("~"*3 + " Syphax's Data " + "~"*30)

    # Calculate mean and standard deviation of Syphax's Data.
    mu_heads, sigma_heads = get_mu_and_sigma(syphax)
    print(f"{'Mean ':-<30} {round(mu_heads, 10):<12} {unit}")
    # print(f"{'Standard deviation ':-<30} {round(sigma_heads, 10):<12} °")

    # Calculate the statistical uncertainty of Syphax's Data.
    statistical_un_heads = get_statistical_un(sigma_heads, len(syphax))
    print(f"{'Statistical uncertainty ':-<30} {round(statistical_un_heads, 10):<12} {unit}")

    # Calculate the systematic uncertainty of Syphax's Data.
    systematic_un_heads = 0.01
    print(f"{'Systematic uncertainty ':-<30} {systematic_un_heads:<12} {unit}")

    # Calculate the uncertainty of Syphax's Data.
    uncertainty_angle = get_uncertainty(statistical_un_heads, systematic_un_heads)
    print(f"{'Uncertainty ':-<30} {round(uncertainty_angle, 10):<12} {unit}")

    # Calculate the angle for Syphax's Data.
    angle_for_heads = str(round(mu_heads, 2)) + " ± " + str(round(uncertainty_angle, 2))
    print(f"{'Time ':-<30} {angle_for_heads:<12} {unit}")

    # Plot the histogram of Syphax's Data.
    heads_title = "Histogram of the time measured"
    show_histogram(syphax, mu_heads, sigma_heads, heads_title)

if __name__ == "__main__":
    main()