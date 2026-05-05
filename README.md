**Servos:** 
0: right front knee
1: right front hip
2: right side knee
3: right side hip 
4: right back knee
5: right back hip
6: left back knee
7: left back hip
8: left side knee
9: left side hip
10: left front knee
11: left front hip

virtual environemnt: 
source ~/spyderbot-env/bin/activate

for right side hips: positive angle is foward
for left side hips: positive angle is backward


moving foward: 
lift left before moving foward
# spyderbot.move_hips_forward_group_abs('left')

        # spyderbot.lower_knees_group('left')

        # spyderbot.lift_knees_group('right')

        # spyderbot.move_hips_backward_group_abs('left')

        # spyderbot.move_hips_forward_group_abs('right')

        # spyderbot.lower_knees_group('right')

        # spyderbot.lift_knees_group('left')

        # spyderbot.move_hips_backward_group_abs('right')

    lower left at end of for loop
