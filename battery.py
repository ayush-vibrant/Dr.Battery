file1 = open('/sys/class/power_supply/BAT0/capacity','r')
file2 = open('/sys/class/power_supply/BAT0/status','r')
charging_status = file2.read()
charging_status = charging_status.rstrip('\r\n').lower()
flag = 1 if (charging_status == 'charging') else 0

battery_percentage = int(file1.read())


if (battery_percentage) < 40:
    message =  'Plug in your charger battery is less then 40%.' if charging_status == 'discharging' else 'Charger is already plugged in.'

if (battery_percentage) > 80:
    message = 'Plug out your charger battery is more then 80%.' if charging_status == 'charging' else 'Battery is in safe state.'

if 40 <= (battery_percentage) <= 80:
    message = 'Battery is ' + charging_status + ' despite being in safe state, kindly remove the charger.' if (flag == 1) else 'Battery is in safe state.'

