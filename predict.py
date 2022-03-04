import csv


def predict(x, t0, t1):
    return t0 + t1 * x


while True:
    try:
        mileage = float(input('input mileage: '))
        if mileage < 0:
            raise ValueError
        break
    except ValueError:
        print('You inputed wrong number! Try again!')

thetas = []
with open('thetas.csv', 'r') as thetas_f:
    csv_reader = csv.reader(thetas_f)
    header = next(csv_reader)
    for row in csv_reader:
        thetas.append(row)

theta0 = float(thetas[-1][0])
theta1 = float(thetas[-1][1])
print('Predicted price: ', predict(mileage, theta0, theta1))
