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

params = []
with open('thetas.csv', 'r') as thetas_f:
    csv_reader = csv.reader(thetas_f)
    header = next(csv_reader)
    for row in csv_reader:
        params.append(row)

theta0 = float(params[-1][0])
theta1 = float(params[-1][1])
mean_val = float(params[-1][2])
std_val = float(params[-1][3])
if std_val == 0:
    std_val = 1
mileage = (mileage - mean_val) / std_val
print('Predicted price: ', predict(mileage, theta0, theta1))
