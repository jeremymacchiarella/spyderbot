from spyderbot import Spyderbot
import atexit
import time

STEP_DELAY = 0.02
MICROSTEPS = 10

TRIPOD_A_KNEES = [0, 4, 8]
TRIPOD_A_HIPS = [1, 5, 9]

TRIPOD_B_KNEES = [2, 6, 10]
TRIPOD_B_HIPS = [3, 7, 11]


def move_3_servos_smooth(bot, servo_1, servo_2, servo_3,
                         target_1, target_2, target_3,
                         steps, delay):
    """
    Smoothly move 3 servos from their current angles
    to their target angles.
    """

    start_1 = bot.kit.servo[servo_1].angle
    start_2 = bot.kit.servo[servo_2].angle
    start_3 = bot.kit.servo[servo_3].angle

    if start_1 is None or start_2 is None or start_3 is None:
        print("Error: one of the servos has angle None")
        return

    step_number = 1

    while step_number <= steps:
        fraction = step_number / steps

        angle_1 = start_1 + (target_1 - start_1) * fraction
        angle_2 = start_2 + (target_2 - start_2) * fraction
        angle_3 = start_3 + (target_3 - start_3) * fraction

        bot.move_servo(servo_1, int(angle_1))
        bot.move_servo(servo_2, int(angle_2))
        bot.move_servo(servo_3, int(angle_3))

        time.sleep(delay)
        step_number = step_number + 1


def lift_tripod_a(bot):
    move_3_servos_smooth(
        bot,
        TRIPOD_A_KNEES[0], TRIPOD_A_KNEES[1], TRIPOD_A_KNEES[2],
        100, 100, 100,
        MICROSTEPS,
        STEP_DELAY
    )


def lower_tripod_a(bot):
    move_3_servos_smooth(
        bot,
        TRIPOD_A_KNEES[0], TRIPOD_A_KNEES[1], TRIPOD_A_KNEES[2],
        64, 64, 64,
        MICROSTEPS,
        STEP_DELAY
    )


def lift_tripod_b(bot):
    move_3_servos_smooth(
        bot,
        TRIPOD_B_KNEES[0], TRIPOD_B_KNEES[1], TRIPOD_B_KNEES[2],
        100, 100, 100,
        MICROSTEPS,
        STEP_DELAY
    )


def lower_tripod_b(bot):
    move_3_servos_smooth(
        bot,
        TRIPOD_B_KNEES[0], TRIPOD_B_KNEES[1], TRIPOD_B_KNEES[2],
        64, 64, 64,
        MICROSTEPS,
        STEP_DELAY
    )


def move_tripod_a_forward(bot):
    move_3_servos_smooth(
        bot,
        TRIPOD_A_HIPS[0], TRIPOD_A_HIPS[1], TRIPOD_A_HIPS[2],
        110, 110, 70,
        MICROSTEPS,
        STEP_DELAY
    )


def move_tripod_a_back_to_middle(bot):
    move_3_servos_smooth(
        bot,
        TRIPOD_A_HIPS[0], TRIPOD_A_HIPS[1], TRIPOD_A_HIPS[2],
        90, 90, 90,
        MICROSTEPS,
        STEP_DELAY
    )


def move_tripod_b_forward(bot):
    move_3_servos_smooth(
        bot,
        TRIPOD_B_HIPS[0], TRIPOD_B_HIPS[1], TRIPOD_B_HIPS[2],
        110, 70, 70,
        MICROSTEPS,
        STEP_DELAY
    )


def move_tripod_b_back_to_middle(bot):
    move_3_servos_smooth(
        bot,
        TRIPOD_B_HIPS[0], TRIPOD_B_HIPS[1], TRIPOD_B_HIPS[2],
        90, 90, 90,
        MICROSTEPS,
        STEP_DELAY
    )


def main():
    bot = Spyderbot()
    atexit.register(bot.shutdown)
    time.sleep(1)

    lift_tripod_a(bot)

    time.sleep(1)

    # while True:
    #     # tripod A step
    #     lift_tripod_a(bot)
    #     move_tripod_a_forward(bot)
    #     lower_tripod_a(bot)
    #     move_tripod_a_back_to_middle(bot)

    #     # tripod B step
    #     lift_tripod_b(bot)
    #     move_tripod_b_forward(bot)
    #     lower_tripod_b(bot)
    #     move_tripod_b_back_to_middle(bot)


if __name__ == "__main__":
    main()