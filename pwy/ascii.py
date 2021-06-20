from pwy.colours import BYELLOW, BWHITE, BGREY, BBLUE, RESET


clear_sky = [
    "{}    \\   /    {}".format(BYELLOW, RESET),
    "{}     .-.     {}".format(BYELLOW, RESET),
    "{}  ‒ (   ) ‒  {}".format(BYELLOW, RESET),
    "{}     `-᾿     {}".format(BYELLOW, RESET),
    "{}    /   \\    {}".format(BYELLOW, RESET)
]


few_clouds = [
    "{}   \\  /       {}".format(BYELLOW, RESET),
    "{} _ /\"\"{}.-.     {}".format(BYELLOW, BWHITE, RESET),
    "{}   \\{}_(   ).-. {}".format(BYELLOW, BWHITE, RESET),
    "{}   /{}(________){}".format(BYELLOW, BWHITE, RESET),
    "{}              {}".format(BGREY, RESET)
]


overcast_cloud = [
    "{}          {}".format(BGREY, RESET),
    "{}  .-.     {}".format(BGREY, RESET),
    "{} (   ).-. {}".format(BGREY, RESET),
    "{}(________){}".format(BGREY, RESET),
    "{}          {}".format(BGREY, RESET)
]


rain = [
    "{}    .-.     {}".format(BGREY, RESET),
    "{}   (   ).-. {}".format(BGREY, RESET),
    "{}  (________){}".format(BGREY, RESET),
    "{}  ‚ʻ‚ʻ‚ʻ‚ʻ  {}".format(BBLUE, RESET),
    "{}  ‚ʻ‚ʻ‚ʻ‚ʻ  {}".format(BBLUE, RESET),
    "            "
]


thunderstorm = [
    "{}  .-.     {}".format(BGREY, RESET),
    "{} (   ).-. {}".format(BGREY, RESET),
    "{}(________){}".format(BGREY, RESET),
    "{}‚ʻ{}⚡{}ʻ‚{}⚡{}‚ʻ{}".format(BBLUE, BYELLOW, BBLUE, BYELLOW, BBLUE, RESET),
    "{}‚ʻ‚ʻ{}⚡{}ʻ‚ʻ {}".format(BBLUE, BYELLOW, BBLUE, RESET),
    "         "
]


snow = [
    "{}  .-.     {}".format(BGREY, RESET),
    "{} (   ).-. {}".format(BGREY, RESET),
    "{}(________){}".format(BGREY, RESET),
    "{}  * * * * {}".format(BWHITE, RESET),
    "{} * * * *  {}".format(BWHITE, RESET)
]


mist = [
    "{}             {}".format(BGREY, RESET),
    "{} _ - _ - _ - {}".format(BGREY, RESET),
    "{}  _ - _ - _  {}".format(BGREY, RESET),
    "{} _ - _ - _ - {}".format(BGREY, RESET),
    "{}             {}".format(BGREY, RESET)
]


unknown = [
    "{}    .-.      {}".format(BWHITE, RESET),
    "{}     __)     {}".format(BWHITE, RESET),
    "{}    (        {}".format(BWHITE, RESET),
    "{}     `-᾿     {}".format(BWHITE, RESET),
    "{}      •      {}".format(BWHITE, RESET)
]