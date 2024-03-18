def calculate_packages(num_people, num_hotdogs_per_person):
    hotdogs_per_package = 10
    buns_per_package = 8

    total_hotdogs_needed = num_people * num_hotdogs_per_person
    total_hotdog_packages = total_hotdogs_needed // hotdogs_per_package
    hotdogs_leftover = total_hotdogs_needed % hotdogs_per_package

    total_buns_needed = total_hotdogs_needed // buns_per_package
    buns_leftover = total_hotdogs_needed % buns_per_package

    # Adjusting for leftover buns
    if hotdogs_leftover > 0:
        total_buns_needed += 1

    return total_hotdog_packages, total_buns_needed, hotdogs_leftover, buns_leftover


def main():
    try:
        num_people = int(input("Enter the number of people attending the cookout: "))
        num_hotdogs_per_person = int(input("Enter the number of hot dogs each person will be given: "))

        hotdog_packages, bun_packages, hotdogs_leftover, buns_leftover = calculate_packages(num_people, num_hotdogs_per_person)

        print(f"\nMinimum number of packages of hot dogs required: {hotdog_packages}")
        print(f"Minimum number of packages of hot dog buns required: {bun_packages}")
        print(f"Number of hot dogs left over: {hotdogs_leftover}")
        print(f"Number of hot dog buns left over: {buns_leftover}")

    except ValueError:
        print("Please enter valid integer values for number of people and number of hot dogs per person.")


if __name__ == "__main__":
    main()
