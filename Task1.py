from sys import argv

def salary_function():
    try:
        money_perhour, stavkaperhour, overbasicincome = map(float, argv[1:0])


        print(f"salalry-{(money_perhour*stavkaperhour)+overbasicincome}")
    except ValueError:
        print('Введите числа, а не строки и не символы')

salary_function()
