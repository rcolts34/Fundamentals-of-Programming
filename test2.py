
def user_info():
    try:
        result = ""
        name = input("Enter your name: ")
        dob = int(input("Enter your birth year: "))
        budget = int(input("Enter your budget: "))
        price = int(input("Enter the price of the product: "))
        result = f"Hello {name}! You are {2024-dob} years old and you can buy {round(budget/price)} products."
    except ValueError as e:
        print("Something went wrong -", e)
    except ZeroDivisionError as e:
        print("Something went wrong - ", e)
    except Exception as e:
        print("Something went wrong -", e)
    else:
        print("From else: ", result)
    finally:
        return result

print(user_info())




# except ValueError as e:
# print("Something went wrong -", e)
# except ZeroDivisionError as e:
# print("Something went wrong - ", e)
# except Exception as e:
# print("Something went wrong -", e)





