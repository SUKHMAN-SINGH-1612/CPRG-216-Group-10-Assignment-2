# -----------------constants-----------------
# first user input: key->vehicle type, value->rate per day.
VEHICLE_TYPE_MAP = {"Compact":25,"Sedan":35,"SUV":50,"Luxury":60}
# second user input: key->rental duration in days, value->discount
RENTAL_DURATION_MAP = {"1":0,"2":0.04,"4":0.1,"8":0.2}
# final user input: key->extra features or services, value->rate per day. [⛔️ Restrictions: each feature only be added once]
EXTRA_FEATURES_MAP = {"GPS Navigation":5,"Mobile Wi-Fi":8,"Child Seat":2,"Toll Pass":4.5,"Roadside Assistance Plus":5}

# PHASE_SHIFT
PHASE_SHIFT = 20

# selected features: key->feature name, value->selected times
features = {"GPS":2}
# terminating loop signal
terminate_signal = '1'



# -----------------display and validation------------------
welcome = "~ Welcome to Best Cars Inc. ~"
waves = "".rjust(len(welcome),"=")
print(waves)
print(welcome)
print(waves)

# step 1: get model price
v_title = "Vehicle Type"+"Daily Rate".rjust(PHASE_SHIFT)
print("Step 1. Choose the type of vehicle you wish to rent.")
print(v_title)
v_types = VEHICLE_TYPE_MAP.keys()
# print type info
for i in range(1,5):
    v_ps = len(v_title)-len(v_types[i-1]+4)
    val = VEHICLE_TYPE_MAP.get(v_types[i-1])
    print(" {i}. {v_types[0]}","{:>v_ps}".format(val))
v_sel = int(input("Your Selection: "))
# check selection range
while v_sel not in range(1,5):
    v_sel = input("Please select from 1 to 4: ")
v_price = VEHICLE_TYPE_MAP.get(v_types[v_sel-1])
print("You have chosen a Compact. The base rental rate is ${v_price:.2f} per day")
print("\n")

# step 2: calculate basic price apply discount
print("Step 2. Specify the duration of this vehicle rental.")
input_days = int(input("Enter the number of days needed: "))
while input_days <= 0:
    input_days = int(input("Please input valid rental days: "))
# get basic price
base_price = v_price * input_days
# apply discount 
#   1. deduce rate
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
#   2. apply rate to base price
updated_price = base_price - base_price * discount_rate
rate_display = discount_rate * 100
print("Discount to be applied is {rate_display}%")
print(f"Your discounted rental rate is ${daily_rate:.2f} per day")

# step 3: feature fees
print("Step 3. Choose your desired additional features or services.")
f_title = "Option" + "Daily Rate".rjust(PHASE_SHIFT)
flag = "y"
while flag.lower() == "y":
    print(f_title)
    f_names = EXTRA_FEATURES_MAP.keys()
    selected_features = {}
    # add multiple features
    while True:
        # print feature info
        for i in range(1,6):
            ps = len(f_title)-len(f_names[i-1]+4)
            val = EXTRA_FEATURES_MAP.get(f_names[i-1])
            f_info = f" {i}. {f_names[0]}{val:>ps}"
            if len(selected_features) != 0:
                print(f_info," ✓")
            print(f_info)
        f_sel = input("Enter option # or 0 to proceed: ")
        # end loop
        if f_sel == '#' or '0':
            break
        # check the value
        while f_sel not in range(1,6):
            f_sel = input("Please select from 1 to 5: ")
        selected_features.add(f_sel)
        f_price = EXTRA_FEATURES_MAP.get(f_names[f_sel-1])
        print("Feature: ",f"{f_names[f_sel-1]} ","added for $",f"{f_price:.2f}")

# print success info
print("Success! Your reservation for a 3 day Compact rental is complete.")
# TODO: 
print("The price (not including GST) is $26.00 per day or $78.00 for the rental.")
flag = input("Do you want to rent another vehicle? (Y/N): ")



# ------obsolete-------
while terminate_signal !='0':
    

# -----------------calculation-----------------
# ⚠️ Note: Depending on availability at check-in time,
#   up to two extra child seats may be included at no additional charge.

# function: calculate and display selected type for specified days with discount applied and additional feature fees.
# parameters: days
# return: total amount  type: Float(rounded)
# 1. decide the base type and base price
if input_days is not int:
    print("input int days")
    exit()
v_price = VEHICLE_TYPE_MAP.get(v_type)
if v_price is None:
    print("select the right vehicle type")
    exit()
base_price = v_price * input_days
# 2. apply discount
#   2.1 deduce rate
discount_rate = 0
if input_days == 1:
    pass
elif 2 <= input_days < 4:
    discount_rate = RENTAL_DURATION_MAP["2"]
elif 4 <= input_days < 8:
    discount_rate = RENTAL_DURATION_MAP["4"]
else:
    discount_rate = RENTAL_DURATION_MAP["8"]
#   2.2 apply rate to base price
updated_price = base_price - base_price * discount_rate
# 3. add feature fees
for key in features:
    times = features.get(key)
    feature_rate = EXTRA_FEATURES_MAP.get(key)
    if feature_rate is None:
        print("ERROR: {} feature doesn't exist",key)
        continue
    feature_fee = feature_rate * input_days
    if key == "Child Seat" and times <= 2:
        feature_fee = 0
    updated_price += feature_fee

# -----------------append total display-----------------