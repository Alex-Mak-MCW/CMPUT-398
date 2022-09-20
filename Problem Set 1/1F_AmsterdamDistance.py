"""
  Alex Mak
  1584710

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  - https://www.cuemath.com/geometry/arc-length/

  List any classmate you discussed the problem with. Remember, you can only
  have high-level verbal discussions. No code should be shared, developed,
  or even looked at in these chats. No formulas or pseudocode should be
  written or shared in these chats.

  I have not discussed with anyone in this problem

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 403.
"""

import numpy as np
lines=[]
# Read the inputs in a for loop, then assign them to a list in order to reassign them for each variable
for i in range(2):
    lines.append(input().split(" "))
# Assign variables from list elements
M=float(lines[0][0])
N=float(lines[0][1])
R=float(lines[0][2])
ax=float(lines[1][0])
ay=float(lines[1][1])
bx=float(lines[1][2])
by=float(lines[1][3])

# The subdistance equals to overall radius/ # of circle rings, always <= the R, used for both computing horizontal and vertical distance
subradius=R/N

# I can think of 2 ways to find the distance, then choose the shorter one
# Method 1 (with horizontal distance): Go outer/inner on the circle(go veritcally from the radius) then walk horizontally (on the arc left/right)
# Method 2 (no horizontal distance at all): Go to the center of the circle by walking inner/ outer of the circle, rare/ special case

# Method 1 from above:

# Veritcal distance, found by the product of subradius and difference of both y's, use aboslute to prevent negative values
v_dist=subradius*abs(ay-by)

# Horizontal distance, found by determining the arc length of the inner circle
# Regular arc length formula: radian(pi)*r
# For this limited semi-circle: still pi*r, but needs more calculation on r (denoted new_r)
# new_r is the new radius: computed the product of subradius, the length of inner y, and the horizontal distance (denoted sub_h)
# sub_h is the new horizontal length difference of the 2 points, then divide by M, similar concept to v_dist above

# I learned the arc length formula from the link below
# https://www.cuemath.com/geometry/arc-length/

sub_h=abs(ax-bx)/M
new_r=subradius*min(ay,by)*sub_h
h_dist=np.pi*new_r
# add the vertical and horizontal distances together to reach total distance for this method
dist1=v_dist+h_dist

# Method 2 above, no horizontal distances
dist2=subradius*abs(ay+by)

# Fint the minimum distance of both methods to get the shortest distance
print(min(dist1,dist2))