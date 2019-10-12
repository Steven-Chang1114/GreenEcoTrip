import requests

def find_train(origin, destination):
    directions = requests.get('https://maps.googleapis.com/maps/api/directions/json?origin={}&destination={}' \
                              '&mode=transit&key=AIzaSyCUPvUnI4COqOfF73iRo32tRd8wQp_M4f8')
    return directions


if __name__ == '__main__':
    find_train('Edinburgh,UK', 'Paris,France')