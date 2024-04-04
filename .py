from sklearn.linear_model import LinearRegression

def get_previous_winning_numbers():
    previous_winning_numbers = []
    for i in range(2):
        numbers = input(f"Enter the {i+1}st set of 5 winning numbers separated by spaces: ").strip().split()
        previous_winning_numbers.append([int(num) for num in numbers])
    return previous_winning_numbers

def predict_next_winning_numbers(previous_winning_numbers):
    X = [num for sublist in previous_winning_numbers for num in sublist]
    X = [[num] for num in X]
    y = [num for sublist in previous_winning_numbers[-1:] for num in sublist]

    model = LinearRegression()
    model.fit(X[:-5], y)

    next_numbers = model.predict([X[-5:]])[0]
    return next_numbers

def main():
    previous_winning_numbers = get_previous_winning_numbers()
    next_winning_numbers = predict_next_winning_numbers(previous_winning_numbers)

    print("Predicted next winning numbers:", next_winning_numbers)

if __name__ == "__main__":
    main()
