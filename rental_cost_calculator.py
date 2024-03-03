# -----------------constants-----------------
# first user input: key->vehicle type, value->rate per day.
VEHICLE_TYPE_MAP = {"Compact": 25, "Sedan": 35, "SUV": 50, "Luxury": 60}
# second user input: key->rental duration in days, value->discount
RENTAL_DURATION_MAP = {"1": 0, "2": 0.04, "4": 0.1, "8": 0.2}
# final user input: key->extra features or services, value->rate per day. [⛔️ Restrictions: each feature only be added once]
EXTRA_FEATURES_MAP = {"GPS Navigation": 5, "Mobile Wi-Fi": 8,
                      "Child Seat": 2, "Toll Pass": 4.5, "Roadside Assistance Plus": 5}
# GST ratio
GST_RATIO = 0.05

# PHASE_SHIFT
PHASE_SHIFT = 20

# output strings
STR_RENTAL_NUM = "Number of vehicles rented:"
STR_AMOUNT_DUE = "Amount due before tax:"
STR_GST = "GST:"
STR_TOTAL_AMOUNT = "Total amount due:"


# -----------------processing------------------
welcome = "~ Welcome to Best Cars Inc. ~"
waves = "".rjust(len(welcome), "~")
print(waves)
print(welcome)
print(waves)

rental_num = 0
amount_before_tax = 0
gst_amount = 0
total_amount = 0
flag = "y"
while flag.lower() == "y":
    # step 1: get model price
    v_title = "Vehicle Type"+"Daily Rate".rjust(PHASE_SHIFT)
    print("Step 1. Choose the type of vehicle you wish to rent.")
    print(v_title)
    v_types = list(VEHICLE_TYPE_MAP.keys())
    # print type info
    for i in range(1, 5):
        v_item = v_types[i-1]
        v_ps = len(v_title) - (len(v_item) + 4)
        val = VEHICLE_TYPE_MAP.get(v_item)
        print(f" {i}. {v_item}{val:>{v_ps}}")
    v_sel = int(input("Your Selection: "))
    # check selection range
    while v_sel not in range(1, 5):
        print("Invalid selection. Please enter one of the option numbers displayed.")
        v_sel = int(input("Your Selection: "))
    v_price = VEHICLE_TYPE_MAP.get(v_types[v_sel-1])
    print(f"You have chosen a Compact. The base rental rate is ${
          v_price:.2f} per day")
    print("\n")
    rental_num += 1

    # step 2: calculate basic price apply discount
    print("Step 2. Specify the duration of this vehicle rental.")
    input_days = int(input("Enter the number of days needed: "))
    while input_days <= 0:
        print("Error: Value cannot be less than 1.")
        input_days = int(input("Enter the number of days needed: "))
    # get basic price
    base_price = v_price * input_days
    # apply discount
    # 1. deduce rate
    discount_rate = 0
    if input_days == 1:
        pass
    elif 2 <= input_days < 4:
        discount_rate = RENTAL_DURATION_MAP["2"]
    elif 4 <= input_days < 8:
        discount_rate = RENTAL_DURATION_MAP["4"]
    else:
        discount_rate = RENTAL_DURATION_MAP["8"]
    daily_rate = v_price - v_price * discount_rate
    # 2. apply rate to base price
    updated_price = base_price - base_price * discount_rate
    # discount to show on the screen by timing 100
    rate_display = discount_rate * 100
    print(f"Discount to be applied is {rate_display}%")
    print(f"Your discounted rental rate is ${daily_rate:.2f} per day")
    print("\n")

    # step 3: feature fees
    print("Step 3. Choose your desired additional features or services.")
    f_title = "Option" + "Daily Rate".rjust(PHASE_SHIFT)

    print(f_title)
    f_names = list(EXTRA_FEATURES_MAP.keys())
    selected_features = {}
    # add multiple features
    while True:
        # print feature info
        for i in range(1, 6):
            f_item = f_names[i-1]
            ps = len(f_title)-(len(f_item) + 4)
            val = EXTRA_FEATURES_MAP.get(f_item)
            f_info = f" {i}. {f_item}{val:>{ps}}"
            if selected_features.get(f_item) is not None:
                print(f_info, " ✓")
            else:
                print(f_info)
        f_sel = input("Enter option # or 0 to proceed: ")
        # check if already selected type
        # end loop
        if f_sel in ('#','0'):
            break
        # check the value
        f_sel = int(f_sel)
        while f_sel not in range(1, 6):
            f_sel = int(input("Please select from 1 to 5: "))
        sel_name = f_names[f_sel-1]
        if selected_features.get(sel_name) is not None:
            print("\n")
            print("You've already selected this feature. Please select another one. ")
            continue
        selected_features.update({sel_name:1})
        f_price = EXTRA_FEATURES_MAP.get(sel_name)
        print("Feature: ", f"{sel_name} ",
              "added for $", f"{f_price:.2f}")
        updated_price += f_price * input_days

    # add price to the raw price
    amount_before_tax += updated_price
    # print success info
    print("\n")
    print(f"Success! Your reservation for a {input_days} day Compact rental is complete.")
    print(f"The price (not including GST) is ${updated_price/input_days} per day or ${updated_price} for the rental.")
    flag = input("Do you want to rent another vehicle? (Y/N): ")

# print price list
print("\n")
waves = "".rjust(50, "~")
print(waves)
print(f"~~~{'RENTAL BILLING SUMMARY':^44}~~~")
waves_len = len(waves)
# print rental num
p_rn = waves_len - len(STR_RENTAL_NUM)
print(f"{STR_RENTAL_NUM}{rental_num:>{p_rn},.2f}")
# print amount before tax
p_ad = waves_len - len(STR_AMOUNT_DUE)
print(f"{STR_AMOUNT_DUE}{amount_before_tax:>{p_ad},.2f}")
# print gst amount
gst_amount = amount_before_tax * GST_RATIO
p_gst = waves_len - len(STR_GST)
print(f"{STR_GST}{gst_amount:>{p_gst},.2f}")
# print total
p_ta = waves_len - len(STR_TOTAL_AMOUNT)
total_amount = amount_before_tax + gst_amount
print(f"{STR_TOTAL_AMOUNT}{total_amount:>{p_ta},.2f}")
print(waves)
print("Thank you for choosing Best Cars!")
