from wwy.colours import *


overcast_cloud = [
    '{}  .-.     {}'.format(BGREY, RESET),
    '{} (   ).-. {}'.format(BGREY, RESET),
    '{}(________){}'.format(BGREY, RESET)
]


few_clouds = [
    '{}   \\  /      {}'.format(BYELLOW, RESET),
    '{} _ /\"\"{}.-.     {}'.format(BYELLOW, BWHITE, RESET),
    '{}   \\{}_(   ).-. {}'.format(BYELLOW, BWHITE, RESET),
    '{}   /{}(________){}'.format(BYELLOW, BWHITE, RESET)
]


clear_sky = [
    '{}    \\   /   {}'.format(BYELLOW, RESET),
    '{}     .-.     {}'.format(BYELLOW, RESET),
    '{}  ‒ (   ) ‒  {}'.format(BYELLOW, RESET),
    '{}     `-᾿     {}'.format(BYELLOW, RESET),
    '{}    /   \\   {}'.format(BYELLOW, RESET)
]


rain = [
    '{}    .-.     {}'.format(BGREY, RESET),
    '{}   (   ).-. {}'.format(BGREY, RESET),
    '{}  (________){}'.format(BGREY, RESET),
    '{}  ‚ʻ‚ʻ‚ʻ‚ʻ  {}'.format(BBLUE, RESET),
    '{}  ‚ʻ‚ʻ‚ʻ‚ʻ  {}'.format(BBLUE, RESET)
]


snow = [
    '  .-.     '.format(BGREY, RESET),
    ' (   ).-. '.format(BGREY, RESET),
    '(________)'.format(BGREY, RESET),
    '  * * * * '.format(BWHITE, RESET),
    ' * * * *  '.format(BWHITE, RESET)
]


thunderstorm = [
    '{}  .-.     {}'.format(BGREY, RESET),
    '{} (   ).-. {}'.format(BGREY, RESET),
    '{}(________){}'.format(BGREY, RESET),
    '{}‚ʻ{}⚡{}ʻ‚{}⚡{}‚ʻ{}'.format(BBLUE, BYELLOW, BBLUE, BYELLOW, BBLUE, RESET),
    '{}‚ʻ‚ʻ{}⚡{}ʻ‚ʻ {}'.format(BBLUE, BYELLOW, BBLUE, RESET)
]

mist = [
    ' _ - _ - _ - '.format(BGREY, RESET),
    '  _ - _ - _  '.format(BGREY, RESET),
    ' _ - _ - _ - '.format(BGREY, RESET)
]