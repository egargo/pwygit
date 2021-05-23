from wwy.colours import *


overcast_cloud = [
    '{}  .-.     {}'.format(BGREY, RESET),
    '{} (   ).-. {}'.format(BGREY, RESET),
    '{}(________){}'.format(BGREY, RESET)
]


scattered_cloud = [
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


light_rain = [
    '{}    .-.     {}'.format(BGREY, RESET),
    '{}   (   ).-. {}'.format(BGREY, RESET),
    '{}  (________){}'.format(BGREY, RESET),
    '{}    ‚   ‚   {}'.format(BBLUE, RESET),
    '{}  ‚   ‚  ,  {}'.format(BBLUE, RESET)
]

snow = [
    '  .-.     '.format(BGREY, RESET),
    ' (   ).-. '.format(BGREY, RESET),
    '(________)'.format(BGREY, RESET),
    '  * * * * '.format(BWHITE, RESET),
    ' * * * *  '.format(BWHITE, RESET)
]


thunder_rain = [
    '{}  .-.     {}'.format(BGREY, RESET),
    '{} (   ).-. {}'.format(BGREY, RESET),
    '{}(________){}'.format(BGREY, RESET),
    '{}‚ʻ{}⚡{}ʻ‚{}⚡{}‚ʻ{}'.format(BBLUE, BYELLOW, BBLUE, BYELLOW, BBLUE, RESET),
    '{}‚ʻ‚ʻ{}⚡{}ʻ‚ʻ {}'.format(BBLUE, BYELLOW, BBLUE, RESET)
]
