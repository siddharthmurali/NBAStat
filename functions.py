# Author: Kaustubh Kulkarni
# Date: 11/24/15

# Team metrics
def possessions(fga,fta,orb,to):
    return fga + 0.44*fta - orb + to

def ts(points,fga,fta):
   return 0.5*points/(fga+0.44*fta)


# Main method
def main():
    print ts(118,89,13)

if __name__ == "__main__":
    main()
