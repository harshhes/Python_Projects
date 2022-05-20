import random

when= ['Day before Yesterday', 'A few years ago', 'Last night', 'On 8th of April',
        'On 23rd August']

who = ['Eric', 'Dwayne', 'Ranveer', 'Harsh', 'Sabreena', 'Travis', 'Kylie']

where = ['Meeting', 'Hotel', "School", "University", "Mall", 'Get Together']

what = ["Ate a pizza", 'Met amazing folks', 'Clicked lots of photographs', 'Wrote a book']

print(random.choice(when)+ ", " + random.choice(who) + " went to the "+ random.choice  (where) + "," + " and "+ random.choice(what) )